import pandas as pd

data = pd.read_csv('titanic-passengers.csv', sep=';', index_col=0, names=['PassengerId', 'Survived', 'Pclass', 'Name', 'Sex', 'Age', 'SibSp', 'Parch', 'Ticket', 'Fare', 'Cabin', 'Embarked'])

women_df = data.loc[data['Sex'] == 'female']
men_df = data.loc[data['Sex'] == 'male']

print(women_df["Sex"].count(), men_df["Sex"].count())
print(data)
