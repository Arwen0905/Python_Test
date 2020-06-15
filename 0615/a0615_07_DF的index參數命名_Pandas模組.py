import pandas as pd
info = {'種族':['騎士','法師','女神','盜賊'],
        '武器':['聖劍','法仗','法器','暗器'],
        '金錢':[3000,1000,500,1500]
        }
title = ["物理","法術","補師","遠程"]
user = pd.DataFrame(info,index=title)
print(user)