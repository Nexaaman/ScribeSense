from ScribeSense.config.configuration import ConfigurationManager
from ScribeSense.components.data_transformation import DataTransformation
from ScribeSense.logging import logger


class DataTransformationPipeline:
    def __init__(self) -> None:
        pass
    def main(self):
        config = ConfigurationManager()
        data_transformation_config = config.get_data_transformation_config()
        data_transformation = DataTransformation(config = data_transformation_config)
        data_transformation.convert()