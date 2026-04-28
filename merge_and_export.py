import pandas as pd


main_df = pd.read_csv("tagged_transaction_logs.csv")
cluster_df = pd.read_csv("clustered_unknown_logs.csv")


CLUSTER_BUSINESS_MAPPING = {
    0: {"tag": "Missed Subscriptions", "icon": "📺"}, 
    1: {"tag": "Local POS & Retail", "icon": "🏪"},  
    2: {"tag": "E-Commerce & ACH", "icon": "💳"}     
}


def apply_cluster_labels(row):
    if row['system_tag'] == 'Unknown':
     
        cluster_record = cluster_df[cluster_df['log_id'] == row['log_id']]
        if not cluster_record.empty:
            c_id = cluster_record.iloc[0]['cluster_id']
            mapping = CLUSTER_BUSINESS_MAPPING.get(c_id, {"tag": "Other", "icon": "❓"})
            return pd.Series([mapping["tag"], mapping["icon"]])
    return pd.Series([row['system_tag'], row['category_icon']])

print("⏳ reading and merging data...")
main_df[['final_tag', 'final_icon']] = main_df.apply(apply_cluster_labels, axis=1)


final_df = main_df[['log_id', 'transaction_date', 'raw_query_text', 'amount', 'final_tag', 'final_icon']]


output_file = "looker_ready_financial_data.csv"
final_df.to_csv(output_file, index=False)

print("\n📊 final classification results:")
print(final_df['final_tag'].value_counts())
print(f"\n🎉 success {len(final_df)} data points classified!")
print(f"📁 final BI analysis table saved to: {output_file}")