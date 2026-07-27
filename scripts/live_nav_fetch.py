import requests
import pandas as pd

scheme_code = "120841"

url = f"https://api.mfapi.in/mf/{scheme_code}"

response = requests.get(url)

data = response.json()

history = pd.DataFrame(data["data"])

history.to_csv(
    "data/raw/HDFC_Top100_NAV.csv",
    index=False
)

print("Downloaded Successfully")