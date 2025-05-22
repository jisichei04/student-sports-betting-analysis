import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("C:/Users/Owner/Downloads/Parlay-Project/finalized_student_sports_betting_data.csv")


#the betting style based on weekly bets and average bet amount
def label_betting_style(row):
    if row['weekly_bets'] > 6 or row['avg_bet_amount'] > 50:
        return 'High-Risk'   # Students who bet a lot or bet large amounts
    elif row['weekly_bets'] >= 3:
        return 'Regular'     # Students who bet a few times each week
    else:
        return 'Casual'      # Students who barely bet

df['betting_style'] = df.apply(label_betting_style, axis=1)

#students are in each group
print(" Number of Students by Betting Style:")
print(df['betting_style'].value_counts())

#pie chart showing betting distribution
df['betting_style'].value_counts().plot(kind='pie', autopct='%1.1f%%', startangle=90)
plt.title('Betting Style Distribution')
plt.ylabel('')  # Hide the y-axis label
plt.show()

#impulsivity score in each group
print("\n Average Impulsivity Score by Betting Style:")
print(df.groupby('betting_style')['impulsivity_score'].mean().round(2))

#majors bet distribution
print("\n Average Bet Amount by Major:")
print(df.groupby('major')['avg_bet_amount'].mean().round(2).sort_values(ascending=False))

high_risk_sport = df[df['betting_style'] == 'High-Risk']
percent_high_risk = (high_risk_sport['favorite_sport'].value_counts() / df['favorite_sport'].value_counts() * 100).round(1)

print("\n Percent of High-Risk Students by Favorite Sport:")
print(percent_high_risk.sort_values(ascending=False))

#impulsivity score across different betting styles
sns.boxplot(data=df, x='betting_style', y='impulsivity_score')
plt.title('Impulsivity Score by Betting Style')
plt.xlabel('Betting Style')
plt.ylabel('Impulsivity Score')
plt.show()
