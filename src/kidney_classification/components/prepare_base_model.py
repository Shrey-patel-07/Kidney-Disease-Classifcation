import tensorflow as tf
from pathlib import Path
from kidney_classification.entity.config_entity import PrepareBaseModelConfig
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Flatten, BatchNormalization, Dropout


class PrepareBaseModel:
    @staticmethod
    def prepare_full_model():
        VGG_model = Sequential()

        pretrained_model = tf.keras.applications.VGG16(
            include_top=False,
            input_shape=(150, 150, 3),
            pooling="max",
            classes=4,
            weights="imagenet",
        )

        VGG_model.add(pretrained_model)
        VGG_model.add(Flatten())
        VGG_model.add(Dense(512, activation="relu"))
        VGG_model.add(BatchNormalization())
        VGG_model.add(Dropout(0.5))

        VGG_model.add(Dense(4, activation="softmax"))
        pretrained_model.trainable = False

        VGG_model.compile(
            optimizer="adam",
            loss="sparse_categorical_crossentropy",
            metrics=["accuracy"],
        )

        return VGG_model

    def update_base_model(self, config: PrepareBaseModelConfig):
        full_model = self.prepare_full_model()

        full_model.summary()
        full_model.save(config.updated_base_model_path)

    @staticmethod
    def save_model(path: Path, model: tf.keras.Model):
        model.save(path)
