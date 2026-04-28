import pandas as pd
import re


input_file = "raw_transaction_logs.csv"
try:
    df = pd.read_csv(input_file)
except FileNotFoundError:
    print(f"❌ cannot find {input_file}please run generate_financial_logs.py first to create the raw data.")
    exit()



CATEGORY_RULES = {
    "Subscriptions": {"keywords": ["netflix", "spotify", "apple tv", "amzn prime", "hulu", "disney+"], "icon": "📺"},
    "Utilities": {"keywords": ["pg&e", "comcast", "at&t", "water service", "conedison"], "icon": "⚡️"},
    "Banking": {"keywords": ["transfer", "atm", "zelle", "auto-pay", "wire"], "icon": "🏦"},
    "Dining": {"keywords": ["mcdonalds", "starbucks", "uber eats", "whole foods", "trader joes", "doordash"], "icon": "🍔"}
}

def apply_rules(text):
    text_lower = str(text).lower()
    for category, mapping in CATEGORY_RULES.items():
        for keyword in mapping["keywords"]:
          
            if re.search(r'\b' + re.escape(keyword) + r'\b', text_lower):
                return pd.Series([category, mapping["icon"]])
    

    return pd.Series(["Unknown", "❓"])


print("⏳ running rule-based tagger...")
df[['system_tag', 'category_icon']] = df['raw_query_text'].apply(apply_rules)


df['amount_is_valid'] = df['amount'].apply(lambda x: isinstance(x, float) and x > 0)


tagged_count = len(df[df['system_tag'] != 'Unknown'])
unknown_count = len(df[df['system_tag'] == 'Unknown'])

print("\n📊 Classification Results:")
print(df['system_tag'].value_counts())
print(f"\n✅ Rule Engine Coverage: {(tagged_count / len(df)) * 100:.1f}%")
print(f"⚠️ Remaining Unknown Long-tail Data for Unsupervised Learning: {unknown_count} entries")

#
output_file = "tagged_transaction_logs.csv"
df.to_csv(output_file, index=False)
print(f"\n📁 tagged transaction logs saved to: {output_file}")