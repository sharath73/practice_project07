import configparser
from pyspark import SparkConf

def appconfig(env):
   conf = configparser.ConfigParser()
   conf.read("Configs/application.conf")
   data ={}
   for (key,value) in conf.items(env):
      data[key] = value

   return data


def pysparkconfig(env):
   conf = configparser.ConfigParser()
   conf.read("configs/pysparkconfig.conf")
   psprk = SparkConf()
   for (key,val) in conf.items(env):
      psprk.set(key,val)
   return psprk
