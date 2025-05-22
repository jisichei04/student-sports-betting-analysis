import pandas as pd
import matplotlib.pyplot as plt

# Load cleaned data
df = pd.read_csv("C:/Users/Owner/Downloads/Parlay-Project/finalized_student_sports_betting_data.csv")

#Distributing the Age 
plt.hist(df['age'], bins=8, edgecolor='black')
plt.title('Age Distribution')
plt.xlabel('Age')
plt.ylabel('Count')
plt.show()

#Score Distribution
plt.hist(df['impulsivity_score'], bins=10, edgecolor='black')
plt.title('Impulsivity Score Distribution')
plt.xlabel('Impulsivity Score')
plt.ylabel('Count')
plt.show()

#Bet Amount Distribution
plt.hist(df['avg_bet_amount'], bins=20, edgecolor='black')
plt.title('Avg Bet Amount Distribution')
plt.xlabel('Avg Bet ($)')
plt.ylabel('Count')
plt.show()

#Bet Amount vs Score Distribution
plt.scatter(df['impulsivity_score'], df['weekly_bets'], alpha=0.6)
plt.title('Weekly Bets vs Impulsivity Score')
plt.xlabel('Impulsivity Score')
plt.ylabel('Weekly Bets')
plt.grid(True)
plt.show()

#Gender Distribution
df.boxplot(column='avg_bet_amount', by='gender')
plt.title('Avg Bet Amount by Gender')
plt.suptitle('')
plt.xlabel('Gender')
plt.ylabel('Avg Bet Amount ($)')
plt.show()

#Popularity based on Sports
sport_counts = df['favorite_sport'].value_counts()
sport_counts.plot(kind='barh')
plt.title('Most Popular Sports for Betting')
plt.xlabel('Number of Students')
plt.ylabel('Sport')
plt.show()

#Academic Year Summary
print(df.groupby('academic_year')[['weekly_bets', 'avg_bet_amount', 'impulsivity_score']].mean().round(2))
