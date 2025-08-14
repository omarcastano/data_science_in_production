# Apache Airflow

Apache Airflow is an open-source platform for scheduling, organizing, and monitoring workflows — basically, it helps you automate and manage tasks that need to run in a specific order.

In Machine Learning, it’s important because ML projects involve many steps:

- Collecting and cleaning data

- Training models

- Evaluating and deploying models

- Updating models regularly

Airflow lets you connect these steps into a pipeline so they run automatically, in the right sequence, and can be tracked easily. This makes it easier to reproduce results, handle large projects, and keep models up to date without manually running every script.

## Installation

To install Airflow, run the following command:

```bash
uv add apache-airflow
```

When installing Airflow in its default edition, you will see four different components.

- Webserver: Webserver is Airflow’s user interface (UI), which allows you to interact with it without the need for a CLI or an API. From there one can execute, and monitor pipelines, create connections with external systems, inspect their datasets, and many more.

- Executor: Executors are the mechanism by which pipelines run. There are many different types that run pipelines locally, in a single machine, or in a distributed fashion. A few examples are LocalExecutor, SequentialExecutor, CeleryExecutor and KubernetesExecutor

- Scheduler: The scheduler is responsible for executing different tasks at the correct time, re-running pipelines, backfilling data, ensuring tasks completion, etc.

- PostgreSQL: A database where all pipeline metadata is stored. This is typically a Postgres but other SQL databases are supported too.
