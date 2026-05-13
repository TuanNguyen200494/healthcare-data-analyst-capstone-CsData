import pandas as pd
import json
import os
from pathlib import Path

from gs_service import gs_connector

def read_config(config_path):
    if not os.path.exists(config_path):
        raise FileNotFoundError("Cannot find config file:" + str(config_path))
    else:
        with open(config_path, "r", encoding="utf-8") as file:
            config = json.load(file)
    return config

root = Path(__file__).resolve().parents[2]
config_path = root / "app" / "config" / "config.json"
#print(root)
#print(config_path)
cred_path = root / ".secrets" / "healthcare-capstone-service.json"
dataset_normalized_path = root / "outputs" / "Healcare_Normalized.csv"


json_config = read_config(config_path)
#print(json_config)
#print(type(json_config))

##Type của json_config là kiểu dict bình thường, vậy truy cập như dict
google_sheet_info = json_config["google_sheet_information"]
#print(google_sheet_info)

## get worksheet_id:
wb_id = google_sheet_info["spreadsheet_id"]
#print (wb_id)

## get sheetname

ws_name = google_sheet_info["worksheets"]["master_data"]
#print(ws_name)

#cred_info = read_config(cred_path)

#print(cred_info)

#open connect
worksheet = gs_connector(cred_path, wb_id, ws_name)

df = pd.read_csv(dataset_normalized_path)

columns = df.columns.tolist()
data = df.values.tolist()
count = 0
for d in data:
    if count <= 2:
        print(d)
        count += 1
    else:
        break
#print(columns)
full = [columns] + data ##ở đây phát sinh ra lỗi, chatGPT có advise rằng việc update vào google sheet cần một data kiểu mảng 2 chiều, các values trong data của df thì ổn, riêng column nó chỉ mới là một mảng một chiều, phải thêm []
# về sau, khi muốn add một dòng mới vào dữ liệu bắt buộc phải là mảng 2 chiều.

#print(full)
worksheet.clear()
worksheet.update(full)
