<!-- PROJECT LOGO -->
<br />
<p align="center">
  <a href="https://github.com/ActurialCapital/quantico">
    <img src="https://github.com/ActurialCapital/quantico/blob/master/images/img1.png" width="50%" height="50%">
  </a>

  <h2 align="center">Quantico</h2>

  <p align="center">
  <b>MARKET REGIME + IDIOSYNCRASIES</b>
  </p>
 
## Table of Contents
<a href="https://www.linkedin.com/in/jean-meilhoc-ricaume-0326aa25">
  <img src="https://github.com/ActurialCapital/pyStrap/blob/master/data/icons/linkedin.svg">
</a>
<br>

* [About the Project](#about-the-project)
  * [Introduction](#introduction)
  * [Model Assumptions](#model-assumptions)
  * [Built With](#built-with)
* [Quick Start](#quick-start)
* [Author](#author)
* [License](#license)

## About the Project

### Introduction

The Poisson process model for Monte Carlo methods is used to simulate a particular market regime, taking into account idiosyncrasies.

### Model assumptions

  - We operate  in a specific market regime
  - There is a certain probabilistic number of failing companies that are identifiable - including, but not limited to, bankruptcies, defaults, profit warnings, change in competitive environment, lake of demand, supply-chain disruptions, political uncertainties...
  - As a consequence, the failing companies are represented by a sharp decrease in stock price and a surge of volatility
  - The number of failing companies follows a Poisson distribution

The Poisson distribution:

<p align="center">
   <img src="https://numpy.org/doc/stable/_images/math/c91108ae66a9a5e2feb9442c67962868e368fdc8.svg">
</p>

For events with an expected separation ![equation](https://numpy.org/doc/stable/_images/math/cefc603e5658facb747581f9567192993f21c7ab.svg) the Poisson distribution ![equation](https://numpy.org/doc/stable/_images/math/4d00b2dcd7c9300ef7b531ec4b19efbd75cf8ea6.svg) describes the probability of k events occurring within the observed interval ![equation](https://numpy.org/doc/stable/_images/math/cefc603e5658facb747581f9567192993f21c7ab.svg).

### Built With

  - numpy
  - random
  - scipy

## Quick Start

Import necessary modules:

```
from quantico import monte_carlo as mc
```

Run function **.poisson_process**:

``` 
simulations = mc.simulations(
    S0=100,
    rf=0.05,
    sigma=0.20,
    n_iter=100,
    n_simul=100,
    t=1,
    l=2,
    mu_y=0.02,
    var_y=0.25,
    K=100
 )
```

As a result, we get a dictionary with keys as:
  - **'simulation'**: n_simul number of simulations for n_iter iterations
  - **'jumps'**: number of jumps created for each random timeseries

For example:

``` 
for i in range(0, 4): simulations['simulation'][i].plot()
```

<p align="center">
  <img src="https://github.com/ActurialCapital/quantico/blob/master/images/Figure_1.png" width="50%" height="50%">
</p>  

``` 
pd.DataFrame(simulations['simulation']).stack().hist(bins=100)
```

<p align="center">
  <img src="https://github.com/ActurialCapital/quantico/blob/master/images/Figure_2.png" width="50%" height="50%">
</p>

## Author

**Jean Meilhoc Ricaume** - [ActurialCapital](https://github.com/ActurialCapital)

## License

This project is licensed under the MIT License
