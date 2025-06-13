import requests
import pandas as pd
import matplotlib.pyplot as plt
import random

# ------------------------------
# Fetch data from API
# ------------------------------
url = "https://jsonplaceholder.typicode.com/users"
response = requests.get(url)

if response.status_code == 200:
    users = response.json()
else:
    print("Failed to fetch data from API.")
    exit()

# ------------------------------
# Load into DataFrame
# ------------------------------
df = pd.DataFrame(users)
df_cleaned = df[['name', 'username', 'email', 'address', 'company']].copy()

# Extract nested city and company names
df_cleaned['city'] = df_cleaned['address'].apply(lambda x: x['city'])
df_cleaned['company'] = df_cleaned['company'].apply(lambda x: x['name'])
df_cleaned.drop('address', axis=1, inplace=True)

# ------------------------------
# Simulate More Users (3x)
# ------------------------------
df_expanded = pd.concat([df_cleaned]*3, ignore_index=True)

# Randomize cities to create variation
city_pool = df_cleaned['city'].tolist()
df_expanded['city'] = df_expanded['city'].apply(lambda x: random.choice(city_pool))

# Optional: Shuffle the data
df_expanded = df_expanded.sample(frac=1).reset_index(drop=True)

# ------------------------------
# Visualize Users per City
# ------------------------------
city_counts = df_expanded['city'].value_counts()

plt.figure(figsize=(10, 5))
city_counts.plot(kind='bar', color='skyblue')
plt.title("Number of Users per City (Simulated)")
plt.xlabel("City")
plt.ylabel("User Count")
plt.tight_layout()

# Save chart for Task 2 use too
plt.savefig("bar_chart.png")
plt.show()

# ------------------------------
# Save Cleaned Data (Optional)
# ------------------------------
df_expanded.to_csv("simulated_user_data.csv", index=False)