# Orchestration

## 3.0 Introduction ML pipelines and Mage

### 3.0.1 ML pipeline

#### What is MLOps

MLOps involves moving ML models from development to production to drive business value
In general, there are 4 steps to make it successful:

1. Preparing the model for deployment involves optimizing performance, ensuring it handles real-world data, and packaging it for integration into existing systems.
2. Deploying the model involves moving it from development to production, making it accessible to users and applications.
3. Once deployed, models must be continuously monitored for accuracy and reliability, and may need retraining on new data and updates to maintain effectiveness.
4. The operationalized model must be integrated into existing workflows, applications, and decision-making processes to drive business impact.

#### Why we need MLOps

1. Productivity: MLOps fosters collaboration between data scientists, ML engineers, and DevOps teams by providing a unified environment for experiment tracking, feature engineering, model management, and deployment. This breaks down silos and accelerates the entire machine learning lifecycle.
2. Reliability: MLOps ensures high-quality, reliable models in production through clean datasets, proper testing, validation, CI/CD practices, monitoring, and governance.
3. Reproducibility: MLOps enables reproducibility and compliance by versioning datasets, code, and models, providing transparency and auditability to ensure adherence to policies and regulations.
4. Time-to-value: MLOps streamlines the ML lifecycle, enabling organizations to successfully deploy more projects to production and derive tangible business value and ROI from AI/ML investments at scale.

#### Pipeline and orchestration definitions

Training/ML pipeline refers to the sequence of steps in order to train a ML model.

Orchestration is essentially organizing, scheduling, and manage a pipeline.

#### Why we need orchestration tools over python scripts

Although we can write a python script to run a simple pipeline, but it's

- Hard to handle complex pipeline
- Hard to be centralized for all team members
- Hard to have essential features: monitor, alert, retry, ...

#### How Mage helps MLOps

1. Data preparation: Mage offers features to build, run, and manage data pipelines for data transformation and integration, including pipeline orchestration, notebook environments, data integrations, and streaming pipelines for real-time data.
2. Training and deployment: Mage helps prepare data, train machine learning models, and deploy them with accessible API endpoints.
3. Standardize complex processes: Mage simplifies MLOps by providing a unified platform for data pipelining, model development, deployment, versioning, CI/CD, and maintenance, allowing developers to focus on model creation while improving efficiency and collaboration.

## 3.1 Data preparation: ETL and feature engineering
## 3.2 Training: sklearn models and XGBoost
- [Global data product](https://docs.mage.ai/orchestration/global-data-products/overview) is useable in any pipeline across the entire project. It helps save time and memory as we don't need to regenerate data everytime, but only when the data is updated or outdated.
- [Dynamic blocks](https://docs.mage.ai/design/blocks/dynamic-blocks) will create multiple downstream blocks at runtime. The number of blocks it creates is equal to the number of items in the output data of the dynamic block multiplied by the number of its downstream blocks.
## 3.3 Observability
## 3.4 Triggering: Inference and retraining
## 3.5 Deploying: Running operations in production

**Read more**: [Note](https://github.com/mleiwe/mlops-zoomcamp/blob/Ch3_ML_Notes/cohorts/2024/03-orchestration/ML_Notes.md#what-is-mlops)
