import sys

sys.path.append("./src")
from kidney_classification.pipeline.data_pipeline import DataIngestionTrainingPipeline
from kidney_classification import logger
from kidney_classification.pipeline.prepare_base_model import (
    PrepareBaseModelTrainingPipeline,
)


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
