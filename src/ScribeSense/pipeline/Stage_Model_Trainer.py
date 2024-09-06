from ScribeSense.config.configuration import ConfigurationManager
from ScribeSense.components.model_trainer import ModelTrainer
from ScribeSense.logging import logger
import os
class ModelTrainingPipeline:
    def __init__(self) -> None:
        pass
    def main(self):
        config = ConfigurationManager()
        model_trainer_config = config.get_model_config()
        model_trainer_config = ModelTrainer(config=model_trainer_config)
        model_path = os.path.join("artifacts", "model_trainer", "pegasus-samsum-model", "model-001.safetensors") 
        if os.path.exists(model_path):
            print(f"Model already exists at {model_path}. Skipping training...")
        else:
            print("Model not found. Starting training...")
            model_trainer_config.train()