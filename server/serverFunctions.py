import os 

fileName = 'file.txt'

def ValidateFile(file)->bool:
  if os.path.exists(file):
    return True
  else:
    return False

def GenerateId()->int:
  if not ValidateFile(fileName):
    return 1
  else:
    with open(fileName,'r') as file:
      lines = file.readlines()
      counter = int(lines[-1][0]) + 1
    return counter
  

def Create(name ,vendor, model):
  with open(fileName,'a',encoding='utf8') as file:
    file.write(f'{name},{vendor},{model}\n')



def GetAll():
  pass

def GetItem():
  pass

def DeleteByID():
  pass