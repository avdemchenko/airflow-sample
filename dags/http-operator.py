# imports important for Airflow
import pendulum
from airflow.decorators import dag, task
# from airflow.providers.http.operators.http import HttpOperator
from airflow.providers.http.operators.http import SimpleHttpOperator

# Import Modules for code
import json

# import custom transformer for API data
from transformer import transform_weatherAPI

# [START instantiate_dag]
@dag(
    schedule_interval=None,                             # interval how often the dag will run (can be cron expression as string)
    start_date=pendulum.datetime(2021, 1, 1, tz="UTC"), # from what point on the dag will run (will only be scheduled after this date)
    catchup=False,                                      # no catchup needed, because we are running an api that returns now values
    tags=['airflow-sample'],                      # tag the DAQ so it's easy to find in AirflowUI
)

def SimpleHTTPTest():
    """
    ### TaskFlow API Tutorial Documentation
    This is a simple ETL data pipeline example which demonstrates the use of
    the TaskFlow API using three simple tasks for Extract, Transform, and Load.
    Documentation that goes along with the Airflow TaskFlow API tutorial is
    located
    [here](https://airflow.apache.org/docs/apache-airflow/stable/tutorial_taskflow_api.html)
    """

    # EXTRACT: Query the data from the Weather API
    # TODO: Change the API Key to your key!!
    extract_task = SimpleHttpOperator(
        task_id="extract_data",
        http_conn_id='WeatherAPI',
        method="GET",
        endpoint="/v1/current.json",
        data={'Key': 'YOUR_API_KEY', 'q': 'Cairo', 'aqi': 'no'},
        response_filter=lambda response: response.json()
    )

    # TRANSFORM: Transform the API response into something that is useful for the load
    @task()
    def transform(weather_json: json):
        """
        A simple Transform task which takes in the API data and only extracts the location, wind,
        the temperature and time.
        """
        weather_str = json.dumps(weather_json)
        transformed_str = transform_weatherAPI(weather_str)

        # turn string into dictionary
        ex_dict = json.loads(transformed_str)

        # return ex_dict
        return ex_dict

        # LOAD: Just print the data received from the API
    @task()
    def load(ex_dict: dict):

        print(ex_dict)

    # Define the main flow
    weather_data = extract_task.output
    weather_summary = transform(weather_data)
    load(weather_summary)

# Invocate the DAG
lde_weather_dag = SimpleHTTPTest()
