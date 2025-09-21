# save_excel.py
import os

def save_to_excel(df, save_path):
    file_path = os.path.join(save_path, "weather_report.xlsx")
    df.to_excel(file_path, index=False)   # directly save DataFrame
    return file_path
