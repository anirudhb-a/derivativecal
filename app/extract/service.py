import databento as db
from dotenv import  load_dotenv
import os


# load environment from dotenv
load_dotenv()

DB_API_KEY = os.getenv('DB_API_KEY')

# Establish connection and authenticate
client = db.Historical(DB_API_KEY)



def publisher_data():
  symbol = "NVDA.US"  # Use the correct symbol format for NVDA in Databento
  start_date = "2023-01-01"  # Example start date
  end_date = "2023-09-01"    # Example end date (optional)
  dataset = "PX.D"           # Daily prices dataset

# fetch the daily prices of Nvidia
  data = client.get_hist(
    dataset=dataset,
    symbols=symbol,
    start=start_date,
    end=end_date,
    limit=2  # You can adjust the limit as needed
  )
  return data