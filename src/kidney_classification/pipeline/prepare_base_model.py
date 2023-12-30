from kidney_classification.config.configuration import ConfigurationManager
from kidney_classification.components.prepare_base_model import PrepareBaseModel
from kidney_classification import logger

STAGE_NAME = "Prepare base model"


class PrepareBaseModelTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        prepare_base_model_config = config.get_prepare_base_model_config()
        prepare_base_model = PrepareBaseModel(config=prepare_base_model_config)
        prepare_base_model.get_base_model()
        prepare_base_model.update_base_model()


if __name__ == "__main__":
    try:
        logger.info(f"-------------Running stage: {STAGE_NAME}-------------")
        pipeline = PrepareBaseModelTrainingPipeline()
        pipeline.main()
        logger.info(f"-------------Stage: {STAGE_NAME} completed-------------")
    except Exception as e:
        logger.exception(e)
        raise e
