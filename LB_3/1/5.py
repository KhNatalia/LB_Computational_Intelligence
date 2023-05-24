import pandas as pd

data = pd.read_csv('titanic-passengers.csv', sep=';', index_col=0, names=['PassengerId', 'Survived', 'Pclass', 'Name', 'Sex', 'Age', 'SibSp', 'Parch', 'Ticket', 'Fare', 'Cabin', 'Embarked'])

print(data['SibSp'].corr(data['Parch'], method='pearson'))
