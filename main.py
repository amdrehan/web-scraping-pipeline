import os
import pandas as pd
from scraper import fetch_headlines
from database import init_db, save_to_db

def main():
    # Ensure data directory exists
    if not os.path.exists('data'):
        os.makedirs('data')

    print("Initializing Database...")
    init_db()

    print("Fetching Headlines...")
    data = fetch_headlines()

    if data:
        print(f"Saving {len(data)} items to database...")
        save_to_db(data)
        
        # Transformation/Verification with Pandas
        df = pd.DataFrame(data)
        print("\nData Preview:")
        print(df.head())
    else:
        print("No data retrieved.")

if __name__ == "__main__":
    main()