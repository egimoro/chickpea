import numpy as np
import numpy.random as randn
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime


'This is a script on chickpea delivery service'

start=datetime(2015,1,1,0,0)

rng=pd.date_range(start,periods=700,freq='H')

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

print(chickpea)

chickpea['Order status']=np.random.choice(['sent','pending','received','rejected'],len(rng))

print(chickpea)

chickpea.to_csv('chickpea.csv')

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
