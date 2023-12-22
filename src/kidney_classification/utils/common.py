import json
import yaml
import base64
import joblib
from typing import Any
from pathlib import Path
from box import ConfigBox
from ensure import ensure_annotations
from box.exceptions import BoxValueError
from kidney_classification import logger


@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """read yaml file and return a ConfigBox object

    Args:
        path_to_yaml (Path): path like input

    Raises:
        ValueError: if yaml file is empty
        e: empty file

    Returns:
        ConfigBox: ConfigBox object
    """
    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"yaml file: {path_to_yaml} loaded successfully")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError(f"Yaml file {path_to_yaml} is empty")
    except Exception as e:
        raise e


@ensure_annotations
def save_json(path: Path, data: dict):
    """save the data in json format

    Args:
        path (Path): path to json file
        data (dict): data to be saved
    """
    with open(path, 'w') as f:
        json.dump(data, f, indent=4)
    logger.info(f"json file: {path} saved successfully")


@ensure_annotations
def save_bin(data: Any, path: Path):
    """save binary data

    Args:
        data (Any): data to be saved
        path (Path): path to bin file
    """
    joblib.dump(value=data, filename=path)
    logger.info(f"bin file: {path} saved successfully")


@ensure_annotations
def load_bin(path: Path) -> Any:
    """load binary data

    Args:
        path (Path): path to bin file

    Returns:
        Any: data
    """
    data = joblib.load(filename=path)
    logger.info(f"bin file: {path} loaded successfully")
    return data


def decodeImage(imagestring, fileName):
    imagedata = base64.b64decode(imagestring)
    with open(fileName, 'wb') as f:
        f.write(imagedata)
        f.close()


def encodeImage(imagePath):
    with open(imagePath, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
        return encoded_string
