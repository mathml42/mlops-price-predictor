
# mlops-price-predictor

## Ames Housing ML Pipeline

A modular, orchestrated machine learning pipeline for the Ames Housing dataset, featuring robust EDA, advanced data processing, and a modern MLOps workflow powered by **ZenML** and **MLflow**.

## Table of Contents

- [Project Overview](#project-overview)
- [MLOps Stack](#mlops-stack)
- [Directory Structure](#directory-structure)
- [Getting Started](#getting-started)
- [Project Workflow](#project-workflow)
- [Design Patterns](#design-patterns)
- [Contributing](#contributing)
- [License](#license)

## Project Overview

This repository demonstrates an end-to-end machine learning workflow on the Ames Housing dataset, leveraging ZenML for pipeline orchestration and MLflow for experiment tracking and model deployment. The modular architecture ensures clean, reproducible, and scalable data science projects.

## MLOps Stack

- **ZenML**: Used for defining, running, and managing modular ML pipelines, enabling reproducible workflow steps and pluggable components.
- **MLflow**: Integrated as an experiment tracker (logging metrics, parameters, and artifacts) and for managing and deploying trained models.


## Directory Structure

```
├── analysis/ # EDA notebooks and scripts
├── data/ # Raw data archives
├── designs/ # Design pattern samples (factory, strategy, template)
├── extracted_data/ # Processed datasets
├── pipelines/ # ZenML pipeline scripts for training & deployment
├── requirements.txt # Python dependencies, including ZenML/MLflow
├── run_deployment.py # Entrypoint to deploy model (via ZenML + MLflow)
├── run_pipeline.py # Entrypoint to run full ZenML pipeline
├── source/ # Core data science modules
└── steps/ # ZenML pipeline steps (data ingestion, splitting, etc.)
```

text

## Getting Started

### Prerequisites

- Python 3.10+
- All required packages listed in `requirements.txt`

pip install -r requirements.txt
pip install zenml mlflow

### Installation

```sh
pip install -r requirements.txt
```

If ZenML or MLflow are not installed, you may also need:

```sh
pip install zenml mlflow
```


### ZenML Initialization

If this is your first time running the project, initialize ZenML:

```sh
zenml init
```


### Usage

- **Run Training Pipeline:**
  ```sh
  python run_pipeline.py
  ```

- **Deploy Trained Model:**
  ```sh
  python run_deployment.py
  ```

- **Inspect Runs & Manage Models (MLflow UI):**
  ```sh
  mlflow ui
  ```

- **Explore Data Analysis:**
  Open `analysis/EDA.ipynb` in a Jupyter environment.

## Project Workflow

1. **Data Ingestion** (ZenML step)
2. **EDA** (Jupyter & scripts)
3. **Feature Engineering** (ZenML step)
4. **Missing Values & Outlier Handling** (ZenML step)
5. **Data Splitting** (ZenML step)
6. **Model Building & Training** (ZenML step, MLflow logs)
7. **Evaluation** (ZenML step, MLflow logs)
8. **Deployment** (ZenML step, MLflow serves models)


All core ETL/ML logic is implemented modularly. ZenML pipelines orchestrate the stepwise workflow, while MLflow tracks experiments and manages deployments seamlessly.

## Design Patterns


The `designs/` directory demonstrates:
- Factory Pattern
- Strategy Pattern
- Template Pattern

These patterns help enforce clean, extensible code architecture.

## Contributing

Contributions are welcome! Please open issues or submit pull requests with improvements, new features, or bug fixes.


## License

Specify your license here (e.g., MIT, Apache 2.0).


---

*For questions or further documentation requests, feel free to reach out or open an issue.*