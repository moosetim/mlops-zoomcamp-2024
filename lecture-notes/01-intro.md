# Module 1. Introduction

**MLOps** - a set of best practices for putting ML models into production. 

Problem we are going to work on in the course - predicting the duration of a taxi drive (how many minutes a taxi drive from A to B take).

3 stages of an ML project:
1. Design
   1. Is ML the right tool for solving our problem?
2. Train
   1. Think of a set of appropriate ML models
   2. Train the model and find the best ML model via experimentation
3. Operate
   1. Deploy the model. We have found a model. We deploy the model to a web-service. A customer can communicate with the model via an API, i.e. the customer will tell the model the pick-up and drop-off locations, the API will return the approximate duration of the trip.
   2. Once deployed, we need to monitor the performance of the model.

# Good MLOps practices and cons of using Jupyter notebooks

1. Cons of Jupyter notebooks: 
   1. Often the execution order in a notebook is not linear - such an approach allows a DS to be flexible and experiment with a model but it also leads to a messy notebook that might be hard to follow
2. MLOps best practice 1: When testing different parameters of ML models (e.g., when testing the `alpha` values of a Lasso regression), log the performance results of the fitted model into an `experiment tracker` for future reference and comparison
3. MLOps best practice 2: Once a ML model has been fitted, save the model specification into the `model registry` (`model registy` and `expriment tracker` go together - you will keep track of the fitted models and you'll know what each model's performance was)
4. MLOps best practice 3: Once you've got a Jupyter Notebook with a fitted ML model, you can use a ML pipeline to decompose the notebook into a series of consecutive steps. The steps can be:
   1. Load and prepare the data
   2. Vectorise (train the dictionary vectoriser and turn the dataframe into a feature matrix)
   3. Train a model

Notice that you can parametrise the pipeline. E.g., there can be different parameters for the `train_data` and `validation_data` periods, `model specification`. Once we have a parametrised pipeline, we can run: `python pipeline.py --train_data=... --validation_data=... --model=...`. Tools like `Prefect` and `Kubeflow` will help us create such pipelines.

The output of a ML pipeline is a model. We then put this trained ML model into a web-service. 

Once the model has been deployed, we need to make sure it's performing well. So we need monitoring. If there is a drop in the model's performance, our monitoring system should send an alert.