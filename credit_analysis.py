# Simple Credit Data Analysis

import csv

# Step 1: Load Data
data = []
with open("credit_data.csv", "r") as f:
    reader = csv.DictReader(f)
    for row in reader:
        data.append(row)

# Step 2: Basic Info
print(f"Total clients: {len(data)}")

# Step 3: Count Defaults
default_count = sum(int(row['DEFAULT']) for row in data)
no_default_count = len(data) - default_count
print(f"Clients who defaulted: {default_count}")
print(f"Clients who did not default: {no_default_count}")
print(f"Percentage of clients who defaulted: {round(default_count/len(data)*100, 2)}%")

# Step 4: Average Credit Limit by Default
default_limits = [int(row['LIMIT_BAL']) for row in data if row['DEFAULT']=='1']
no_default_limits = [int(row['LIMIT_BAL']) for row in data if row['DEFAULT']=='0']

avg_default = sum(default_limits)/len(default_limits) if default_limits else 0
avg_no_default = sum(no_default_limits)/len(no_default_limits) if no_default_limits else 0

print(f"Average credit limit (defaulted): {avg_default}")
print(f"Average credit limit (non-defaulted): {avg_no_default}")

# Step 5: Age Summary
ages = [int(row['AGE']) for row in data]
avg_age = sum(ages)/len(ages)
print(f"Average age of clients: {round(avg_age,2)}")
