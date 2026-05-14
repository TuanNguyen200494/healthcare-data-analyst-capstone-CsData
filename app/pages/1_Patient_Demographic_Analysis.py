### module được sử dụng để setting render cho Streamlit
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

from app.services.data_normalized import df_healthcare_data_normalized

st.set_page_config(
    page_title="Patient Demographic Analysis",
    layout = "wide"
)

# ws_columns = dataset[0]
# # with st.container():
# #     st.write(columns)
# ws_data = dataset[1:]
# df = pd.DataFrame(ws_data, columns = ws_columns)

# df["Age"] = pd.to_numeric(df["Age"])

st.dataframe(df_healthcare_data_normalized.head(5))

# +   Có tổng cộng bao nhiêu lượt nhập viện (filter theo năm/tháng hoặc quý)
# +   Tuổi trung bình là bao nhiêu ?
# +   Nhóm tuổi nhập viện nhiều nhất ?
# +   Tỷ lệ các nhóm bệnh trên từng nhóm tuổi (ChatGPT advise)




with st.container(border=True):
    st.write("Thông tin bệnh nhân tổng quát")
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("Tổng Lượt Nhập Viện", value = df_healthcare_data_normalized["Name"].count(), border=True)
        st.metric("Tổng Số ca Urgent", value = df_healthcare_data_normalized[df_healthcare_data_normalized["Admission Type"] == "Urgent"]["Admission Type"].count(), border=True)
    with col2:
        st.metric("Tuổi Trung Bình Nhập viện", value = round(df_healthcare_data_normalized["Age"].mean(),1),border=True)
        st.metric("Trung Bình thời gian nằm viện", value = round(df_healthcare_data_normalized["Stay Date"].mean(),1),border=True)
    with col3:
        st.metric("Nhóm tuổi nhập viện cao nhất", value = df_healthcare_data_normalized["Age Group"].mode()[0],border=True)
        st.metric("Nhóm bệnh nhập viện nhiều nhất", value = df_healthcare_data_normalized["Medical Condition"].mode()[0],border=True)
    with col4:
        st.metric("Tỷ lệ xét nghiệm bất thường", value = round((df_healthcare_data_normalized[df_healthcare_data_normalized["Test Results"]=="Abnormal"]["Test Results"].count()/df_healthcare_data_normalized["Test Results"].count())*100,2),border=True)
        st.metric("Tỷ lệ xét nghiệm bất thường ở người dưới 30 tuổi", value = round((df_healthcare_data_normalized[(df_healthcare_data_normalized["Test Results"]=="Abnormal") & (df_healthcare_data_normalized["Age"] < 30)]["Name"].count() / df_healthcare_data_normalized[df_healthcare_data_normalized["Age"] < 30]["Name"].count())*100,2),border=True)


with st.container(border=True):
    st.write("Thông Tin lượt nhập viện chi tiết")
    with st.container(border=True):
        col1, col2 = st.columns(2)
        with col1:           
            select_type = st.selectbox("Lọc Dữ liệu Theo", ["Age Group", "Gender", "Medical Condition", "Admission Type"])
        with col2:
            if select_type:
                start_date = st.date_input("Từ ngày")
                end_date = st.date_input("Tới ngày",min_value = start_date)
            st.button("Execute")
            if (start_date and end_date):
                st.write("đã tìm thấy: " + str(df_healthcare_data_normalized[(df_healthcare_data_normalized["Date of Admission"]>= start_date) & (df_healthcare_data_normalized["Date of Admission"] <= end_date)]["Name"].count()))          
        with st.container():
            st.subheader("Biểu đố số lượng nhập viện theo " + str(select_type) + " từ " + str(start_date) + str(" đến ") + str(end_date))
            if(st.button): 
                col1,col2 = st.columns(2)
                with col1:
                    fig1, ax1 = plt.subplots(figsize=(10,6))
                    df_healthcare_data_normalized_for_chart_1 = df_healthcare_data_normalized[(df_healthcare_data_normalized["Date of Admission"]>= start_date) & (df_healthcare_data_normalized["Date of Admission"] <= end_date)]
                    df_healthcare_data_normalized_for_chart_1 = df_healthcare_data_normalized_for_chart_1.groupby(select_type)["Name"].count().reset_index()
                    df_healthcare_data_normalized_for_chart_1.columns = ["Type", "Count_No"]
                    ax1.pie(df_healthcare_data_normalized_for_chart_1["Count_No"], labels = df_healthcare_data_normalized_for_chart_1["Type"],autopct='%1.1f%%')
                    ax1.legend(df_healthcare_data_normalized_for_chart_1["Type"])
                    st.pyplot(fig1)
                with col2:
                    df_healthcare_data_normalized_for_chart_2 = df_healthcare_data_normalized[(df_healthcare_data_normalized["Date of Admission"]>= start_date) & (df_healthcare_data_normalized["Date of Admission"] <= end_date)]
                    df_healthcare_data_normalized_for_chart_2["Date of Admission"] = pd.to_datetime(df_healthcare_data_normalized_for_chart_2["Date of Admission"])

                    df_healthcare_data_normalized_for_chart_2["Year Admission"] = df_healthcare_data_normalized_for_chart_2["Date of Admission"].dt.year
                    df_healthcare_data_normalized_for_chart_2["Month Admission"] = df_healthcare_data_normalized_for_chart_2["Date of Admission"].dt.month
                    df_healthcare_data_normalized_for_chart_2["Week Admission"] = df_healthcare_data_normalized_for_chart_2["Date of Admission"].dt.isocalendar().week
                    df_healthcare_data_normalized_for_chart_2["Date Admission"] = df_healthcare_data_normalized_for_chart_2["Date of Admission"].dt.day

                    if((end_date - start_date).days <= 7):
                        group_selection = "Date Admission"
                    elif((end_date - start_date).days <= 31):
                        group_selection = "Week Admission"
                    elif((end_date - start_date).days <= 366):
                        group_selection = "Month Admission"
                    else:
                        group_selection = "Year Admission"

                    fig2, ax2 = plt.subplots(figsize=(10,6))
                    df_healthcare_data_normalized_for_chart_2 = df_healthcare_data_normalized_for_chart_2.groupby(group_selection)["Name"].count().reset_index()
                    df_healthcare_data_normalized_for_chart_2.columns = ["Range", "Count_No"]
                    ax2.bar(df_healthcare_data_normalized_for_chart_2["Range"],df_healthcare_data_normalized_for_chart_2["Count_No"])
                    st.pyplot(fig2)

        








    