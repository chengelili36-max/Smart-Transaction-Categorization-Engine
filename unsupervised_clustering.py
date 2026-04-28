import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans


df = pd.read_csv("tagged_transaction_logs.csv")


unknown_df = df[df['system_tag'] == 'Unknown'].copy()
print(f"🔍 success {len(unknown_df)}  'Unknown' record")


vectorizer = TfidfVectorizer(stop_words='english', max_features=500)
X = vectorizer.fit_transform(unknown_df['raw_query_text'])


num_clusters = 3
kmeans = KMeans(n_clusters=num_clusters, random_state=42, n_init=10)
kmeans.fit(X)

unknown_df['cluster_id'] = kmeans.labels_


print("\n🧠 AI no monitoring clustering results:")
order_centroids = kmeans.cluster_centers_.argsort()[:, ::-1]
terms = vectorizer.get_feature_names_out()

for i in range(num_clusters):
    print(f"\n{'='*40}")
    print(f"🔹  (Cluster) {i}:")
    top_terms = [terms[ind] for ind in order_centroids[i, :5]]
    print("   🔑 core terms: " + ", ".join(top_terms))
    

    print("   📄 real samples:")
    samples = unknown_df[unknown_df['cluster_id'] == i]['raw_query_text'].head(3).tolist()
    for sample in samples:
        print(f"      - {sample}")

# 把聚类结果保存下来
unknown_df.to_csv("clustered_unknown_logs.csv", index=False)
print(f"\n✅ clustering analysis complete, detailed results saved to: clustered_unknown_logs.csv")