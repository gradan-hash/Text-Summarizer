from src.textSummarizer.pipeline.stage01_data_ingestion import DataIngestionTrainingPipeline


from src.textSummarizer.pipeline.stage02_data_validation import DataValidationpipelineConfig


from src.textSummarizer.pipeline.stage03_data_transformation import DataTransformationpipelineConfig
from src.textSummarizer.pipeline.stage04_model_trainer import ModelTrainerpipelineConfig


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

    data_validation = DataValidationpipelineConfig()

    data_validation.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed \n")

except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "Data Transformation Stage"

try:
    logger.info(f">>>>> stage{STAGE_NAME} started")

    data_transformation = DataTransformationpipelineConfig()

    data_transformation.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed \n")

except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Model trainnig  Stage"

try:
    logger.info(f">>>>> stage{STAGE_NAME} started")

    model_trainning = ModelTrainerpipelineConfig()

    model_trainning.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed \n")

except Exception as e:
    logger.exception(e)
    raise e
