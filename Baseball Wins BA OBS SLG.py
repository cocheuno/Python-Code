import pandas as pd  # Used for data manipulation and analysis
import matplotlib.pyplot as plt  # Used for creating static, interactive, and animated visualizations
import statsmodels.api as sm  # Provides classes and functions for the estimation of many different statistical models

# Additional imports for handling file paths
from pathlib import Path  # Used for easier file path manipulation

# Define the path to the Excel file
file_path = Path("C:/Users/caronet/Downloads/baseball.xlsx")

# Read the Excel file into a pandas DataFrame
df = pd.read_excel(file_path)

# Display the first few rows of the DataFrame to ensure it's loaded correctly
print(df.head())

# Calculate the difference between 'Runs Scored' and 'Runs Allowed'
df['Run_Difference'] = df['Runs Scored'] - df['Runs Allowed']

# Perform the linear regression using 'Wins' as the dependent variable and 'Run Difference' as the independent variable
X1 = sm.add_constant(df['Run_Difference'])  # Adds a constant term to the predictor
Y1 = df['Wins']

# Fit the regression model
model1 = sm.OLS(Y1, X1).fit()

# Plotting
plt.figure(figsize=(10, 6))
plt.scatter(df['Run_Difference'], df['Wins'], alpha=0.5)  # Plot the raw data
plt.plot(df['Run_Difference'], model1.predict(X1), color='red')  # Plot the regression line
plt.title('Wins vs Run Difference with Linear Regression Line')
plt.xlabel('Run Difference (Runs Scored - Runs Allowed)')
plt.ylabel('Wins')
plt.text(0.05, 0.95, f'R-squared: {model1.rsquared:.2f}', transform=plt.gca().transAxes)  # Show R^2 value on the plot
plt.show()

# Perform the second linear regression using 'Run Difference' as the dependent variable and 'Team Batting Average' as the independent variable
X2 = sm.add_constant(df['Team Batting Average'])
Y2 = df['Run_Difference']

# Fit the regression model
model2 = sm.OLS(Y2, X2).fit()

# Plotting
plt.figure(figsize=(10, 6))
plt.scatter(df['Team Batting Average'], df['Run_Difference'], alpha=0.5)  # Plot the raw data
plt.plot(df['Team Batting Average'], model2.predict(X2), color='red')  # Plot the regression line
plt.title('Run Difference vs Team Batting Average with Linear Regression Line')
plt.xlabel('Team Batting Average')
plt.ylabel('Run Difference (Runs Scored - Runs Allowed)')
plt.text(0.05, 0.95, f'R-squared: {model2.rsquared:.2f}', transform=plt.gca().transAxes)  # Show R^2 value on the plot
plt.show()

# Prepare the data for multiple regression
X3 = df[['OBP', 'SLG']]  # Independent variables
X3 = sm.add_constant(X3)  # Add a constant term to the model
Y3 = df['Run_Difference']  # Dependent variable

# Fit the multiple regression model
model3 = sm.OLS(Y3, X3).fit()

# Print out the regression statistics
print(model3.summary())

# Explanation of the statistics will be provided in the comments below the printed summary

