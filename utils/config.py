import yaml
import os


def load_config():
    config_path = os.path.join(os.path.dirname(__file__), '..', 'config', 'config.yaml')
    with open(config_path, 'r') as file:
        return yaml.safe_load(file)


def get_amazon_credentials():
    config = load_config()
    return config.get("amazon", {})


def get_orangeHrm_credentials():
    config = load_config()
    return config.get("orangeHrm", {})
