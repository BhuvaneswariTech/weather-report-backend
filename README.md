Weather Report Backend
A Flask-based backend project that fetches weather data from the Open-Meteo API, stores it in SQLite, and allows exporting reports to Excel and PDF with charts.
________________________________________
Features
•	Fetch real-time weather data
•	Save data into SQLite database
•	Export reports to Excel (.xlsx) and PDF (with charts)
•	Simple Flask app to run everything
________________________________________
Project Structure
app.py → Main Flask app
fetch_data.py → Fetch weather data from API
save_db.py → Save data into database
save_excel.py → Export data to Excel
save_pdf.py → Export data to PDF
check_db.py → Check database contents
test_db.py → Test database functions
requirements.txt → Project dependencies
README.md → Documentation
.gitignore → Ignored files
________________________________________
Installation
1.	Clone the repository
o	git clone https://github.com/BhuvaneswariTech/weather-report-backend.git
o	cd weather-report-backend
2.	Create a virtual environment (recommended)
o	python -m venv venv
o	venv\Scripts\activate (on Windows)
3.	Install dependencies
o	pip install -r requirements.txt
________________________________________

How to Run
1.	Start the Flask app
o	python app.py
o	The app will run at http://127.0.0.1:5000/
2.	Fetch and save data
o	python fetch_data.py
o	This will call the Open-Meteo API and store the data in the SQLite database.
3.	Export data to Excel
o	python save_excel.py
o	Output file: weather_report.xlsx
4.	Export data to PDF
o	python save_pdf.py
o	Output file: weather_report.pdf
5.	Check database contents (optional)
o	python check_db.py
________________________________________
Technologies Used
•	Python (Flask)
•	SQLite
•	Requests
•	Pandas
•	Matplotlib
•	ReportLab
•	OpenPyXL

# weather-report-backend
A Flask-based backend service that fetches weather data from Open-Meteo API, stores it in SQLite, and provides export to Excel &amp; PDF with charts.
