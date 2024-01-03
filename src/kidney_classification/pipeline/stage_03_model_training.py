from kidney_classification.config.configuration import ConfigurationManager
from kidney_classification.components.model_training import Training
from kidney_classification import logger

STAGE_NAME = "Training Model"


class ModelTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        training_config = config.get_training_config()
        training = Training(config=training_config)
        training.get_base_model()
        training.train_valid_generator()
        training.define_and_train_model()


if __name__ == "__main__":
    try:
        logger.info(f"-------------Running stage: {STAGE_NAME}-------------")
        pipeline = ModelTrainingPipeline()
        pipeline.main()
        logger.info(f"-------------Stage: {STAGE_NAME} completed-------------")
    except Exception as e:
        logger.exception(e)
        raise e
