import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
detail=r"C:\Users\Suryakant\Downloads\30_random_names_ages.csv"
detail_=pd.read_csv(detail)
a=detail_[(detail_['Age']>=30) & (detail_['Age']<40)]
a.plot(kind='bar')
plt.show()