from fetch_data import get_weather_data
from save_excel import save_to_excel
from save_pdf import save_to_pdf
from save_db import save_to_db

from flask import Flask, request, jsonify, send_file
import os
import sqlite3 


app = Flask(__name__)

# Folder to save reports
SAVE_PATH = r"C:\Users\Bhuvaneswari Y\Desktop\Interview\Github\SYMB assignment"

@app.route("/weather-report", methods=["GET"])
def weather_report():
    lat = float(request.args.get("lat", 47.37))
    lon = float(request.args.get("lon", 8.55))
  
    df = get_weather_data(lat, lon)

    if df is not None and not df.empty:
      save_to_db(df)
      return jsonify(df.to_dict(orient="records"))

@app.route("/export/excel", methods=["GET"])
def export_excel():
    df = get_weather_data()
    excel_file = save_to_excel(df, SAVE_PATH)
    return send_file(excel_file, as_attachment=True)

# --- ✅ New Route: Get from DB ---
@app.route("/get-from-db", methods=["GET"])
def get_from_db():
    conn = sqlite3.connect("finaldata.db")
    c = conn.cursor()

    # Fetch last 48 hours (limit rows if needed)
    c.execute("SELECT timestamp, temperature, humidity FROM weather_report ORDER BY id DESC LIMIT 48")
    rows = c.fetchall()
    conn.close()

    # Convert rows to list of dicts
    result = [
        {"timestamp": r[0], "temperature": r[1], "humidity": r[2]}
        for r in rows
    ]

    return jsonify(result)


@app.route("/export/pdf", methods=["GET"])
def export_pdf():
    df = get_weather_data()
    pdf_file = save_to_pdf(df, SAVE_PATH)
    return send_file(pdf_file, as_attachment=True)

if __name__ == "__main__":
    app.run(debug=True)

