import pandas as pd
from config import CSV_FILE
from utils import log

class Storage:
    def save_to_csv(self, data):
        """Save scraped data to CSV"""
        df = pd.DataFrame(data)
        df.to_csv(CSV_FILE, index=False, encoding='utf-8-sig')  
        log(f"✅ Data saved successfully to {CSV_FILE}")
