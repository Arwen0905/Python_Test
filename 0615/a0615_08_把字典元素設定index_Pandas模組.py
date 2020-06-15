import pandas as pd
cities = {'country':['China','Japan','Singapore'],
          'town':['Beijin','Tokyo','Singapore'],
          'Population':[2000,1600,600]
          }
citydf=pd.DataFrame(cities)
print(citydf)
print('==============================================')

cities = {'country':['China','Japan','Singapore'],
          'town':['Beijin','Tokyo','Singapore'],
          'Population':[2000,1600,600]
          }
citydf=pd.DataFrame(cities,columns=["town","population"],
                    index=cities["country"])
print(citydf)


'''
                town population
China         Beijin        NaN
Japan          Tokyo        NaN
Singapore  Singapore        NaN
'''