import requests
import pandas as pd

# Step 1: Fetch data from API
url = "https://jsonplaceholder.typicode.com/users"
response = requests.get(url)

if response.status_code != 200:
    print("Failed to fetch data:", response.status_code)
    exit()

data = response.json()
print("✅ Data fetched successfully!")

# Step 2: Process the data
processed_users = []

for user in data:
    name = user.get('name', 'Unknown')
    username = user.get('username', 'N/A')
    email = user.get('email', 'N/A')
    city = user.get('address', {}).get('city', 'N/A')
    company = user.get('company', {}).get('name', 'N/A')

    processed_users.append({
        "Name": name,
        "Username": username,
        "Email": email,
        "City": city,
        "Company": company
    })

# Step 3: Convert to DataFrame
df = pd.DataFrame(processed_users)

# Preview the processed data
print("\n📊 Cleaned User Data:")
print(df)
import matplotlib.pyplot as plt
import seaborn as sns

# Step 4: Visualize the data
plt.figure(figsize=(10, 6))
city_counts = df['City'].value_counts()
sns.barplot(x=city_counts.index, y=city_counts.values, palette="coolwarm")

plt.title("Number of Users per City", fontsize=16)
plt.xlabel("City", fontsize=12)
plt.ylabel("Number of Users", fontsize=12)
plt.xticks(rotation=45)
plt.tight_layout()

# Show the plot
plt.show()


# Step 4: Summary for Visualization
city_counts = df['City'].value_counts()
print("\n🏙️ Users per City:")
print(city_counts)