import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

from app.services.data_normalized import df_healthcare_data_normalized

st.set_page_config(
    page_title="Medical Condition Analysis",
    layout = "wide"
)

# Phân tích chuyển sâu về các nhóm bệnh, giải quyết các vấn đề:
#         +   Medical Condition nào phổ biến nhất (theo nhóm máu, nhóm tuổi, giới tính)
#         +   Billing Amount của từng nhóm bệnh 
#         +   Thời gian nằm viện dài nhất.
#         +   Test Result trả về Abnormal nhiều nhất ở nhóm bệnh nào? nhóm tuổi? nhóm máu? (ChatGPT advise)


st.write("Phân Tích Chuyên sâu cho từng nhóm bệnh")

with st.container(border=True):
    select_type = st.selectbox("Chọn thông tin nhóm bệnh", df_healthcare_data_normalized["Medical Condition"].unique())
    df_page2 = df_healthcare_data_normalized[df_healthcare_data_normalized["Medical Condition"] == select_type]
    with st.container(border=True):
        st.write("Thông tin bệnh theo nhóm máu")
        df_ranked = df_page2.groupby("Blood Type")["Name"].count().reset_index()
        df_ranked["Rank"] = df_ranked["Name"].rank(ascending=False).astype(int)       
        #st.dataframe(df_ranked)
        blood_type = df_healthcare_data_normalized["Blood Type"].unique()
        rank_means = int(len(blood_type)/2)
        for bt in blood_type:
            with st.container(border=True):
                st.write("Thông tin nhóm máu "+ str(bt))
                col1,col2,col3,col4 = st.columns(4)
                with col1:
                    if(df_ranked[df_ranked["Blood Type"] == bt]["Rank"].values[0] < rank_means):
                        color = "inverse"
                    elif(df_ranked[df_ranked["Blood Type"] == bt]["Rank"].values[0] > rank_means):
                        color = "normal"
                    else:
                        color = "off"
                    st.metric("Tổng số ca nhiễm", value = df_ranked[df_ranked["Blood Type"] == bt]["Name"].values[0],delta=df_ranked[df_ranked["Blood Type"] == bt]["Rank"].values[0], delta_color=color,delta_arrow="off",delta_description="Rank",border=True)
                with col2:
                    st.metric("Tỷ lệ phát hiện bất thường", value = round(df_page2[(df_page2["Blood Type"] == bt) & (df_page2["Test Results"]=="Abnormal")]["Name"].count()/df_page2[(df_page2["Blood Type"] == bt)]["Name"].count()*100,2),border=True)
                with col3:
                    st.metric("Trung bình thời gian điều trị", value=round(df_page2[df_page2["Blood Type"] == bt]["Stay Date"].mean(),1),border=True)
                with col4:
                    st.metric("trung bình chi phí điều trị", value=round(df_page2[df_page2["Blood Type"] == bt]["Billing Amount"].mean(),1),border=True)
    with st.container(border=True):
        st.write("Thông tin bệnh theo nhóm tuổi")
        df_ranked = df_page2.groupby("Age Group")["Name"].count().reset_index()
        df_ranked["Rank"] = df_ranked["Name"].rank(ascending=False).astype(int)       
        #st.dataframe(df_ranked)
        blood_type = df_healthcare_data_normalized["Age Group"].unique()
        rank_means = int(len(blood_type)/2)
        for bt in blood_type:
            with st.container(border=True):
                st.write("Thông tin nhóm tuổi "+ str(bt))
                col1,col2,col3,col4 = st.columns(4)
                with col1:
                    if(df_ranked[df_ranked["Age Group"] == bt]["Rank"].values[0] < rank_means):
                        color = "inverse"
                    elif(df_ranked[df_ranked["Age Group"] == bt]["Rank"].values[0] > rank_means):
                        color = "normal"
                    else:
                        color = "off"
                    st.metric("Tổng số ca nhiễm", value = df_ranked[df_ranked["Age Group"] == bt]["Name"].values[0],delta=df_ranked[df_ranked["Age Group"] == bt]["Rank"].values[0], delta_color=color,delta_arrow="off",delta_description="Rank",border=True)
                with col2:
                    st.metric("Tỷ lệ phát hiện bất thường", value = round(df_page2[(df_page2["Age Group"] == bt) & (df_page2["Test Results"]=="Abnormal")]["Name"].count()/df_page2[(df_page2["Age Group"] == bt)]["Name"].count()*100,2),border=True)
                with col3:
                    st.metric("Trung bình thời gian điều trị", value=round(df_page2[df_page2["Age Group"] == bt]["Stay Date"].mean(),1),border=True)
                with col4:
                    st.metric("trung bình chi phí điều trị", value=round(df_page2[df_page2["Age Group"] == bt]["Billing Amount"].mean(),1),border=True)
    with st.container(border=True):
        st.write("Thông tin bệnh theo Giới Tính")
        df_ranked = df_page2.groupby("Gender")["Name"].count().reset_index()
        df_ranked["Rank"] = df_ranked["Name"].rank(ascending=False).astype(int)       
        #st.dataframe(df_ranked)
        blood_type = df_healthcare_data_normalized["Gender"].unique()
        rank_means = int(len(blood_type)/2)
        for bt in blood_type:
            with st.container(border=True):
                st.write("Thông tin Giới Tính "+ str(bt))
                col1,col2,col3,col4 = st.columns(4)
                with col1:
                    if(df_ranked[df_ranked["Gender"] == bt]["Rank"].values[0] < rank_means):
                        color = "inverse"
                    elif(df_ranked[df_ranked["Gender"] == bt]["Rank"].values[0] > rank_means):
                        color = "normal"
                    else:
                        color = "off"
                    st.metric("Tổng số ca nhiễm", value = df_ranked[df_ranked["Gender"] == bt]["Name"].values[0],delta=df_ranked[df_ranked["Gender"] == bt]["Rank"].values[0], delta_color=color,delta_arrow="off",delta_description="Rank",border=True)
                with col2:
                    st.metric("Tỷ lệ phát hiện bất thường", value = round(df_page2[(df_page2["Gender"] == bt) & (df_page2["Test Results"]=="Abnormal")]["Name"].count()/df_page2[(df_page2["Gender"] == bt)]["Name"].count()*100,2),border=True)
                with col3:
                    st.metric("Trung bình thời gian điều trị", value=round(df_page2[df_page2["Gender"] == bt]["Stay Date"].mean(),1),border=True)
                with col4:
                    st.metric("trung bình chi phí điều trị", value=round(df_page2[df_page2["Gender"] == bt]["Billing Amount"].mean(),1),border=True)