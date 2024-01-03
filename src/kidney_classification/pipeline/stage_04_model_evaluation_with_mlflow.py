from kidney_classification.config.configuration import ConfigurationManager
from kidney_classification.components.model_evaluation_mlflow import Evaluation
from kidney_classification import logger


STAGE_NAME = "Evaluation Stage"


class EvaluationPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        eval_config = config.get_evaluation_config()
        evaluation = Evaluation(eval_config)
        evaluation.evaluation()
        evaluation.log_into_mlflow()


if __name__ == "__main__":
    try:
        logger.info(f"-------------Running stage: {STAGE_NAME}-------------")
        pipeline = EvaluationPipeline()
        pipeline.main()
        logger.info(f"-------------Stage: {STAGE_NAME} completed-------------")
    except Exception as e:
        logger.exception(e)
        raise e
