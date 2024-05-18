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
2. Create the `data` folder and place both the training and validation sets there. Download the following datasets: `green_tripdata_2021-01.csv` and `green_tripdata_2021-02.csv` (in the 2024 edition of the MLOps Zoomcamp `.parquet` files are used instead of `.csv` files)
3. Create the `models` folder. The created ML models will be stored there
4. MLflow-related commands to set up a new experiment:

# Let us now start using MLflow to track our experiments

        with mlflow.start_run():

        # Start logging the information about this run with MLflow
        mlflow.set_tag("developer", "Timur Musin")

        mlflow.log_param("train-data-path", "./data/green_tripdata_2021-01.parquet")
        mlflow.log_param("valid-data-path", "./data/green_tripdata_2021-02.parquet")

        alpha = 0.01
        mlflow.log_param("alpha", alpha)

        # Fit the Lasso Linear Regression model
        lr = Lasso(0.01)
        lr.fit(X_train, y_train)

        # Create predictions on the validation set
        y_pred = lr.predict(X_val)
        rmse = root_mean_squared_error(y_val, y_pred)
        mlflow.log_metric("rmse", rmse)