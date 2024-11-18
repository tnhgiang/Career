# Monitoring

## 1. Overview

Our ML production models are production software and thus face the same problems faced by other production SE/SD software. However, in addition to these general issues, certain ML-specific issues may occur in ML production models that don't in SE/SD. As such, SE/SD tools are not sufficient to monitor ML production models.

Monitoring models is mostly around 4 main aspects:

- Service health
- Model performance
- Data Quality and Integrity: Checking data's overall completeness, correctness, consistency, ...
- Data Drift and Concept Drift: Checking data and its distribution as data always changes over time.

### 1.1 Service health

Check whether the model is actually working or not, it's just like general software health checks. Example metrics:

- Uptime
- Memory usage
- Latency

### 1.2 Model performance

How good of the model based on set of metrics depending on problem statement. Example:

- RMSE for regression
- Precision, recall and F1 score for classification

Typically, evaluation would be based on batch data that comes later as we will not have ground truth data coming in.

### 1.3 Data quality and integrity

Data integrity ensures the data’s overall completeness, correctness, consistency, accessibility, and security

Data quality measures the level of data integrity

### 1.4 Data and concept drift

Over time, ML models may degrade. This is due to one of two effects:

- Data drift refers to changes in the distribution of the input features an ML model receives in production.
- Concept drift is a change in input-output relationships.

### 1.5 Some others aspects to check:

- Performance by segment: E.g. split out your metrics by class/category so you have higher granularity.
- Model bias/fairness
- Outliers: If the cost of an individual error is high, outliers may need to be considered separately.
- Explainability

## 2. Batch vs Online Serving models

### 2.1 Batch

Batch is based on training data or past batch. For example you can measure things such as:

- Expected data quality
- Data distribution type
- Descriptive statistics
- Point estimations
- Stat tests to measure CI

### 2.2 Non-batch

This would be frameworks such as streaming, where you have a continuous data stream. One option is to window, i.e. sample from a moving time window and compare changes between time windows


**Read more:**
- [Why we need monitoring](https://evidentlyai.com/blog/ml-monitoring-metrics)
