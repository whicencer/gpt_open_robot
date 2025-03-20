import yaml
from pathlib import Path


class Config:
  def __init__(self):
    config_dir = Path(__file__).parent.parent.resolve() / "config"
    
    # models
    with open(config_dir / "models.yml", "r") as file:
      self.models = yaml.safe_load(file)
    
    # translations
    with open(config_dir / "translations.yml", "r") as file:
      self.translations = yaml.safe_load(file)

config = Config()