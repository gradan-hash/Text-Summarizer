from src.textSummarizer.pipeline.stage01_data_ingestion import DataIngestionTrainingPipeline
from src.textSummarizer.logging import logger

STAGE_NAME = "Data Ingestion Stage"

try:
    logger.info(f">>>>> stage{STAGE_NAME} started")
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed \n")

except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "Data Validation Stage"

try:
    logger.info(f">>>>> stage{STAGE_NAME} started")
    data_validation = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed \n")

except Exception as e:
    logger.exception(e)
    raise e