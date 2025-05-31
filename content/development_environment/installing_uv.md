# Installing UV

UV is a new tool that helps you manage Python projects, and it’s made to be very fast. When you build something with Python, you often need to add extra tools or libraries (for example, if you want to use math tools like numpy or make graphs with matplotlib). Normally, you use tools like pip or venv to install and organize those libraries. UV does the same thing, but much faster and more efficiently.

To install UV, you can execute the following command in the terminal:

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

Now you can install a specific Python version using UV with the following command:

```bash
uv python install 3.12
```

To manage the dependencies of a specific project, you need to create a `.toml` file where you specify the project name, version, description, and—very importantly—the required Python version for the project.

```toml
[project]
name = "data_science_in_production"
version = "0.1.0"
description = "Project to learn data science in production"
readme = "README.md"
requires-python = ">=3.11, <3.13"
dependencies = []
```

To add Python packages to the project, you can use the following command:

```bash
uv add package-name
```

For example, to add `pandas` as a dependency of the project, you can run:

```bash
uv add pandas
```