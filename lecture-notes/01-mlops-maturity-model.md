# MLOps Maturity Model

Article on [Machine Learning operations maturity model](https://learn.microsoft.com/en-us/azure/architecture/ai-ml/guide/mlops-maturity-model) from Microsoft.

Levels of MLOps automation:

0. No MLOps automation at all:
   1. Jupyter Notebooks, no pipelines, no experiment tracking, no metadata attached to the models
   2. Summary: no automation, all code in sloppy and often messy Jupyter Notebooks
   3. Suitable for the Proof of Concept (POC) stage
1. DevOps but no MLOps
   1. Releases are automated
   2. There are unit tests, integration tests, CI/CD
   3. We monitor certain Ops metrics (e.g., number of requests per second, network situation, etc.)
   4. However, these are general SWE practices and they are not specific the ML models
   5. We are still missing experiment tracking, it is not easy to reproduce the results of an ML model
   6. DS are still separated from Eng
2. Automated Training
   1. Training pipeline
   2. Experiment tracking
   3. Model registry
   4. Deployment may still not be automated but it is low friction to deploy a model
   5. DS work closely with Eng
   6. The company should aim for this stage when there are multiple ML models in the company
3. Automated Deployment
   1. Easy to deploy a ML model, no human is needed to deploy a model
   2. Often this means building an ML platform to which you deploy a trained ML model
   3. The ML platform allows to run A/B tests to select a better performing ML model
   4. Models are monitored as part of the deployment process
4. Full MLOps automation
   1. Automated training and automated deployment all as part of the same pipeline