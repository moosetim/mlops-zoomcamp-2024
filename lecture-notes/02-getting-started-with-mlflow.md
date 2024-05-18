# Getting Started with MLflow

1. Create a `requirements.txt` file with the following packages: 

        mlflow
        jupyter
        scikit-learn
        pandas
        seaborn
        hyperopt
        xgboost
        fastparquet
        boto3
2. Create an Anaconda virtual environment: `conda create -n exp-tracking-env python=3.9`
3. Activate the created environment: `conda activate exp-tracking-env`; to deactivate the environment, type: `conda deactivate`
4. Install the required packges: `pip install -r requirements.txt`; verify the the packages have been installed: `pip list`
5. Running `mlflow` will give you access to the MLflow UI
6. `mlflow ui --backend-store-uri sqlite:///mlflow.db` - launches MLflow and tells MLflow to store all the artifacts and metadata in SQLite (which is a backend store)

# Steps to do locally

1. Place the Jupyter notebook with the ML model from module 1 into the `02-experiment-tracking` folder
2. Create the `data` folder and place both the training and validation sets there