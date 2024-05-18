# Experiment Tracking with MLflow

Example that will be explored: 
- How to add hyperparameter tuning to the Jupyter Notebook
- How to explore the results of the hyperparameter search in MLflow UI
- How to select the best model
- How to use Autolog
  - Autolog - MLflow feature that allows to use logging but with fewer lines of code

# Train and Optimise an xgboost model with MLflow

The imported packages: 
- `from hyperopt import fmin, tpe, hp, STATUS_OK, Trials`
- `from hyperopt.pyll import scope`
  - `hyperopt` - package that uses Bayesion methods to find the best set of hyperparameters
  - `fmin` - method that is used to minimise an objective function
  - `tpe` - algorithm that is used for optimisation
  - `hp` - library that contains different methods to define the search space, it allows to specify the ranges for each of the used hyperparameter
  - `STATUS_OK` - signal that we will be sending at the end of each experiment run to notify hyperopt that the optimisation has finished
  - `Trials` - it will keep the information from each run

Once you've run the optimisation of a model, you can compare all of the experiment runs and obtained metrics that different combinations of hyperparameters led to. To do that:
- Filter the experiment runs with a model tag by typing: `tags.model = 'xgboost'`