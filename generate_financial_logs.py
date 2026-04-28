import pandas as pd
import random
from datetime import datetime, timedelta


start_date = datetime(2025, 12, 4)
end_date = datetime(2026, 1, 9)
delta_days = (end_date - start_date).days


text_templates = [

    "Netflix monthly charge", "apple tv+ sub", "Spotify premium plan", 
    "amzn prime video", "hulu no ads", "disney+ subscription fee",

    "PG&E monthly bill", "comcast internet bill", "at&t wireless phone", 
    "water service san jose", "conedison power",
  
    "transfer to saving", "atm withdrawal", "zelle payment to john", 
    "chase credit card auto-pay", "wire transfer fee",
   
    "mcdonalds doordash", "starbucks coffee", "uber eats delivery", 
    "whole foods market", "trader joes grocery",

    "POS DEBIT 12/24/2025 terminal 482", "ach web payment random stuff", 
    "sq *local coffee shop", "paypal *ebay purchase"
]

def random_date():
    random_days = random.randint(0, delta_days)
    return start_date + timedelta(days=random_days)


data = []
for i in range(500):
    raw_text = random.choice(text_templates)
   
    if random.random() > 0.5:
        raw_text = raw_text + f" ref #{random.randint(1000,9999)}"
        
  
    amount = round(random.uniform(5.0, 500.0), 2)
    
    data.append({
        "log_id": f"LOG_{i+1000}",
        "transaction_date": random_date().strftime("%Y-%m-%d"),
        "raw_query_text": raw_text,
        "amount": amount,
    
        "system_tag": None 
    })


df = pd.DataFrame(data)

df = df.sort_values(by="transaction_date").reset_index(drop=True)

output_file = "raw_transaction_logs.csv"
df.to_csv(output_file, index=False)

print(f"✅ success {len(df)} transaction logs generated.")
print(f"📅 log range: 2025/12/04 - 2026/01/09")
print(f"📁 file saved to: {output_file}")