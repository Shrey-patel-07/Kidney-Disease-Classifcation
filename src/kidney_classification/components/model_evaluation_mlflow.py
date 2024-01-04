import tensorflow as tf
from urllib.parse import urlparse
import mlflow
import mlflow.keras
from pathlib import Path
from kidney_classification.utils.common import save_json
from kidney_classification.entity.config_entity import EvaluationConfig


class Evaluation:
    def __init__(self, config: EvaluationConfig):
        self.config = config
        self.valid_generator = None  # Initialize to None

    def _valid_generator(self):
        img_height, img_width = self.config.params_image_size[:-1]

        self.valid_generator = tf.keras.utils.image_dataset_from_directory(
            self.config.training_data,
            image_size=(img_height, img_width),
            validation_split=0.30,
            subset="validation",
            seed=123,
        )

        self.valid_generator = self.valid_generator.map(lambda x, y: (x / 255, y))
        AUTOTUNE = tf.data.AUTOTUNE
        self.valid_generator = self.valid_generator.cache().prefetch(
            buffer_size=AUTOTUNE
        )

    @staticmethod
    def load_model(path: Path) -> tf.keras.Model:
        return tf.keras.models.load_model(path)

    def evaluation(self):
        self.model = self.load_model(self.config.path_of_model)
        self._valid_generator()
        self.score = self.model.evaluate(self.valid_generator)
        self.save_score()

    def save_score(self):
        scores = {"loss": self.score[0], "accuracy": self.score[1]}
        save_json(path=Path("scores.json"), data=scores)

    def log_into_mlflow(self):
        mlflow.set_registry_uri(self.config.mlflow_uri)
        tracking_url_type_store = urlparse(mlflow.get_tracking_uri()).scheme

        with mlflow.start_run():
            mlflow.log_params(self.config.all_params)
            mlflow.log_metrics({"loss": self.score[0], "accuracy": self.score[1]})
            # Model registry does not work with file store
            if tracking_url_type_store != "file":
                mlflow.keras.log_model(
                    self.model, "model", registered_model_name="VGG16Model"
                )
            else:
                mlflow.keras.log_model(self.model, "model")
