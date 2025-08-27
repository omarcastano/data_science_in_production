# Streamlit

Streamlit is an open-source Python framework designed to turn your data science and machine learning models into interactive web applications quickly and easily. It’s especially useful for building user-friendly interfaces without needing any front-end development experience.

Think of Streamlit as a tool that allows anyone to interact with your machine learning model through buttons, sliders, inputs, and visualizations — all using pure Python.

## Key Features of Streamlit

- Rapid development with only a few lines of code.
- Automatically generates a clean and modern web interface.
- Built specifically for data science workflows.
- Automatically updates when the code changes.

## Why Use Streamlit for Machine Learning?

Machine learning models are often used in notebooks or scripts — environments that are not accessible to non-programmers. With Streamlit, you can:

1. Create an easy-to-use interface for your model.
2. Allow users to input data through interactive elements.
3. Visualize model predictions and outputs instantly.

Streamlit is ideal for turning your model into a usable tool, demo, or dashboard.

## Streamlit vs FastAPI: What’s the Difference?

Both Streamlit and FastAPI are used for deploying machine learning models, but they serve different purposes.

| Feature                  | Streamlit                                 | FastAPI                                         |
|--------------------------|--------------------------------------------|--------------------------------------------------|
| Purpose                  | Build interactive data apps and dashboards | Build APIs and backend services                  |
| Target Users             | End users, data scientists, analysts        | Developers, system integrators                   |
| Interface Type           | Visual user interface                      | API endpoints (JSON in/out)                      |
| Interactivity            | Direct, through UI elements                | Indirect, through HTTP requests                  |
| Typical Use Case         | Prototypes, dashboards, demos              | Production-ready services and integrations       |
| Frontend Code Needed     | None                                        | Yes, if a user interface is required             |
| Real-Time Responses      | Yes, through UI updates                    | Yes, through API responses                       |

### Which One Should You Use?

- Use **Streamlit** if you want to quickly build a demo or internal tool where people interact directly with the model.
- Use **FastAPI** if you need to serve your model as a service, especially when other systems or apps need to call it.

You can also combine both:

- Use FastAPI to handle the backend logic.
- Use Streamlit to provide a simple frontend for internal users or demonstrations.

## Installing Streamlit

To install Streamlit using uv:

```bash
uv add streamlit
```

## Running a Streamlit App

To launch the Streamlit application streamlit_aplication.py, run:

```bash
uv run streamlit run src/app/deployment/streamlit_aplication.py
```

This will open the app in your web browser.
