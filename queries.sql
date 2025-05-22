-- 1. High-Risk Bettors View
CREATE VIEW High_Risk_Bettors AS
SELECT *
FROM betting_data
WHERE weekly_bets > 6 OR avg_bet_amount > 50;

-- 2. Average Bet by Major
CREATE VIEW Avg_Bet_By_Major AS
SELECT major, AVG(avg_bet_amount) AS Avg_Bet_Amount
FROM betting_data
GROUP BY major;

-- 3. Impulsivity Score by Betting Style
CREATE VIEW Impulsivity_By_Style AS
SELECT
  CASE
    WHEN weekly_bets > 6 OR avg_bet_amount > 50 THEN 'High-Risk'
    WHEN weekly_bets >= 3 THEN 'Regular'
    ELSE 'Casual'
  END AS betting_style,
  AVG(impulsivity_score) AS Avg_Impulsivity
FROM betting_data
GROUP BY betting_style;

-- 4. Students by Year & Gender
CREATE VIEW Student_Count_By_Year_Gender AS
SELECT academic_year, gender, COUNT(*) AS student_count
FROM betting_data
GROUP BY academic_year, gender;

-- 5. Most Popular Sports
CREATE VIEW Favorite_Sport_Counts AS
SELECT favorite_sport, COUNT(*) AS sport_count
FROM betting_data
GROUP BY favorite_sport
ORDER BY sport_count DESC;

-- 6. Total Spent per Week by Betting Style
CREATE VIEW Total_Spent_By_Style AS
SELECT
  CASE
    WHEN weekly_bets > 6 OR avg_bet_amount > 50 THEN 'High-Risk'
    WHEN weekly_bets >= 3 THEN 'Regular'
    ELSE 'Casual'
  END AS betting_style,
  AVG(total_spent_per_week) AS Avg_Spent
FROM betting_data
GROUP BY betting_style;

-- 7. Top 5 Majors by Average Weekly Spend
CREATE VIEW Top_Spending_Majors AS
SELECT major, AVG(total_spent_per_week) AS Avg_Weekly_Spend
FROM betting_data
GROUP BY major
ORDER BY Avg_Weekly_Spend DESC
LIMIT 5;

-- 8. Weekly Bets by Academic Year
CREATE VIEW Weekly_Bets_By_Year AS
SELECT academic_year, AVG(weekly_bets) AS Avg_Weekly_Bets
FROM betting_data
GROUP BY academic_year
ORDER BY FIELD(academic_year, 'Freshman', 'Sophomore', 'Junior', 'Senior')
