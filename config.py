import configparser
import os

config_params = configparser.ConfigParser()
config_params.read(os.path.dirname(os.path.realpath(__file__)) + "\\config.ini")
