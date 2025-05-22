import pandas as pd
import numpy as np
import random

np.random.seed(42)

n = 200

majors = ['Business', 'Computer Science', 'Psychology', 'Biology', 'Engineering', 'Economics']
sports = ['Football', 'Basketball', 'Baseball', 'Soccer', 'Tennis', 'Esports']
years = ['Freshman', 'Sophomore', 'Junior', 'Senior']
genders = ['Male', 'Female', 'Other']

data = {
    'student_id': [f"S{i+1:04d}" for i in range(n)],
    'age': np.random.randint(18, 26, n),
    'gender': np.random.choice(genders, n, p=[0.5, 0.45, 0.05]),
    'major': np.random.choice(majors, n),
    'academic_year': np.random.choice(years, n, p=[0.25, 0.25, 0.25, 0.25]),
    'weekly_bets': np.random.poisson(3, n).clip(0, 15),
    'avg_bet_amount': np.round(np.random.normal(20, 10, n).clip(1, 100), 2),
    'favorite_sport': np.random.choice(sports, n),
    'impulsivity_score': np.round(np.random.normal(5, 2, n).clip(1, 10), 1)
}

df = pd.DataFrame(data)
df['total_spent_per_week'] = df['weekly_bets'] * df['avg_bet_amount']

# Save to CSV
df.to_csv('student_sports_betting_data.csv', index=False)
