Please follow the steps below to ensure a smooth installation and execution of the Python project.

## Prerequisites

Before you begin, ensure you have the following installed on your system:

Python
Pip

## Python Installation

In order to install Python, run the command below in terminal:

````
# Python Installtion
Python engine should be already installed in Ubuntu but with the following command it can be check by running `python3` command in terminal. Next is to install `pip` and all Python requirements.

## Install Pip
To install the `pip` in Ubuntu run the following command in the terminal:
```shell
sudo apt update
sudo apt install python3-pip
````

## Install Python Requirements

To install the Python requirements for your project, navigate to the root folder and run the following command in the terminal:

```shell
pip install -r requirements.txt
```

## Start Server

To start the server for your application, use the following command:

```shell
uvicorn app:app --host localhost --port 8000

nodemon --exec python3 app.py
```

## Run Tests

To run the tests for your application, execute the following command:

```shell
pytest
```

## Check Linting Issues

To check for linting issues in your code, run:

```shell
black .
```

## Format the Code

To format your code, run:

```shell
flake8 .
```