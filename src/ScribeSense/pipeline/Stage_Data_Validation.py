from ScribeSense.config.configuration import ConfigurationManager
from ScribeSense.components.data_validation import DataValidation
from ScribeSense.logging import logger

class DataValidationPipeline:
    def __init__(self) -> None:
        pass
    def main(self):
        config = ConfigurationManager()
        data_validation_config = config.get_data_validation_config()
        data_validation = DataValidation(config = data_validation_config)
        data_validation.validate_all_files()