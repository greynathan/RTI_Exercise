import sqlite3 
import pandas as pd
import plotly.express as px
import plotly

#3. IMPORTING TABLE 
#connecting to the database
conn = sqlite3.connect('exercise01.sqlite')

#creating a Pandas Dataframe for analysis and web app using the flat_records table from the DB
df = pd.read_sql_query("SELECT * FROM 'flat_records'", conn)
df = df.iloc[: , 1:]

#4. ANALYSIS 

#calculating the total number of people based on the amount of rows 
total_people = df.shape[0]

#creating one way frequency dataframes using value_count to 
# calculate the frequency of each option
work_freq = df['workclass'].value_counts().to_frame()
ed_freq = df['education'].value_counts().to_frame()
marital_freq = df['marital_status'].value_counts().to_frame()
occ_freq = df['occupation'].value_counts().to_frame()
relation_freq = df['relationship'].value_counts().to_frame()
race_freq = df['race'].value_counts().to_frame()
country_freq = df['country'].value_counts().to_frame()
fifty_freq = df['over_50k'].value_counts().to_frame()
sex_freq = df['sex'].value_counts().to_frame()

#creating two way frequency dataframes using crosstab to compare two traits
sex_50k = pd.crosstab(index=df['sex'], columns=df['over_50k'])
sex_ed = pd.crosstab(index=df['sex'], columns=df['education'])

#7. GRAPHS
#creating graphs
sex_fig = px.bar(sex_freq, x = ['male', 'female'], y = "sex")
sex_fig.write_image("static/sex_freq.jpg")
work_fig = px.bar(work_freq, x = ['Private', 'Self Employed not Inc', 'Local Gov', "?", 'State Gov', 'Self Employeed Inc', 'Federal Gov', 'Without Pay', 'Never Worked' ], y = "workclass")
work_fig.write_image("static/work_freq.jpg")
ed_fig = px.bar(ed_freq, x = ['HS grad', 'Some College', 'Bachelors', "Masters", 'Associate Vocation', '11th', 'Associate Academic', '10th', '7-8th', 'Professional School', '9th', '12th', 'Doctorate', '5-6th', '1-4th', 'Preschool' ], y = "education")
ed_fig.write_image("static/ed_freq.jpg")
marital_fig = px.bar(marital_freq, x = ['Married Civ Spouse', 'Never Married', 'Divorced', "Separated", 'Widowed', 'Married Spouse Absent', 'Married AF Spouse'], y = "marital_status")
marital_fig.write_image("static/marital_freq.jpg")
relation_fig = px.bar(relation_freq, x = ['Husband', 'No Family', 'Only child', "Unmarried", 'Wife', 'Other Relative'], y = "relationship")
relation_fig.write_image("static/relation_freq.jpg")
occ_fig = px.bar(occ_freq, x = ['Professional Specialty', 'Craft Repair', 'Executive Managerial', "Admin Clerical", 'Sales', 'Other Services', 'Machine Operation-Inspector', '?', 'Tranport-Moving', 'Handlers-Cleaners', 'Farming-Fishing', 'Tech-Support','Protective-Service','Private-House-Service','Armed-Forces'], y = "occupation")
occ_fig.write_image("static/occ_freq.jpg")
race_fig = px.bar(race_freq, x = ['White', 'Black', 'Asian Pacific Islander', "American Indian Eskimo", 'Other'], y = "race")
race_fig.write_image("static/race_freq.jpg")
fifty_fig = px.bar(fifty_freq, x = ['Under', 'Over'], y = "over_50k")
fifty_fig.write_image("static/fifty_freq.jpg")





