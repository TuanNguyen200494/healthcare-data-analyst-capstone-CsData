import pandas as pd
import json
import os

from app.services.path_provider import root,config_path,cred_path
from app.services.gs_service import gs_connector


def read_config(config_path):
    if not os.path.exists(config_path):
        raise FileNotFoundError("Cannot find config file:" + str(config_path))
    else:
        with open(config_path, "r", encoding="utf-8") as file:
            config = json.load(file)
    return config

json_config = read_config(config_path)
gs_sheet_information = json_config["google_sheet_information"]
wb = gs_connector(cred_path, gs_sheet_information["spreadsheet_id"], gs_sheet_information["worksheets"]["master_data"])
dataset = wb.get_values()

