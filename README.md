# Customer Segmentation Analysis: Unsupervised Learning Approach

## 📋 Overview

This project performs comprehensive customer segmentation using unsupervised machine learning techniques (K-Means clustering) on retail transaction data. The analysis transforms raw transactional data into actionable customer insights, enabling data-driven marketing strategies and personalized customer engagement.

The analysis workflow encompasses:

1. **Data Collection & Preparation:** Loading and initial data inspection
2. **Data Cleaning:** Handling missing values, outliers, and inconsistencies
3. **Exploratory Data Analysis (EDA):** Understanding patterns and relationships
4. **Feature Engineering:** Creating meaningful features for clustering
5. **Clustering Analysis:** K-Means segmentation with visualization
6. **Business Insights:** Actionable recommendations per customer segment

---

## 🎯 Project Objectives

- Identify distinct customer segments based on purchasing behavior
- Understand demographic and behavioral patterns within each segment
- Provide actionable insights for targeted marketing strategies
- Create a customer-centric analytical framework

---

## 📊 Dataset Description

**Source:** `Dataset (1).csv`

**Initial Features:**

- `Transaction ID`: Unique transaction identifier
- `Date`: Transaction date
- `Customer ID`: Unique customer identifier
- `Gender`: Customer gender (Male/Female)
- `Age`: Customer age in years
- `Product Category`: Product type (Beauty/Clothing/Electronics)
- `Quantity`: Number of items purchased
- `Price per Unit`: Price per individual item (€)
- `Total Amount`: Total transaction value (€)

**Dataset Statistics:**

- Total Observations: 1,050 transactions
- Features: 9 columns
- Missing Values: ~3.5% (37 missing values across multiple columns)

---

## 🔧 Data Preprocessing Pipeline

### 1. Data Type Conversions

- **Date Column:** Converted from object to datetime format for temporal analysis

### 2. Missing Value Imputation

| Feature            | Method            | Value                     | Rationale                                                |
| ------------------ | ----------------- | ------------------------- | -------------------------------------------------------- |
| `Age`              | Mode              | 43.0                      | Distribution slightly right-skewed; mode closest to mean |
| `Gender`           | Mode              | Male                      | Simple imputation for categorical variable               |
| `Product Category` | KNN Imputer (k=3) | -                         | Leverages similarity to other features for prediction    |
| `Quantity`         | Median            | 3.0                       | Robust to outliers                                       |
| `Price per Unit`   | Mode              | 50.0                      | Most common price point                                  |
| `Total Amount`     | Calculation       | Quantity × Price per Unit | Ensures data consistency                                 |

### 3. Outlier Treatment

- **Age:** Values < 16 adjusted to 16 (minimum customer age)
- **Quantity:** Negative values corrected to 3 (median)
- **Price per Unit:** Negative values corrected to 20

### 4. Data Validation

- **Duplicate Check:** No duplicates found
- **Consistency Check:** `Total Amount` recalculated to ensure accuracy

---

## 🔍 Exploratory Data Analysis

### Key Findings

**📈 Temporal Patterns:**

- **Peak Sales Period:** May (potential Easter holiday effect)
- **High Sales:** February (discount season) and November-December (holiday shopping)
- **Low Sales:** January (potentially incomplete data)

**🛍️ Product Categories:**

- Three distinct categories analyzed: Beauty, Clothing, Electronics
- Category preferences vary significantly across customer segments

**👥 Demographic Insights:**

- **Gender Spending:** Female customers exhibit slightly higher average spending
- **Age Distribution:** Customers span ages 16-65, with clustering around middle age groups

**🔗 Feature Correlations:**

- `Price per Unit` ↔ `Total Amount`: Strong positive correlation (0.85)
- `Quantity` ↔ `Total Amount`: Moderate positive correlation (0.36)

---

## ⚙️ Feature Engineering

### Created Features

1. **`Gender_Male`** (Binary)

   - 1 = Male, 0 = Female
   - Enables numerical analysis of gender effects

2. **Product Category Dummies**

   - `Beauty` (0/1)
   - `Clothing` (0/1)
   - `Electronics` (0/1)

3. **`days_between`** (Recency Metric)

   - Days since last purchase (reference date: 2024-01-01)
   - Measures customer recency

4. **Normalization**
   - Features scaled to [0,1] range using MinMaxScaler
   - Normalized features: `Age`, `Quantity`, `Price per Unit`, `Total Amount`, `days_between`

---

## 🤖 Clustering Methodology

### Algorithm: K-Means Clustering

**Optimal Cluster Selection:**

- **Method:** Elbow Method (WCSS analysis)
- **Optimal K:** 3 clusters
- **Rationale:** Clear elbow point at k=3, indicating natural groupings

**Features Used for Clustering:**

```python
features = [
    'Age', 'Quantity', 'Price per Unit', 'Total Amount',
    'Gender', 'Beauty', 'Clothing', 'Electronics', 'days_between'
]
```

**Model Configuration:**

- Algorithm: K-Means++
- Random State: 42 (for reproducibility)
- Convergence: Auto

---

## 🎯 Customer Segments Identified

### Cluster 0: Value-Conscious Clothing Shoppers

**Profile:**

- **Dominant Product:** Clothing
- **Spending Pattern:** Lower average transaction value
- **Price Sensitivity:** Prefer lower-priced items
- **Recency:** Less recent purchases
- **Size:** ~33% of customer base

**Marketing Strategy:**

- Seasonal discount campaigns
- Bundle offers on clothing
- Loyalty rewards for repeat purchases
- Value-for-money messaging

