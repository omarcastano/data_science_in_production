# MLflow

## What is MLflow?

**MLflow** is an open-source platform designed to help manage the **machine learning lifecycle**. It is used to **track experiments**, **package code into reproducible runs**, **share and deploy models**, and **manage model versions**.

### What is MLflow used for?

MLflow is used to make machine learning workflows more **organized**, **reproducible**, and **collaborative**. It helps data scientists and ML engineers keep track of:

- The parameters and metrics of each experiment run.
- The source code and environment used.
- The trained models and their performance.

### How is MLflow used in machine learning?

In a machine learning project, MLflow is typically used to:

1. **Track experiments**: Record parameters, metrics (like accuracy or loss), and results to compare different models or configurations.
2. **Log models**: Save trained models so they can be easily reloaded or shared.
3. **Serve models**: Deploy models as REST APIs for use in applications.
4. **Manage model versions**: Keep track of different versions of a model and promote the best ones to production.

MLflow helps students and professionals build better machine learning workflows by making the process more transparent and reproducible.

To install MLflow, run the following command:

```bash
uv add mlflow
```

To start the MLflow server, run the following command:

```bash
mlflow server --host 127.0.0.1 --port 5000
```

You can access the MLflow UI at `http://127.0.0.1:5000`.

You can check the notebook [mlflow.ipynb](mlflow.ipynb) for more details about logging and tracking experiments.
