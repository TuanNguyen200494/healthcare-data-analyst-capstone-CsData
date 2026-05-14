import pandas as pd

from app.services.data_loader import dataset


ds_columns = dataset[0]
ds_data = dataset[1:]

df_healthcare_data =  pd.DataFrame(data=ds_data,columns=ds_columns)

df_healthcare_data_clean = df_healthcare_data

df_healthcare_data_clean["Age"] = pd.to_numeric(df_healthcare_data_clean["Age"])
df_healthcare_data_clean["Stay Date"] = pd.to_numeric(df_healthcare_data_clean["Stay Date"])

df_healthcare_data_clean["Billing Amount"] = df_healthcare_data_clean["Billing Amount"].str.replace(",",".")
df_healthcare_data_clean["Billing Amount"] = pd.to_numeric(df_healthcare_data_clean["Billing Amount"])

df_healthcare_data_clean["Date of Admission"] = pd.to_datetime(df_healthcare_data_clean["Date of Admission"]).dt.date
df_healthcare_data_clean["Discharge Date"] = pd.to_datetime(df_healthcare_data_clean["Discharge Date"]).dt.date


df_healthcare_data_normalized = df_healthcare_data_clean