import pandas as pd
from datetime import date


## module này chỉ cần chạy 1 lần trong dự án, mục đích để đưa toàn bộ dataset này lên tại google sheet, ngoài ra các def sẽ được reuse cho trường hợp nhập input

df_health_raw = pd.read_csv('/Users/tuananhnguyen/Desktop/AI Bootcamp/data-analyst-healthcare/data/raw/healthcare_dataset.csv')

df_health_clean = df_health_raw

def upper_data(i):
    return i.upper()


def calculate_stay(i):
    return i["Discharge Date"] - i["Date of Admission"]

#tạo thêm 1 cột quy đổi về nhóm tuổi (0-16, 17-30, 31-45, 46-60, 61-75, 75+)
def age_group(i):
    if i > 75:
        return "75+"
    elif 61 <= i <= 75:
        return "61-75"
    elif 46 <= i <= 60:
        return "46-60"
    elif 31 <= i <= 45:
        return "31-45" 
    elif 17 <= i <= 30:
        return "17-30"
    else:
        return "0-16"



def billing_fill(i):
    if(i < 0):
        return new_mean
    else:
        return i
    


##Billing category:
def billing_class(i):
    if(i >= q3):
        return "Very High"
    elif(i >= q2):
        return "High"
    elif(i >= q1):
        return "Medium"
    else:
        return "Low"
    

df_health_clean["Age Group"] = df_health_clean["Age"].apply(age_group)

df_health_clean["Name"]= df_health_clean["Name"].apply(upper_data)
df_health_clean["Doctor"]= df_health_clean["Doctor"].apply(upper_data)
df_health_clean["Date of Admission"] = pd.to_datetime(df_health_clean["Date of Admission"]).dt.date
df_health_clean["Discharge Date"] = pd.to_datetime(df_health_clean["Discharge Date"]).dt.date

df_health_clean["Stay Date"] = df_health_clean.apply(calculate_stay, axis=1)
df_health_clean["Stay Date"] = df_health_clean["Stay Date"].dt.days

new_mean = df_health_clean[df_health_clean["Billing Amount"]>0]["Billing Amount"].mean()
df_health_clean["Billing Amount"] = df_health_clean["Billing Amount"].apply(billing_fill)

q1 = df_health_clean["Billing Amount"].quantile(0.25)
q2 = df_health_clean["Billing Amount"].quantile(0.5)
q3 = df_health_clean["Billing Amount"].quantile(0.75)

df_health_clean["Billing Group"] = df_health_clean["Billing Amount"].apply(billing_class)

##Lưu kết df_health_clean tại data/processed
df_health_clean.to_csv("/Users/tuananhnguyen/Desktop/AI Bootcamp/data-analyst-healthcare/data/processed/Healthcare_Processed_Clean.csv", index=False)

df_health_normalized = df_health_clean
df_health_normalized.to_csv("/Users/tuananhnguyen/Desktop/AI Bootcamp/data-analyst-healthcare/outputs/Healcare_Normalized.csv", index=False)