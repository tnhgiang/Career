# Deployment

## 1. Overview
There are 3 steps in Machine Learning project
- Design
- Model
- Operate: Now, it's time to deploy model

There are 3 ways to deploy a model:
- Batch deployment (Offline deployment): The model is not up and running all the time, and only runs regularly.
- Online deployment: The model is always available, and makes prediction as soon as possible.
    - Web service: The model is available at a web address, and we must send a HTTP request to get back the prediction.
    - Streaming: The model is constantly listening for events on the stream and processes it. A streaming system consists of producer and consumer.

## 4.2 Deployment as a web service with Flask and Docker
## 4.3 Web-service: Getting the models from the model registry
**Note**
Currently the code is dependent on being able to access the tracking server. However there could be issues with the server and it may go down for any number of reasons (e.g. Heavy Traffic). Therefore we may want to be able to use our model independently of the server.
```python
logged_model = f's3://mlflow-models-alexey/1/{RUN_ID}/artifacts/model'
```
We can export the `RUN_ID` in the environment variable.

**Read more**:
- [Note](https://github.com/mleiwe/mlops-zoomcamp/blob/NotesBranch/cohorts/2024/04-deployment/Ch4_Notes_ML.md)
- [Note](https://github.com/ayoub-berdeddouch/mlops-journey/blob/main/deployment-04.md)
