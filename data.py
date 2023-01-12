# PROJECT 2 


def list_dic_gen(listA, listB):
  acc = []
  length = len(listA)
  for index in listB:
    dic = {}
    for i in range(length):
      dic.update({listA[i]:index[i]})
    acc.append(dic)
  return acc 


# print(list_dic_gen(['One','Two'], [['First','Second']]))
# print(list_dic_gen(['Second'], [['One'],['Third Fourth']]))


import csv 
def read_values(file_name):
    with open(file_name, "r") as f:
      reader=csv.reader(f)
      next(reader)
      acc=[]
      for i in reader:
        acc.append(i)

    return acc 


# print(read_values("pre.csv"))
# print(read_values("fiction.csv"))





  
def list_gen(dicts, keys):
    acc = []
    for i in dicts:
        temp = []
        for k in keys:
            temp.append(i[k])
        acc.append(temp)
    return acc

print(list_gen([{'Used Key': 'Data', 'Unused Keys' : 'More Data'}],

['Used Key']))





def write_values(data, file_name):
  with open(file_name, "a") as f:
    for i in data:
      writer = csv.writer(f)
      writer.writerow(i)


# print(write_values([['Something Meaninful'], ['Look a , comma']],
# "emp.csv"))
# print(write_values([ ['2021','NY'] ], "pretend.csv"))

# PROJECT 3 


def split_date(x):
  acc = [ ]
  y = x.split("-")
  year = int(y[0])
  month = int(y[1])
  acc.append(year)
  acc.append(month)
  return acc 


def fix_data(lod,k):
  for i in lod:
    val = i[k]
    temp = split_date(val)
    i['year'] = temp[0]
    i['month'] = temp[1]
  return lod 

import json 
import urllib.request
def json_loader(url):
  response = urllib.request.urlopen(url)
  cont = response.read().decode()
  cont = json.loads(cont)
  return cont 
  

def make_values_numeric(lst, dic):
  for i in lst:
    if i in dic:
      dic[i] = int(dic[i])

  return dic


def save_data(lod, keys, filename):
    with open(filename, "w") as f:
        writer = csv.writer(f)
        writer.writerow(keys)
        for dict in lod:
            acc = []
            for key in keys:
                acc.append(dict[key])
            writer.writerow(acc)

def load_data(filename):
  acc = []
  with open(filename, "r", ) as f:
    csvreader = csv.DictReader(f)
    for row in csvreader:
      acc.append(row)
    return acc