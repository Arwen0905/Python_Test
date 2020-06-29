import pandas as pd
import numpy as np
import matplotlib.pyplot as plot
import bokeh
url = 'https://www.tpex.org.tw/web/emergingstock/lateststats/new.htm?l=zh-tw'
# data = pd.read_html(url)
url1 = './data/興櫃股票_當日行情new.csv'
data = pd.read_csv(url1)
# df = pd.DataFrame(data)
print(data)

