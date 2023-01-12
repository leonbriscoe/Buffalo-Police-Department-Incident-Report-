# PART 1 OF PROJECT 


def gen_dictionary(data, key):
  acc = {}
  for index in data:
    if key in index:
      v = index[key]
      acc[v] = 0
  return acc 

def total_matches(lod,k,v):
  acc = 0
  for index in lod:
    value = index[k]
    if(value == v):
      acc = acc + 1 
  return acc 


def total_matches_specific(lod,k,v,k2,v2):
  acc = 0
  for index in lod:
    value = index[k]
    if (index[k2] == v2 and value == v):
      acc += 1
  return acc 


def remove_min(data, min_value):
  dict = {}
  for index in data:
    value = data[index]
    if value > min_value:
      dict[index] = value
  return dict 