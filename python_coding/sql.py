import pandas as pd
import sqlite3
mca = pd.DataFrame({ 'Rolno': [1,2,3,4],
                     'Name': ['vishal', 'omkar', 'nitish', 'wasu'],
                      'Age': [21,22,23,24],
                      'Marks':[340,356,387,375]})
print(mca)               
cnn = sqlite3.connect('college.db')
mca.to_sql('student',cnn)

# %load_ext sql
%sql sqlite:///college.db