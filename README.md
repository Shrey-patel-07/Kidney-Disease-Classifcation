# Kidney Tumor, Cyst, or Stone Classification
![alt text](https://github.com/Shrey-patel-07/Kidney-Disease-Classifcation/blob/b19262be45c45d9e375e2119d89462ccfc7475c1/templates/kidney_ctscan.png)

## Project Overview
The main goal of this project is to develop a reliable and efficient deep-learning model that can accurately classify kidney tumors and Stone from medical images.

## Introduction
Kidney Disease Classification is a project utilizing deep learning techniques to classify Kidney Tumor and Stone diseases from [medical images dataset](https://www.kaggle.com/datasets/nazmul0087/ct-kidney-dataset-normal-cyst-tumor-and-stone/). This project leverages the power of Deep Learning, Machine Learning Operations (MLOps) practices, Data Version Control (DVC). It integrates with DagsHub for collaboration and versioning.

## Dagshub Project Pipeline
![alt text](https://github.com/Shrey-patel-07/Kidney-Disease-Classifcation/blob/2ad0c02af659c2c1e82798524897d831349b1071/templates/dagshub-kidney_disease_classification.png)

## Mlflow Stats
![alt text](https://github.com/Shrey-patel-07/Kidney-Disease-Classifcation/blob/2ad0c02af659c2c1e82798524897d831349b1071/templates/mlflow-kidney_disease_classification.png)

## Importance of the Project
- **Enhancing Healthcare**: By providing accurate and quick disease classification, this project aims to improve patient care and diagnostic accuracy significantly.
- **Research and Development**: It serves as a tool for researchers to analyze medical images more effectively, paving the way for discoveries in the medical field.
- **Educational Value**: This project can be a learning platform for students and professionals interested in deep learning and medical image analysis.

## Technical Overview
- **Deep Learning Frameworks**: Utilizes popular frameworks like TensorFlow or PyTorch for building and training the classification models.
- **Data Version Control (DVC)**: Manages and versions large datasets and machine learning models, ensuring reproducibility and streamlined data pipelines.
- **Git Integration**: For source code management and version control, making the project easily maintainable and scalable.
- **MLOps Practices**: Incorporates best practices in machine learning operations to automate workflows, from data preparation to model deployment.
- **DagsHub Integration**: Facilitates collaboration, data and model versioning, experiment tracking, and more in a user-friendly platform.

## How to run?
### STEPS:

Clone the repository

```bash
https://github.com/krishnaik06/Kidney-Disease-Classification-Deep-Learning-Project
```
### STEP 01- Create a conda environment after opening the repository

```bash
conda create -n venv python=3.11 -y
```

```bash
conda activate venv
```


### STEP 02- install the requirements
```bash
pip install -r requirements.txt
```

```bash
# Finally run the following command
python app.py
```

Now,
```bash
open up your local host and port
```

## To Run the Pipeline
```bash
dvc repro
```
---

This project is still in development, and we welcome contributions of all kinds: from model development and data processing to documentation and bug fixes.

**Join me in this exciting journey to revolutionize the field of medical image classification with AI!**
