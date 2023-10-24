'''
json.dumps() - is used to python object is converted into json object
    serilization
    pickling

json.loads () - is used to json object is converted into python object
    deserilization
    unpikling



'''




import pandas as pd

# data = {
#   "calories": [420, 380, 390],
#   "duration": [50, 40, 45]
# }
#
# #load data into a DataFrame object:
# df = pd.DataFrame(data)
#
# print(df)

# val = ['gopi','surya','kamali','prabu','sakara']
#
# va = pd.Series(val)
#
# print(va)
#
# a = [1, 7, 2]
#
# myvar = pd.Series(a)
#
# print(myvar)
import pandas as pd

dic = {
    'NAME' : ['GOPI','SURYA', 'SAKARA', 'KAMALI', 'KARUPPU'],

    'AGE'  : [24, 22, 23, 24, 26],
    'city' : 'salem', 'dharmapuri', 'salem', 'salem', 'karur']

}

out = pd.DataFrame(dic)

print(out)