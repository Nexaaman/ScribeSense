from ScribeSense.config.configuration import ConfigurationManager
from ScribeSense.components.model_evaluation import ModelEvaluation
from ScribeSense.logging import logger
import os
class ModelEvaluationPipeline:
    def __init__(self) -> None:
        pass
    def main(self):
        config = ConfigurationManager()
        model_eval_config = config.get_model_eval_config()
        model_eval_config = ModelEvaluation(config = model_eval_config)

        model_path = os.path.join("artifacts", "model_evaluation", "evaluation_results.csv")

        if os.path.exists(model_path):
            print(f"Csv already exists at {model_path}. Skipping ...")
        else:
            print("Csv not found. Starting evaluation...")
            model_eval_config.evaluate()