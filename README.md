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
* [Getting Started](#getting-started)
* [Contributing](#contributing)
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
   <img src="https://docs.scipy.org/doc/numpy/_images/math/5530e3b933171293a6e472ceb20c8b6e13907694.svg">
</p>

For events with an expected separation ![equation](https://docs.scipy.org/doc/numpy/_images/math/76f1d8ace30435987c01a00ca53a71cba1f40e6c.svg) the Poisson distribution ![equation](https://docs.scipy.org/doc/numpy/_images/math/4543967a0487e3e38e5d9af75c03d0c481a740c4.svg) describes the probability of k events occurring within the observed interval ![equation](https://docs.scipy.org/doc/numpy/_images/math/76f1d8ace30435987c01a00ca53a71cba1f40e6c.svg).

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
simulations = mc.poisson_process(
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

## Getting Started

The easiest way to install quantico is using **pip** package management system. To install quantico, enter the following command at a Bash or Windows command prompt:

```
pip install quantico
```

## Contributing

Please read [CONTRIBUTING.md](https://gist.github.com/PurpleBooth/b24679402957c63ec426) for details on our code of conduct, and the process for submitting pull requests to us.

## Author

* **Jean Meilhoc Ricaume** - [ActurialCapital](https://github.com/ActurialCapital)

## License

This project is licensed under the MIT License
