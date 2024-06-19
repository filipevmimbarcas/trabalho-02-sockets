import os 
import pprint

fileName = 'file.txt'

def GenerateId():
  if not os.path.exists(fileName):
    print(f'The {fileName} does not exist, creating file...\n')
    return 1
  else:
    print(f'The {fileName} already exists')
    file = open(fileName)
    lines = file.readlines()
    file.close()
    counter = len(lines) + 1
    return counter

#Insere um dipositivo
def Create(name,vendor,model):
  with open(fileName,'a',encoding='utf8') as file:
    id = GenerateId()
    file.write(f'{id};{name};{vendor};{model}\n')
    print('Asset registered successfully')
    line = {}
    line.update({'id': id})
    line.update({'name': name})
    line.update({'vendor': vendor})
    line.update({'model': model})
    print(line)

