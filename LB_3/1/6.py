import pandas as pd

data = pd.read_csv('titanic-passengers.csv', sep=';', index_col=0, names=['PassengerId', 'Survived', 'Pclass', 'Name', 'Sex', 'Age', 'SibSp', 'Parch', 'Ticket', 'Fare', 'Cabin', 'Embarked'])

women_df = data.loc[data['Sex'] == 'female']
women_name = pd.Series(women_df["Name"]).str.split(" ")

print(women_name.apply(lambda x: x[2]).mode())
