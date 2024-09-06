from ScribeSense.pipeline.Stage_Data_Ingestion import DataIngestionPipeline
from ScribeSense.pipeline.Stage_Data_Validation import DataValidationPipeline
from ScribeSense.pipeline.Stage_Data_Transformation import DataTransformationPipeline
from ScribeSense.pipeline.Stage_Model_Trainer import ModelTrainingPipeline
from ScribeSense.pipeline.Stage_Model_Evaluation import ModelEvaluationPipeline
from ScribeSense.logging import logger

STAGE_NAME = "Data Ingestion"

try:
    logger.info(f"************{STAGE_NAME}************")
    data_ingestion = DataIngestionPipeline()
    data_ingestion.main()
    logger.info(f"************{STAGE_NAME} completed Succesfully************")

except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Data Validation"

try:
    logger.info(f"************{STAGE_NAME}************")
    data_Validation = DataValidationPipeline()
    data_Validation.main()
    logger.info(f"************{STAGE_NAME} completed Succesfully************")

except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Data Transformation"
try:
    logger.info(f"************{STAGE_NAME}************")
    data_Transformation = DataTransformationPipeline()
    data_Transformation.main()
    logger.info(f"************{STAGE_NAME} completed Succesfully************")

except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Model Training"
try:
    logger.info(f"************{STAGE_NAME}************")
    data_Transformation = ModelTrainingPipeline()
    data_Transformation.main()
    logger.info(f"************{STAGE_NAME} completed Succesfully************")

except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Model Evaluation"
try:
    logger.info(f"************{STAGE_NAME}************")
    data_Transformation = ModelEvaluationPipeline()
    data_Transformation.main()
    logger.info(f"************{STAGE_NAME} completed Succesfully************")

except Exception as e:
    logger.exception(e)
    raise e



