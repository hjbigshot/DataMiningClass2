import pandas as pd

data = pd.read_csv('D:\\train.csv', index_col='PassengerId')
data.fillna(-1, inplace=True)
data['Survived'][data['Survived'] == 0] = 'dead'
data['Survived'][data['Survived'] == 1] = 'live'
data['Relatives'] = data['SibSp'] + data['Parch']
data['Relatives'][data['Relatives'] != 0] = 'haskins'
data['Relatives'][data['Relatives'] == 0] = 'nokins'

for i in data.index:
    if data.loc[i, 'Age'] < 0:
        data.loc[i, 'Age'] = ''
    elif data.loc[i, 'Age'] < 18:
        data.loc[i, 'Age'] = 'teen'
    elif data.loc[i, 'Age'] < 55:
        data.loc[i, 'Age'] = 'adult'
    else:
        data.loc[i, 'Age'] = 'old'

data = data[['Survived', 'Pclass', 'Sex', 'Age', 'Relatives']]
data.to_csv('D:\\pre.tab', sep='\t')
