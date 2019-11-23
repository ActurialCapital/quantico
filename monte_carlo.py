import numpy as np
from random import random
from scipy.stats import norm
import pandas as pd

def inverse_poisson(u, l):
    p = np.exp(-l)
    F = p
    n = 0
    while u > F:
        n = n + 1
        p = p * (l / n)
        F = F + p           	
    invpoisson = n
    return invpoisson
    
def simulations(
        S0=100,
        rf=0.05,
        sigma=0.2,
        n_iter=100,
        n_simul=100,
        t=1,
        l=2,
        mu_y=0.02,
        var_y=0.25,
        K=100
    ):
    list_simul = []
    list_jumps = []
    dt = t / n_iter
    Sum = 0    
    for m in range(0, n_simul):
        ts=[S0]
        jump = 0
        S = S0
        n_jump = 0
        for i in range(0, n_iter):
            u = random()
            alea_normal = norm.ppf(u)
            alea_poisson = inverse_poisson(u, l * dt)
            if alea_poisson == 0:
                jump = 0
            else:
                for j in range(0, alea_poisson):
                    jump = jump * norm.ppf(random(), loc=mu_y, scale=var_y)
                    
            x = np.log(S) + (rf - sigma * sigma * 0.5) * dt + np.sqrt(dt) * sigma * alea_normal + jump
            S = np.exp(x)
            ts.append(S)
            n_jump = n_jump + alea_poisson
            
        list_simul.append(pd.Series(ts))
        
        payoff = np.max(S - K, 0)
        Sum = Sum + np.exp(-rf * t) * payoff
        list_jumps.append(n_jump)
    price = (1 / n_simul) * Sum
    return {'price': price, 'simulation': list_simul, 'jumps': list_jumps}


if __name__ == '__main__':
    
    from pyStrap import pystrap
    from pyStrap.highcharts import highcharts as hc
    import os
    
    # calc simulations
    DICT = simulations(
        S0=100,
        rf=0,
        sigma=0.30,
        n_iter=100,
        n_simul=100,
        t=1,
        l=100,
        mu_y=0,
        var_y=0.20,
        K=100
    )
    
    df = pd.DataFrame(DICT['simulation'])
    df.stack().hist()

    
    
    
    # create plot
    plt = hc.plot()
    for i in  range(0, 100):
        plt.add({'data': pd.DataFrame(DICT['simulation'][i]), 'type': 'line'})
    plt = plt.draw(setting=12, title='pyStrap', x_axis_type='linear') 
   
    # create dashboard      
    path = os.getcwd() + r'\examples'              
    doc_name = 'poisson_process.html'
    dashboard = pystrap.Figure(path=path, doc_name=doc_name)
    dashboard.insert(pystrap.grid.open_row())
    dashboard.insert(plt)
    dashboard.insert(pystrap.grid.close_row())
    dashboard.show() 
