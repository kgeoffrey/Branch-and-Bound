![Kiku](Images/spongegar.png)

# cavemanstatistics 1.0

This package contains unnecessarily slow, brute-force search methods for finding highest R^2 of (with specified or unspecified dependant variable) Linear Regression Models. It is mainly a personal project for getting to know packaging with pypi.org and developing my workflow. In the future I'd like to vectorize the loops and maybe add more search options and better search methods.

### Dependancies

* NumPy
* Pandas
* SciPy
* scikit-learn
* Tabulate

### Installing

Install with:

```
pip install cavemanstatistics
```

## Quick documentation

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

After installation, import:

```python
from cavemanstatistics import ExhaustiveSearch, BruteForce
```


#### Search for highest R^2 (unspecified dependant variable):

```python
model, results = ExhaustiveSearch(data = pd.dataframe, remove = list, lowerbound = int, upperbound = int, adjusted_R2 = bool).solve()
y, x = model
print(model)

('depedant variable', [list of explanatory variables])

```

ExhaustiveSearch().solve() returns a touple containing a string (dependant variable) and a list (explanatory variables) and a sorted dictionary with all results.

Parameters:
* data:  has to be a pandas dataframe
* remove: place list of variable names that you would like to exclude as depedant variables (or place an empty list)
* lowerbound: smallest integer number of explanatory variables in solution set
* upperbound: largest integer number of exoplanatory variables in solution set
* adjusted_R2: True for adjusted R^2, false for R^2


#### Search for highest R^2 (specified dependant variable):

```python
model, results = BruteForce(data = pd.dataframe, Y = str, lowerbound = int, upperbound = int, adjusted_R2 = bool).solve()
y, x = model
print(model)

('depedant variable', [list of explanatory variables])

```

BruteForce().solve() returns a touple containing a string (dependant) and a list (explanatory variables) and a sorted dictionary with all results.

Parameters:
* data:  has to be a pandas dataframe
* Y: the name of the variable that you would like to specify as dependant variable
* lowerbound: smallest integer number of explanatory variables in solution set
* upperbound: largest integer number of exoplanatory variables in solution set
* adjusted_R2: True for adjusted R^2, false for R^2


## Authors

* **Geoffrey Kasenbacher** - [kgeoffrey](https://github.com/kgeoffrey)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* This is a spawn of the frustration caused by the R-Package 'leaps'
* Tip fedora to the ascii art creators