---

### Cluster 1: Tech-Savvy Electronics Buyers

**Profile:**

- **Dominant Product:** Electronics
- **Spending Pattern:** Mid-range transaction values
- **Recency:** Most recent purchases
- **Engagement:** Active buyers
- **Size:** ~33% of customer base

**Marketing Strategy:**

- New product launch alerts
- Tech reviews and comparisons
- Early-bird discounts
- Accessory bundle deals

---

### Cluster 2: Premium Beauty Enthusiasts

**Profile:**

- **Dominant Product:** Beauty products
- **Demographics:** Slightly younger, predominantly female
- **Spending Pattern:** Highest average spending
- **Price Preference:** Premium/high-value items
- **Size:** ~34% of customer base

**Marketing Strategy:**

- Exclusive product launches
- Premium brand partnerships
- Personalized recommendations
- VIP customer programs

---

## 📊 Visualization Suite

The analysis includes comprehensive visualizations:

### 1. Cluster Overview Dashboard

- Cluster size distribution (pie chart)
- Age distribution per cluster (violin plots)
- Spending distribution (box plots)
- Product preferences (stacked bars)
- Gender distribution (grouped bars)
- Metrics comparison (normalized bars)

### 2. Business Impact Analysis

- Total revenue contribution per cluster
- Customer count distribution
- Average order value comparison

### 3. Density Analysis

- Contour plots showing cluster boundaries
- Age vs Spending patterns
- Recency vs Spending relationships
- Quantity vs Price behavior

### 4. Statistical Heatmaps

- Normalized feature values per cluster
- Actual (denormalized) values for interpretation

---

## 💼 Business Recommendations

### Cluster 0 (Clothing Shoppers)

1. Implement tiered loyalty program
2. Send targeted email campaigns during sales events
3. Feature customer testimonials
4. Create "value packs" with complementary items

### Cluster 1 (Electronics Buyers)

1. Offer pre-order bonuses for new releases
2. Create tech comparison guides
3. Develop electronics + accessories bundles
4. Maintain regular engagement with product updates

### Cluster 2 (Beauty Enthusiasts)

1. Curate personalized product recommendations
2. Host exclusive beauty workshops
3. Offer gift-with-purchase promotions
4. Create limited-edition premium sets

---

## 🛠️ Technical Requirements

### Python Version

- Python 3.8+

### Core Libraries

```
pandas>=1.3.0
numpy>=1.21.0
matplotlib>=3.4.0
seaborn>=0.11.0
scikit-learn>=0.24.0
scipy>=1.7.0
statsmodels>=0.13.0
```

---

## 🚀 Usage Instructions

### 1. Environment Setup

```bash
# Clone repository
git clone <repository-url>
cd customer-segmentation

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### 2. Running the Analysis

```bash
# Launch Jupyter Notebook
jupyter notebook

# Open project.ipynb and run all cells
```

### 3. Data Requirements

- Ensure `Dataset (1).csv` is in the project root directory
- Update the file path in the notebook if needed:

```python
dataset = pd.read_csv('./Dataset (1).csv')
```

---

## 📈 Project Output

### Generated Artifacts

1. **Cleaned Dataset:** `df_for_clustering` with cluster labels
2. **Visualizations:** 10+ comprehensive plots and dashboards
3. **Summary Statistics:** Detailed cluster profiles
4. **Business Insights:** Actionable recommendations per segment

### Key Metrics Summary

```
================================================================================
                         CLUSTER ANALYSIS SUMMARY
================================================================================
 Cluster  Size  Size %  Avg Age  Avg Spending  Total Revenue  Dominant Product  Gender Split
       0   XXX    XX%      XX.X    €XX.XX        €XXXXX.XX     Clothing         XX% F / XX% M
       1   XXX    XX%      XX.X    €XX.XX        €XXXXX.XX     Electronics      XX% F / XX% M
       2   XXX    XX%      XX.X    €XX.XX        €XXXXX.XX     Beauty           XX% F / XX% M
================================================================================
```

---

## 🔮 Future Enhancements

1. **RFM Analysis:**

   - Current limitation: Single transaction per customer
   - Recommendation: Collect longitudinal data for frequency analysis

2. **Predictive Modeling:**

   - Build classification models to predict cluster membership for new customers
   - Implement churn prediction per segment

3. **Advanced Segmentation:**

   - Explore hierarchical clustering
   - Test DBSCAN for density-based segmentation
   - Implement ensemble clustering methods

4. **Real-time Dashboard:**

   - Create interactive Plotly/Dash dashboard
   - Enable dynamic filtering and exploration

5. **A/B Testing Framework:**
   - Test marketing strategies per cluster
   - Measure campaign effectiveness

---

## 📝 Notes & Limitations

- **Frequency Limitation:** Dataset shows frequency = 1 per customer, limiting traditional RFM analysis
- **Temporal Coverage:** Sales data spans limited time period; January appears incomplete
- **Sample Size:** 1,050 transactions may benefit from larger dataset for more robust clustering
- **Feature Scope:** Additional features (e.g., customer location, payment method) could enhance segmentation

---

## 👤 Author

**Ilias Mazarakis**

- Program: MSc Enterprise Software System Development
- Focus: Customer Analytics & Machine Learning

---

## 📄 License

This project is part of academic coursework.

---

## 🤝 Contributing

For suggestions or improvements:

1. Fork the repository
2. Create a feature branch
3. Submit a pull request with detailed description

---

## 📧 Contact

For questions or collaboration opportunities, please reach out.

---

**Last Updated:** November 2025
