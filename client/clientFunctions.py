
def Create(num)-> str:
  name = input('Nome: ')
  vendor = input('Fabricante: ')
  model = input ('Modelo: ')
  option = str(num)
  data = f'{option},{name},{vendor},{model}'
  return data
