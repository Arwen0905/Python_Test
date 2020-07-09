from bs4 import BeautifulSoup
import requests
import os
from urllib.request import urlretrieve
import re
import pandas as pd
import numpy as np
import glob
import matplotlib.pyplot as plt


# p = ["107年",["春天",["三維","三維","三維"]],"108年",["夏天",["三維","三維","三維"]],
#        "109年",["秋天",["三維","三維","三維"]]]
p = {"年":{"一月":{"日":"三維"},"二月":{"日":"三維"}}}

df = pd.DataFrame(p)
# df = pd.Panel(p) #出錯
print(df)

# p.ix[:,:,'add'] = pd.DataFrame(np.random.randn(p.major_axis.shape[0],
#                                                 p.items.shape[0]),index=p.major_axis,
#                                 columns=p.items)

