import tensorflow as tf
from pathlib import Path
from kidney_classification.entity.config_entity import TrainingConfig


class Training:
    def __init__(self, config: TrainingConfig):
        self.config = config

    def get_base_model(self):
        self.model = tf.keras.models.load_model(self.config.updated_base_model_path)

    def train_valid_generator(self):
        img_height, img_width = self.config.params_image_size[:-1]

        train = tf.keras.utils.image_dataset_from_directory(
            self.config.training_data,
            image_size=(img_height, img_width),
            validation_split=0.1,
            subset="training",
            seed=123,
        )

        val = tf.keras.utils.image_dataset_from_directory(
            self.config.training_data,
            image_size=(img_height, img_width),
            validation_split=0.2,
            subset="validation",
            seed=123,
        )
        train = train.map(lambda x, y: (x / 255, y))
        val = val.map(lambda x, y: (x / 255, y))
        AUTOTUNE = tf.data.AUTOTUNE

        self.train_dataset = train.cache().prefetch(buffer_size=AUTOTUNE)
        self.val_dataset = val.cache().prefetch(buffer_size=AUTOTUNE)

    @staticmethod
    def save_model(path: Path, model: tf.keras.Model):
        model.save(path)

    def define_and_train_model(self):
        self.model.fit(
            self.train_dataset,
            validation_data=self.val_dataset,
            epochs=self.config.params_epochs,
        )

        self.save_model(path=self.config.trained_model_path, model=self.model)
