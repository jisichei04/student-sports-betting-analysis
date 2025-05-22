import pandas as pd

df = pd.read_csv("C:/Users/Owner/Downloads/Parlay-Project/student_sports_betting_data.csv")  # Adjust path if needed
df.head()

df.columns = df.columns.str.lower().str.replace(" ", "_")
df.isnull().sum()
df.describe()
df['weekly_bets'] = df['weekly_bets'].clip(0, 15)
df['avg_bet_amount'] = df['avg_bet_amount'].clip(1, 100)
df['total_spent_per_week'] = df['weekly_bets'] * df['avg_bet_amount']
df.to_csv("C:/Users/Owner/Downloads/Parlay-Project/finalized_student_sports_betting_data.csv", index=False)
