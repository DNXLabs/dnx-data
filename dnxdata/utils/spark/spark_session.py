import sys
from pyspark import SparkFiles
from pyspark.sql import SparkSession
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from dnxdata.logger import Logger


logger = Logger("Metrics-Transformer =>")


def spark():

    logger.debug("Starting SparkSession")

    spark = SparkSession \
        .builder.appName("Metrics-Transformer => - Data ETL Glue") \
        .enableHiveSupport() \
        .getOrCreate()

    sys.path.insert(0, SparkFiles.getRootDirectory())

    logger.debug("Finishing SparkSession")

    return spark


def glue_context():

    logger.debug("Starting glue_context")

    glue = GlueContext(SparkContext.getOrCreate())

    logger.debug("Finishing glue_context")

    return glue
