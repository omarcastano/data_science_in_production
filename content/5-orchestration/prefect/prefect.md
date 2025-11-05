# Prefect

In order to install prefect, we need to run the following command:

```bash
uv add prefect
```

# Prefect Components

The prefect components that we are going to learn are:

- [Server and UI](#server-and-ui)
- [Workflows](#workflows)
  - [Flows](#flows)
  - [Tasks](#tasks)
- [Deployments](#deployments)
  - [Work Pools](#work-pools)
  - [Workers](#workers)
  - [Schedules](#schedules)
  - [Creating a Deployment from CLI](#creating-a-deployment-from-cli)
  - [Creating a Deployment using Python](#creating-a-deployment-using-python)

## Server and UI

The Prefect Server runs the orchestration backend, handling state tracking, scheduling, API interactions, and metadata. The UI is a graphical interface that lets you monitor, debug, and manage flow runs in real time. It shows dependency graphs, task logs, run status, and enables actions like triggering or canceling runs

In order to start the prefect server, we need to run the following command:

```bash
uv run prefect server start
```

After starting the prefect server, we can access the prefect UI at [http://localhost:4200](http://localhost:4200).

## Workflows

Workflows are structured pipelines consisting of tasks. Prefect allows workflows to be defined using native Python code with decorators. Workflows coordinate task execution logic, dependencies, parameters, error handling, and logging

### Flows

A flow is essentially the Python function decorated to orchestrate a workflow. It defines the sequence of tasks, an example of a flow is the following:

```python
from prefect import flow

@flow
def my_flow():
    print("Hello, World!")
```

### Tasks

Tasks are the individual units of work within a workflow. They perform specific operations, such as data processing, API calls, or file operations. Tasks are defined as functions decorated with `@task`, and they can be executed within a flow. Here's an example of a task:

```python
from prefect import task

@task
def my_task():
    print("Hello, World!")

@flow
def my_flow():
    my_task()
```

Once you workflow has been created, similar to the one shown in [my_first_workflow.py](my_first_workflow.py), you can run it using the following command:

```bash
uv run python my_first_workflow.py
```

## Deployments

A Deployment in Prefect is like a ready-to-use version of your flow, it defines when, where, and how your workflow should run, without needing to manually trigger it each time. Now, before we create a deployment, we need to define two important concepts, worker pool and workers, let's use an analogy to understand them better.

Imagine there’s a class project outline, the flow or workflow, that lays out the series of steps such as research, writing, and presentation (each of those steps being a task, small individual assignments), and this plan is posted on a smart whiteboard (the Work Pool) that not only lists what needs to be done but also tells you where and with which tools to do it (for instance, using the computer lab or art supplies)—then a student (the Worker) reads that board, sees both the assignments and their requirements, moves to the designated location, gathers the proper tools, and then carries out each task in sequence, which mirrors how a Prefect Worker polls the Work Pool (blueprint of infrastructure), provisions the appropriate environment (like Docker, Kubernetes, or cloud), and runs each task in the flow according to the workflow's plan.

Now let's define the work pool and workers more formally.

### Work Pools

A work pool is a group of workers that share the same infrastructure and capabilities. It defines where and how flow runs should execute. Work pools can be configured to use different types of infrastructure, such as Docker, Kubernetes, or cloud platforms.

### Workers

Workers are the agents that actually execute flow runs. They poll assigned work pools, retrieve tasks, run them in matching environments (e.g. Docker, Kubernetes, process, cloud), and report results back to the Prefect Server.

### Schedules

Schedules define when and how often a deployment should run. They can be configured to run on a fixed schedule (e.g. daily, weekly, monthly) or based on specific events (e.g. cron, HTTP requests, file changes).

---

With all this in mind, let's create a deployment for our flow.

### Creating a Deployment from CLI

In order to create a deployment from the CLI, we need to run the following command:

```bash
uv run prefect deploy
```

Once you execute this command, you will have to select the flow you want to deploy, and then you will have to create and select the work pool you want to use.

After selecting the flow and work pool, you will have to start the worker, but first you need to set the `PREFECT_API_URL` environment variable to the URL of your Prefect server.

```bash
export PREFECT_API_URL="http://localhost:4200/api"
```

then, you can start the worker pool using the following command:

```bash
uv run prefect worker start
```

you will be asked to select the work pool you want to use, select the worker you have just created.

After your deploy and worker are ready, you can execute a run of your flow from the UI.

You can schedule your deployment to run at a specific time using the following command:

```bash
uv run prefect deployment schedule create my-flow/my_first_deployment --interval 60
```

Alternatively, you can schedule your deployment to run at a specific time using the UI.

### Creating a Deployment using Python

AN alternative to creating a deployment using the CLI is to create it using Python, specifically you can use the `.serve()` method of the flow to create  the deployment. Here's an example:

```python
from prefect import flow

@flow
def my_flow():
    print("Hello, World!")

my_flow.serve(name="my_first_deployment", interval=60)
```

Now, you can run the script, which will create a scheduled deployment and start the worker pool, using the following command:

```bash
uv run python my_first_workflow.py
```
