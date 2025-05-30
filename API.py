
import requests 
import pandas as pd

# Endpoint of API wich contains the required data
url = "http://egov.dai.uom.gr:5001/data"

# get function in API
response = requests.get(url)

# check
if response.status_code >=200 and response.status_code <= 299: #http response status codes  (200-299 succesful responses)
    data = response.json()  # data transformation from JSON to Python dict/list
    
    # transform to pandas DataFrame
    df = pd.DataFrame(data)
    
    df.to_csv("dataset.csv", index=False, encoding="utf-8")
    
    print("Dataset has been saved as : dataset.csv")
else:
    print(f"Error: {response.status_code}")


