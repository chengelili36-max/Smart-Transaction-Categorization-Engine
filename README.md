# 🧠 Smart Transaction Categorization Engine (FinTech)

![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)
![Scikit-Learn](https://img.shields.io/badge/Machine_Learning-Scikit_Learn-F7931E.svg)
![Pandas](https://img.shields.io/badge/Data_Processing-Pandas-150458.svg)
![NLP](https://img.shields.io/badge/NLP-TF--IDF-green.svg)

## 📌 Project Overview
This project is a **Hybrid-Driven Financial Text Classification Engine** designed to process highly unstructured, messy transaction logs and natural language financial queries. 

Instead of relying solely on black-box machine learning, this architecture utilizes a **Dual-Track System** (Rule-Based Regex + Unsupervised K-Means Clustering) to achieve **100% classification coverage** while preventing feature collapse on long-tail data. The final output maps cleanly to UI category icons, preparing the dataset for automated AI auditing and BI dashboards.

## 🏗️ Dual-Track Architecture
1. **Track 1: Deterministic Rule-Based Tagger**
   - Built a high-precision regex engine to extract exact keywords for standard categories (e.g., Dining, Banking).
   - Successfully parsed and tagged ~80% of the dataset with zero false positives.
   
2. **Track 2: Unsupervised ML for Long-Tail Data**
   - Isolated the remaining "Unknown" / messy records (e.g., random ACH transfers, local POS swipes).
   - Applied **TF-IDF Vectorization** to convert unstructured text into numeric features.
   - Deployed **K-Means Clustering** to autonomously discover latent spending behaviors, effectively capturing edge cases (e.g., missed subscriptions due to regex boundary limits).

## 🚀 Key Results
- **100% Categorization Rate:** Successfully transformed 500 unlabelled, noisy transaction logs into a clean, structured dataset.
- **UI-Aligned Output:** Generated `final_icon` and `amount` attributes perfectly aligned with frontend application requirements.
- **Human-in-the-loop (HITL):** Seamlessly translated abstract ML clusters into actionable business labels (e.g., "E-Commerce & Digital Payments").

## 📂 Repository Structure
```text
pennie_ai_classifier/
├── generate_financial_logs.py      # Generates mock unstructured financial data
├── rule_based_tagger.py            # Regex engine for high-precision tagging
├── unsupervised_clustering.py      # TF-IDF & K-Means clustering script
├── merge_and_export.py             # Joins tracks & exports Looker-ready dataset
└── looker_ready_financial_data.csv # Final structured output# Smart-Transaction-Categorization-Engine
