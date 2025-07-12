# Airflow Sample Repository

This repository contains sample Apache Airflow DAGs to demonstrate various workflow scenarios. It serves as a starting point for understanding how to structure and run workflows using Airflow. Apache Airflow is a platform to programmatically author, schedule, and monitor workflows, and this repository provides practical examples to help users get familiar with its core concepts.

## Prerequisites

Before you begin, ensure you have the following installed:

- Python 3.7 or higher
- Docker and Docker Compose (for containerized setup)
- Access to a PostgreSQL database (if using CeleryExecutor)

## Setup Instructions

You can set up and run the Airflow environment using either a local Python setup or Docker Compose. Choose the option that best suits your needs.

### Docker Compose

1. **Clone the repository**:
   ```bash
   git clone https://github.com/avdemchenko/airflow-sample.git
   cd airflow-sample
   ```

2. **Build and start the containers**:
   ```bash
   docker-compose up --build
   ```

3. **Access the Airflow UI** at `http://localhost:8080`

## Running the Workflows

- The DAGs are located in the `dags/` directory.
- To trigger a DAG, navigate to the Airflow UI, locate the DAG, and click the "Trigger DAG" button.
- Monitor the workflow progress and logs directly through the Airflow UI.

## Examples and Use Cases

The repository includes several DAGs that showcase different Airflow features:

- **`example_dag.py`**: Demonstrates a simple workflow with sequential tasks.
- **`parallel_tasks_dag.py`**: Shows how to run tasks in parallel.
- **`dynamic_tasks_dag.py`**: Illustrates dynamic task generation based on input parameters.

These examples are designed to help users understand core Airflow concepts such as task dependencies, parallelism, and dynamic workflows.

## Custom Operators

- **`MyCustomOperator`**: A custom operator that extends Airflow's functionality. For more details, refer to `plugins/my_custom_operator.py`.

Custom operators like this one demonstrate how Airflow can be extended to meet specific use cases, providing flexibility beyond the built-in operators.

## Troubleshooting

- **Database connection issues**: Ensure that the database is running and that the connection string is correctly configured in `airflow.cfg`.
- **Docker-related issues**: Check the container logs using `docker-compose logs` to diagnose any problems.

## Contributing

Feel free to modify the existing DAGs or add new ones to enhance the repository. Pull requests are welcome, and contributions that improve the examples or add new use cases are especially appreciated.
