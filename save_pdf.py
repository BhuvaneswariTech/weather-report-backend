# save_pdf.py
import os
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image
from reportlab.lib.styles import getSampleStyleSheet

def save_to_pdf(df, save_path):
    # File path
    file_path = os.path.join(save_path, "weather_report.pdf")

    # Generate line chart
    plt.figure(figsize=(9, 4))  # slightly wider chart
    plt.plot(df["timestamp"], df["temperature_2m"], label="Temperature (°C)", color="blue")
    plt.plot(df["timestamp"], df["relative_humidity_2m"], label="Humidity (%)", color="orange")
    plt.xlabel("Time")
    plt.ylabel("Values")
    plt.title("Weather Data")
    plt.legend()

    # ✅ Format x-axis (limit number of labels)
    ax = plt.gca()
    ax.xaxis.set_major_locator(MaxNLocator(nbins=8))  # max 8 ticks
    plt.xticks(rotation=45, ha="right")  # rotate & align labels

    # Save chart as image
    chart_path = os.path.join(save_path, "chart.png")
    plt.tight_layout()
    plt.savefig(chart_path, dpi=150)  # better quality
    plt.close()

    # Create PDF
    doc = SimpleDocTemplate(file_path, pagesize=letter)
    styles = getSampleStyleSheet()
    elements = []

    elements.append(Paragraph("Weather Report", styles["Title"]))
    elements.append(Spacer(1, 12))

    avg_temp = df["temperature_2m"].mean()
    avg_hum = df["relative_humidity_2m"].mean()
    elements.append(Paragraph(f"Average Temperature: {avg_temp:.2f} °C", styles["Normal"]))
    elements.append(Paragraph(f"Average Humidity: {avg_hum:.2f} %", styles["Normal"]))
    elements.append(Spacer(1, 12))

    # Add chart
    elements.append(Image(chart_path, width=500, height=250))

    doc.build(elements)
    return file_path
