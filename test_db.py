import pandas as pd
from save_db import save_to_db   # assuming your function is in save_db.py

# Sample DataFrame
data = {
    "timestamp": ["2025-09-21 10:00", "2025-09-21 11:00"],
    "temperature_2m": [20.5, 21.0],
    "relative_humidity_2m": [60, 58]
}
df = pd.DataFrame(data)

# Call function to save
save_to_db(df)
