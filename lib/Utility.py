from pyspark.sql import SparkSession
from lib.configreader import pysparkconfig

def sprk_session(env):
    if env == "Loc":
        return  SparkSession.builder \
        .config(conf = pysparkconfig(env)) \
        .master("local[2]") \
        .getOrCreate()

    else:
         return  SparkSession \
                .config(conf = pysparkconfig(env)) \
                .master("yarn") \
                .enableHiveSupport() \
                .getOrCreate()
        
