from src.textSummarizer.config.configuration import ConfigurationManager

from src.textSummarizer.components.data_transformation import DataTransformation
from src.textSummarizer.logging import logger


class DataTransformationpipelineConfig:
    def __init__(self):
        pass

    def main(self):

        config = ConfigurationManager()

        data_transformation_config = config.get_data_transformation()

        data_transformation = DataTransformation(
            config=data_transformation_config)
        data_transformation.convert()
