import pandas as pd
cities = {'country':['China','Japan','Singapore'],
          'town':['Beijin','Tokyo','Singapore'],
          'Population':[2000,1600,600]
          }
citydf=pd.DataFrame(cities)
print(citydf)
    