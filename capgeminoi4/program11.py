# # import pandas as pd

# # data=[
# #     {'name': 'John', 'age': 28, 'city': 'New York'},
# #     {'name': 'Anna', 'age': 24, 'city': 'Paris'},
# #     {'name': 'Peter', 'age': 35, 'city': 'Berlin'},
# # ]
# # df=pd.DataFrame(data)
# # print(df)
# import pandas as pd
# data={
#     'name':["Shanmuk reddy","Krishna","Sandeep"],
#     'age':[28,24,35],
#     'city':['New York','Paris','Berlin']
# }
# df=pd.DataFrame(data)
# print(df.head())

import pandas as pd
df=pd.read_csv('people-100.csv')
print(df.head())
