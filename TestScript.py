# Script for testing purposes

import pandas

data = pandas.read_csv('Exported_titanic_2.csv')
pd = pandas.DataFrame(data)



pd['Fare'] = pd['Fare']*10000
pd.to_csv('Exported_final.csv',index=False)