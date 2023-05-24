import pandas as pd

data = pd.read_csv('titanic-passengers.csv', sep=';', index_col=0, names=['PassengerId', 'Survived', 'Pclass', 'Name', 'Sex', 'Age', 'SibSp', 'Parch', 'Ticket', 'Fare', 'Cabin', 'Embarked'])

live_df = data.loc[data["Survived"] == "Yes"]
live = live_df["Survived"].count()

all_pas = data["Survived"].count()

print(((live * 100) / all_pas).round(2))
