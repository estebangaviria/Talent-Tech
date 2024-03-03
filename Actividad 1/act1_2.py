def string_sort(word = str):
  n = list(set(word.lower().replace(' ', '')))
  n.sort()
  return n 

print(string_sort('Esta es una cadena complicadazzz'))