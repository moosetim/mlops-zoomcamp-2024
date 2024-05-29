import os
import pickle
import click
import mlflow

from mlflow.entities import ViewType
from mlflow.tracking import MlflowClient
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import root_mean_squared_error

HPO_EXPERIMENT_NAME = "random-forest-hyperopt"
EXPERIMENT_NAME = "random-forest-best-models"
RF_PARAMS = ['max_depth', 'n_estimators', 'min_samples_split', 'min_samples_leaf', 'random_state']

mlflow.set_tracking_uri("sqlite:///mlflow.db") # http://127.0.0.1:5000
mlflow.set_experiment(EXPERIMENT_NAME)
mlflow.sklearn.autolog()


def load_pickle(filename):
    with open(filename, "rb") as f_in:
        return pickle.load(f_in)


def train_and_log_model(data_path, params):
    X_train, y_train = load_pickle(os.path.join(data_path, "train.pkl"))
    X_val, y_val = load_pickle(os.path.join(data_path, "val.pkl"))
    X_test, y_test = load_pickle(os.path.join(data_path, "test.pkl"))

    print('\nStarting MLflow run')
    with mlflow.start_run():
        new_params = {}
        for param in RF_PARAMS:
            new_params[param] = int(params[param])
            print(param, new_params[param])

        rf = RandomForestRegressor(**new_params)
        rf.fit(X_train, y_train)

        # Evaluate model on the validation and test sets
        val_rmse = root_mean_squared_error(y_val, rf.predict(X_val))
        print('Validation RMSE:', val_rmse)
        mlflow.log_metric("val_rmse", val_rmse)
        print('Validation RMSE logged')

        test_rmse = root_mean_squared_error(y_test, rf.predict(X_test))
        print('Test RMSE:', test_rmse)
        mlflow.log_metric("test_rmse", test_rmse)
        print('Test RMSE logged\n')
    print('Finished MLflow run\n')


@click.command()
@click.option(
    "--data_path",
    default="./output",
    help="Location where the processed NYC taxi trip data was saved"
)
@click.option(
    "--top_n",
    default=5,
    type=int,
    help="Number of top models that need to be evaluated to decide which one to promote"
)
def run_register_model(data_path: str, top_n: int):

    client = MlflowClient()

    # Retrieve the top_n model runs and log the models
    experiment = client.get_experiment_by_name(HPO_EXPERIMENT_NAME)
    runs = client.search_runs(
        experiment_ids=experiment.experiment_id,
        run_view_type=ViewType.ACTIVE_ONLY,
        max_results=top_n,
        order_by=["metrics.test_rmse ASC"]
    )

    print('\nStarted training the best model\n')
    for run in runs:
        train_and_log_model(data_path=data_path, params=run.data.params)
    print('Finished training the best model')

    # Select the model with the lowest test RMSE
    experiment = client.get_experiment_by_name(EXPERIMENT_NAME)
    best_run = client.search_runs(
        experiment_ids=experiment.experiment_id,
        run_view_type=ViewType.ACTIVE_ONLY,
        max_results=1, 
        order_by=["metrics.test_rmse ASC"] 
    )

    # Print the information about the best run
    print("Best run:")
    # print(best_run)
    print("run uuid: {0}, rmse: {1:.4f}".format(best_run[0].info.run_uuid, best_run[0].data.metrics["test_rmse"]))

    # Register the best model
    run_uuid = best_run[0].info.run_uuid
    model_uri = "runs:/{0}/model".format(run_uuid)

    print("run uuid: {0}".format(run_uuid))
    print("model uri: {0}".format(model_uri))

    print('\nRegistering the best model\n')
    mlflow.register_model(model_uri=model_uri, name=EXPERIMENT_NAME)
    print('Finished registering the best model\n')


if __name__ == '__main__':
    run_register_model()