import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 🎯 main
st.header("📊 การศึกษาหาค่าสัมประสิทธิ์การใช้น้ำของข้าวด้วยเครื่องวัดระดับน้ำในนาข้าว โดยวิธี Penman-Monteith")

# 📌 Fetch data from Google Sheets
sheet_url = "https://docs.google.com/spreadsheets/d/1JT_GsDU-X-Adq59TPyFqriPcqM_l5ShkxlrCStHtpg0/export?format=xlsx"

@st.cache_data
def load_data(url):
    xls = pd.ExcelFile(url)
    return {
        "Sheet1": pd.read_excel(xls, sheet_name="Sheet1"),
        "Sheet2": pd.read_excel(xls, sheet_name="Sheet2"),
        "Sheet3": pd.read_excel(xls, sheet_name="Sheet3"),
        "Sheet4": pd.read_excel(xls, sheet_name="Sheet4"),
    }

data = load_data(sheet_url)

# 🔹 Sheet 1: WTH
st.header("📌 Wheather Station Data ")
st.dataframe(data["Sheet1"])

# 🔹 Sheet 2: ETo 
st.header("📌ETo รายวัน (mm/day) ")
st.dataframe(data["Sheet2"])

plt.figure(figsize=(10, 5))
sns.lineplot(data=data["Sheet2"], x="Timestamp", y="ETo (mm/day)", marker="o")
plt.xticks(rotation=45)
plt.xlabel("D/M/Y")
plt.ylabel("ETo(mm/day)")
plt.title("ETo per week")
st.pyplot(plt)

# 🔹 Sheet 3: ETo, ET  Week
st.header("📌ตารางแสดงผลค่า ET นาน้ำขัง ET นาเปียกสลับแห้ง และ ET กรมชลประทาน รายสัปดาห์")
st.dataframe(data["Sheet3"])

plt.figure(figsize=(10, 5))
sns.lineplot(data=data["Sheet3"], x="Week", y="ET_Flooded (mm/day)", marker="o", label="ET_Flooded (mm/day)")
sns.lineplot(data=data["Sheet3"], x="Week", y="ET_AWD (mm/day)", marker="s", label="ET_AWD (mm/day)")
sns.lineplot(data=data["Sheet3"], x="Week", y="ET_RID(mm/day)", marker="^", label="ET_RID(mm/day)")
plt.xlabel("Week")
plt.ylabel("ET(mm/day)")
plt.title(" Evapotranspiration per Week")
plt.legend()
st.pyplot(plt)

# 🔹 Sheet 4
st.header("📌ตารางแสดงผลการวิเคราห์ค่า Kc นาน้ำขัง Kc นาเปียกสลับแห้ง และ Kc กรมชลประทาน รายสัปดาห์")
st.dataframe(data["Sheet4"])

plt.figure(figsize=(10, 5))
sns.lineplot(data=data["Sheet4"], x="Week", y="Kc(Flooded)", marker="o", label="Kc(Flooded)")
sns.lineplot(data=data["Sheet4"], x="Week", y="Kc(AWD)", marker="s", label="Kc(AWD)")
sns.lineplot(data=data["Sheet4"], x="Week", y="Kc (RID)", marker="^", label="Kc (RID)")
plt.ylim(0, 3)
plt.xlabel("Week")
plt.ylabel("Kc ")
plt.title("Kc(AWD),Kc(Flooded) and Kc(RID) per week")
plt.legend()
st.pyplot(plt)
