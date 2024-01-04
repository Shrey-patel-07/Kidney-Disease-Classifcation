import sys

sys.path.append("./src")
from kidney_classification.pipeline.stage_04_model_evaluation_with_mlflow import (
    EvaluationPipeline,
)
from kidney_classification.pipeline.stage_03_model_training import ModelTrainingPipeline
from kidney_classification.pipeline.stage_02_prepare_base_model import (
    PrepareBaseModelTrainingPipeline,
)
from kidney_classification.pipeline.stage_01_data_ingestion import (
    DataIngestionTrainingPipeline,
)
from kidney_classification import logger


STAGE_NAME = "Data Ingestion"

try:
    logger.info(f"-------------Running stage: {STAGE_NAME}-------------")
    pipeline = DataIngestionTrainingPipeline()
    pipeline.main()
    logger.info(f"-------------Stage: {STAGE_NAME} completed-------------")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "Prepare base model"

try:
    logger.info(f"-------------Running stage: {STAGE_NAME}-------------")
    pipeline = PrepareBaseModelTrainingPipeline()
    pipeline.main()
    logger.info(f"-------------Stage: {STAGE_NAME} completed-------------")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "Training Model"

try:
    logger.info(f"-------------Running stage: {STAGE_NAME}-------------")
    pipeline = ModelTrainingPipeline()
    pipeline.main()
    logger.info(f"-------------Stage: {STAGE_NAME} completed-------------")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "Evaluation Stage"

try:
    logger.info(f"-------------Running stage: {STAGE_NAME}-------------")
    pipeline = EvaluationPipeline()
    pipeline.main()
    logger.info(f"-------------Stage: {STAGE_NAME} completed-------------")
except Exception as e:
    logger.exception(e)
    raise e
