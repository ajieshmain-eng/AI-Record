# Experiment 7: Data Cleaning and Exploratory Data Analysis Using Pandas

import pandas as pd

data = {
    "Name": ["Anitha", "Bala", "Chitra", "Dinesh", "Ezhil", "Fathima"],
    "Department": ["CSE", "CSE", "ECE", "CSE", "ECE", "CSE"],
    "Attendance": [92, 85, None, 88, 95, 90],
    "Mark": [86, 91, 78, None, 95, 82]
}

df = pd.DataFrame(data)

print("--- Original Dataset ---")
print(df)

print("\nMissing Values:")
print(df.isnull().sum())

# Missing value treatment
df["Attendance"] = df["Attendance"].fillna(df["Attendance"].mean())
df["Mark"] = df["Mark"].fillna(df["Mark"].mean())

# Remove duplicate records
df = df.drop_duplicates()

print("\n--- Cleaned Dataset ---")
print(df)

print("\n--- Descriptive Statistics ---")
print(df.describe())

print("\n--- Department-wise Average Marks ---")
print(df.groupby("Department")["Mark"].mean().round(2))

print("\n--- EDA Summary ---")
print("Highest Mark :", df["Mark"].max())
print("Lowest Mark :", df["Mark"].min())
print("Average Mark :", round(df["Mark"].mean(), 2))
print("Average Attendance :", round(df["Attendance"].mean(), 2))


# Additional Google Colab version from the manual:
# The manual's %%writefile students1.csv cell is represented here as
# ordinary Python file-writing code so this .py file can run outside Colab.

csv_content = """Name,Department,Attendance,Mark
Asha,CSE,90,88
Bala,CSE,80,76
Charan,ECE,,92
Divya,ECE,95,
Eshan,CSE,85,84
"""

with open("students1.csv", "w", newline="") as file:
    file.write(csv_content)

# Choose the CSV file to analyze
filename = "students1.csv"

# Load the CSV file
df = pd.read_csv(filename)

print("--- Original Dataset ---")
print(df)

print("\nMissing Values:")
print(df.isnull().sum())

# Fill missing values with column means
df["Attendance"] = df["Attendance"].fillna(df["Attendance"].mean())
df["Mark"] = df["Mark"].fillna(df["Mark"].mean())

# Remove duplicate records
df = df.drop_duplicates()

print("\n--- Cleaned Dataset ---")
print(df)

print("\n--- Descriptive Statistics ---")
print(df.describe())

print("\n--- Department-wise Average Marks ---")
print(df.groupby("Department")["Mark"].mean().round(2))

print("\n--- EDA Summary ---")
print("Highest Mark :", df["Mark"].max())
print("Lowest Mark :", df["Mark"].min())
print("Average Mark :", round(df["Mark"].mean(), 2))
print("Average Attendance :", round(df["Attendance"].mean(), 2))
