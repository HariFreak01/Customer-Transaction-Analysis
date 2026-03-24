import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("transactions.csv")
df.head()
df.info()
df.describe()
# Check missing values
df.isnull().sum()

# Drop or fill missing values
df = df.dropna()

# Convert date column
df['date'] = pd.to_datetime(df['date'])
df['month'] = df['date'].dt.month
df['day'] = df['date'].dt.day
df['amount'].sum()
df.groupby('category')['amount'].sum().sort_values().plot(kind='bar')
plt.show()
df.groupby('month')['amount'].sum().plot()
plt.show()
customer_spending = df.groupby('customer_id')['amount'].sum()
customer_spending.sort_values(ascending=False).head()

# Simple anomaly detection
threshold = df['amount'].mean() + 3*df['amount'].std()

anomalies = df[df['amount'] > threshold]
anomalies
