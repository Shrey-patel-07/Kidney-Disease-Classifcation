from kidney_classification.pipeline.data_pipeline import DataIngestionTrainingPipeline
from kidney_classification import logger
import sys

sys.path.append("./src")

STAGE_NAME = "Data Ingestion"

try:
    logger.info(f"-------------Running stage: {STAGE_NAME}-------------")
    pipeline = DataIngestionTrainingPipeline()
    pipeline.main()
    logger.info(f"-------------Stage: {STAGE_NAME} completed-------------")
except Exception as e:
    logger.exception(e)
    raise e
