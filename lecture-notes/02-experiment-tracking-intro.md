# Experiment Tracking Introduction

## Important Concepts

- **ML Experiment:** 
  - Not an online A/B test but an offline experiment
  - ML experiment can be thought of as a process of building an ML model
  - The term refers to an entire process of developing an ML model
- **Experiment run:**
  - Each trial of an ML experiment
- **Run aftifact:**
  - Any file that is associated with an ML experiment run
- **Experiment metadata:**
  - All the information related to an ML experiment
- **Experiment tracking:**
  - Process of keeping track of all the **relevant information** from an **ML experiment** (source code, environment, data, model, hyperparameters, metrics, ...). What we define as relevant depends on the task we're working on
- **Machine Learning Lifecycle:**
  - The whole process of building, deploying and maintraining an ML model

## Why is experiment tracking important?

1. Reproducibility of the results
2. Organisation (organised documentation, easy to find to code, readable and understandable code, structured repository, etc.)
3. Optimisation of an ML model

## MLflow

Check the official documentation [here](https://mlflow.org/docs/latest/index.html).

An open source platform for a machine learning lifecycle. It is a Python package that can be installed locally with `pip`. The package contains four main modules:
- **Tracking:** focused on experiment tracking
- **Models:** MLflow models, a special type of models
- **Model Registry:** used to manage models in MLflow
- **Projects:** not covered in the course

## MLflow demo

Some useful MLflow commands:
- `mlflow ui` - launches MLflow UI that allows to view the runs locally (another option would be to run `mlflow server` locally)