import numpy as np
import pandas as pd
csv_file=r"C:\Users\Suryakant\Downloads\movies.csv"
csv_file_=r"C:\Users\Suryakant\Downloads\ipl-matches.csv"
ipl=pd.read_csv(csv_file_)
movies=pd.read_csv(csv_file)
ipl['ID']=ipl['ID'].astype('int32')
print(ipl.info)