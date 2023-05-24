import pandas as pd

data = pd.read_csv('titanic-passengers.csv', sep=';', index_col=0, names=['PassengerId', 'Survived', 'Pclass', 'Name', 'Sex', 'Age', 'SibSp', 'Parch', 'Ticket', 'Fare', 'Cabin', 'Embarked'])

passenger_1class = data.loc[data["Pclass"] == 1]
kol_1class = passenger_1class["Pclass"].count()

all_pas = data["Pclass"].count()

print(((kol_1class * 100) / all_pas).round(2))
