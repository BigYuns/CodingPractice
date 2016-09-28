import csv

def csvReader(file): 
  f = open(file)
  csv_f = csv.reader(f) 
  csv_f.next()
  return csv_f

def adjacenyList(csv1, csv2): 
  if csv1 == None or csv2 ==None: 
    return None 
  
  employees = csvReader(csv1)
  friendships = csvReader(csv2)
  
  adjacent_list = {}
  
  for row in employees: 
    adjacent_list[row[0]] = None 
    
  for r in friendships: 
    if r[0] in adjacent_list.keys(): 
      if adjacent_list[r[0]]==None: 
        adjacent_list[r[0]]=[]
      adjacent_list[r[0]].append(r[1])
  return adjacent_list 

if __name__ == '__main__':
  print adjacenyList('employees.csv', 'friendships.csv') 