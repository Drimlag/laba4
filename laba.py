import datetime
import os

#import pandas as pd
#
#df = pd.DataFrame({'num_men': [1, 3], 'num_wild': [5, 3]}, index=['test', 'red'])
#print(df)
#
#print(datetime.datetime.now())
try:
    print(os.environ["VAR_1"], "we checked")
except KeyError as e:
    print("an error occurred")
    print(e)

print("Good")