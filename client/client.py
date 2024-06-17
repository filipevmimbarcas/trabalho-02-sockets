import socket
import clientFunctions as c

host = '127.0.0.1'
port = 9000

client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect((host,port))

while True:
  print('\t\tPrograma')
  print('[1] Incluir dados ')
  print('[2] Listar dados ')
  print('[3] Pesquisar dados ')
  print('[4] Excluir dados')
  print('[5] Finalizar')
  option = input('Opção >> ')

  if option.isdigit():
    option = int(option)
    if option == 1:
      data = c.Create(option)
      client.send(data.encode())
    elif option == 2:
      pass
    elif option == 3:
      pass
    elif option == 4:
      pass
    elif option == 5:
      print('Saindo do programa.')
      client.send('end'.encode())
      client.close()
      break
    else:
      print('Alternativa não existe.')
  else:
    print('Opção invalida!')