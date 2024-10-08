from ScribeSense.config.configuration import ConfigurationManager
from ScribeSense.components.data_ingestion import DataIngestion
from ScribeSense.logging import logger

class DataIngestionPipeline:
    def __init__(self) -> None:
        pass
    def main(self):
        config = ConfigurationManager()
        data_ingestion_config = config.get_data_ingestion_config()
        data_ingestion = DataIngestion(config = data_ingestion_config)
        data_ingestion.download()
        data_ingestion.extract_zip_file()