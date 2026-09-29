# Project 4: BCA Fresher Job Scam Detector
# By Sakshi Pradhan - BCA Fresher
# Date: 2024 - My 4th Project
# I collected 100 jobs manually from LinkedIn, Indeed, Naukri

import pandas as pd
import matplotlib.pyplot as plt

# Load my data - 100 jobs I collected
df = pd.read_excel('100_Jobs_Data.xlsx')

print("Total jobs I collected:", len(df))

# Count Real vs Scam - My finding
real = len(df[df['Real_or_Scam'] == 'Real'])
scam = len(df[df['Real_or_Scam'] != 'Real'])

print("Real jobs:", real)
print("Scam jobs:", scam)
print("Scam percentage:", (scam/100)*100, "%")

# My signature RED-GREEN logic - I learned from Project 2
# RED = SCAM (Danger), GREEN = Real

# Chart 1 - Real vs Scam pie chart
plt.figure(figsize=(8,6))
plt.pie([real, scam], labels=['Real', 'SCAM'], colors=['green', 'red'], autopct='%1.0f%%')
plt.title('Real vs SCAM Jobs - My Project 4')
plt.savefig('Chart1_Real_vs_Scam.png')
plt.show()

# Chart 2 - Top skills
# I want to know what companies want
skills = []
for i in range(len(df)):
    if str(df.loc[i, 'Skill_1']) != '' and str(df.loc[i, 'Skill_1']) != 'nan':
        skills.append(df.loc[i, 'Skill_1'])
    if str(df.loc[i, 'Skill_2']) != '' and str(df.loc[i, 'Skill_2']) != 'nan':
        skills.append(df.loc[i, 'Skill_2'])

# Count skills
from collections import Counter
c = Counter(skills)
print("Top skills:", c.most_common(5))

# Bar chart for skills
plt.figure(figsize=(10,6))
plt.bar(c.keys(), c.values(), color='blue')
plt.title('Top Skills for BCA Fresher')
plt.xticks(rotation=20)
plt.savefig('Chart3_Top_Skills.png')
plt.show()

# My learning from this project
print("What I learned:")
print("1. 18% jobs are SCAM asking money")
print("2. Excel and SQL most demanded")
print("3. Real salary is 18k-25k not 50k")
