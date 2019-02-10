import numpy as np
import numpy.random as randn
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime


'This is a script on chickpea delivery service'

start=datetime(2015,1,1,0,0)  #The start date is 1st January 2015 at 00:00

rng=pd.date_range(start,periods=700,freq='H')

#The date range starts from the variable above and has 700 rows in periods and the default frequency is in hours

chickpea=pd.DataFrame({'Recipe':np.random.choice(['Chana Masala','Hummus','Shrimp salad','Greek Salad wraps',
                                                 'Roasted Salmon and Smokey greens','Farmy Hummus',
                                                  'Bean Medley Chili','Nutty Orzo and Vegetables',
                                                  'Couscous Chickpea salad',
                                                  'Spinach and garbanzo beans',
                                                  'Roasted Buffalo Chickpea Wraps',
                                                  'Mexican Orzo Salad','Minestrone Soup',
                                                  'Indian spiced roasted chickpeas','Best Bean Salad'],len(rng)),
                       'Volume': np.random.randint(1,30,len(rng)),'Price':10+np.random.randn(len(rng)).round(2),
                       'Restaurant':np.random.choice(['Lakely','Banley','Huwhite','Dewet','Elon','Tusk'
                                                      ,'Leron','Brenlee','Haswer','Klever','Banju',
                                                      'Xaser','Baswer','Falafel of Jones',
                                                      'Rigamarolex', "Benji's cane",'Wendyameat and Oats'
                                                      "Benyar's dish",'Jimey Woo'],len(rng)),
                       'City':np.random.choice(['Bonn','Berlin','Munich','Frankfurt','Bayern','Leipzig',
                                                'Cologne','Hamburg','Postdam','Hanover','Dusseldorf',
                                                'Bremen'],len(rng))}, index=rng)

#For random choice the algorithm choses between 2 or more strings
#randint indicates only random integer numbers can be selected
#len(rng) the column follows the length of the variable rng

print(chickpea)  #print the elaborated data-set

chickpea['Order status']=np.random.choice(['sent','pending','received','rejected'],len(rng))

#we can add a new column to indicate the status of the delivery
print(chickpea)

chickpea.to_csv('chickpea.csv') #Export the dataset in csv format

print(chickpea.describe())

chickpeaplot=chickpea.reset_index(drop=True)

print(chickpeaplot.iloc[150:270].plot.area(stacked=False))

plt.show()

print(chickpeaplot[20:300].plot.scatter(x='Price',y='Volume'))

plt.show()

chickpea1=chickpea.iloc[170:478].cumsum()

print(chickpea1.plot(legend=True))
 
plt.show()

status=chickpea.iloc[25:300].groupby('Order status').size()

print(status)

print(status.plot.bar())

plt.show()

print(chickpea[chickpea.City=='Berlin'])

city=chickpea.iloc[75:650].groupby('City').size()

print(city.plot.bar())

plt.show()

city=chickpea.iloc[175:350].groupby('Restaurant').size()

print(city.plot.bar())

plt.show()