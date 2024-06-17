import socket 
import serverFunctions as s

host = '127.0.0.1'
port = 9000

try:
  server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
  print('Socket successfully created')
  server.bind((host,port))
  server.listen()
  print(f'Server starded in {host}:{port}')
except socket.error as err:
  print(f'Socket creation failed with error {err}')

print('Waiting for client request ...')
connection, address = server.accept()
print(f'Conected in {address}')

while True:
  data = connection.recv(1024)
  data = data.decode()

  dataList = data.split(',')
  option = int(dataList[0])

  if data == 'end':
    print('Connection is over')
    break

  if option == 1:
    s.Create(dataList[1],dataList[2],dataList[3])
  elif option == 2:
    pass
  elif option == 3:
    pass
  elif option == 4:
    pass
  elif option ==  5:
    pass
  

