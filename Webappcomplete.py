import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 🎯 main
st.header("📊 การศึกษาหาค่าสัมประสิทธิ์การใช้น้ำของข้าวด้วยเครื่องวัดระดับน้ำในนาข้าว โดยวิธี Penman-Monteith")

# 📌 upload
uploaded_file = st.file_uploader("📂 อัปโหลดไฟล์ Excel (.xlsx)", type=["xlsx"])

if uploaded_file:
    # read Excel
    xls = pd.ExcelFile(uploaded_file)

    # 🔹 Sheet 1: WTH
    st.header("📌 Wheather Station Data ")
    sheet1_df = pd.read_excel(xls, sheet_name="Sheet1")
    st.dataframe(sheet1_df)

    # 🔹 Sheet 2: ETo 
    st.header("📌ETo รายวัน (mm/day) ")
    sheet2_df = pd.read_excel(xls, sheet_name="Sheet2")
    st.dataframe(sheet2_df)

    plt.figure(figsize=(10, 5))
    sns.lineplot(data=sheet2_df, x="Timestamp", y="ETo (mm/day)", marker="o")
    plt.xticks(rotation=45)
    plt.xlabel("D/M/Y")
    plt.ylabel("ETo")
    plt.title("ETo vs. Date")
    st.pyplot(plt)

    # 🔹 Sheet 3: ETo, ET  Week
    st.header("📌ตารางแสดงผลค่า ET และ ETo รายสัปดาห์")
    sheet3_df = pd.read_excel(xls, sheet_name="Sheet3")
    st.dataframe(sheet3_df)

    plt.figure(figsize=(10, 5))
    sns.lineplot(data=sheet3_df, x="Week", y="Eto (mm)", marker="o", label="ETo")
    sns.lineplot(data=sheet3_df, x="Week", y="ET (mm)", marker="s", label="ET")
    plt.xlabel("Week")
    plt.ylabel("Values")
    plt.title("ETo & ET per Week")
    plt.legend()
    st.pyplot(plt)

    # 🔹 Sheet 4
    st.header("📌ตารางแสดงผลการวิเคราห์ค่า Kc นาน้ำขัง Kc นาเปียกสลับแห้ง และ Kc กรมชลประทาน")
    sheet4_df = pd.read_excel(xls, sheet_name="Sheet4")
    st.dataframe(sheet4_df)

    plt.figure(figsize=(10, 5))
    sns.lineplot(data=sheet4_df, x="Week", y="KcAWD(cal)", marker="o", label="KcAWD")
    sns.lineplot(data=sheet4_df, x="Week", y="Kc(Cal)", marker="s", label="Kc cal")
    sns.lineplot(data=sheet4_df, x="Week", y="Kc (RID)", marker="^", label="Kc RID")
    plt.ylim(0, 3)
    plt.xlabel("Week")
    plt.ylabel("Kc Values")
    plt.title("KcAWD,Kc(cal) and Kc(RID) per week")
    plt.legend()
    st.pyplot(plt)
