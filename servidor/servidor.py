import socket
import funcoesServidor as fs

host = '127.0.0.1'
port = 9000

try:
    servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print('Socket criado com sucesso')
    servidor.bind((host, port))
    servidor.listen()
    print(f'Servidor iniciado em {host}:{port}')
except socket.error as err:
    print(f'Falha na criação do socket: {err}')

print('Aguardando requisição do cliente...')
conexao, endereco = servidor.accept()
print(f'Conectado em {endereco}')

while True:
    dados = conexao.recv(1024).decode()
    
    if dados == 'end':
        print('Conexão encerrada')
        break
    
    lista_dados = dados.split(',')
    opcao = int(lista_dados[-1])

    if opcao == 1:
        fs.criar(lista_dados[0], lista_dados[1], lista_dados[2])
    elif opcao == 2:
        todos_dados = fs.listar()
        conexao.send(todos_dados.encode())
    elif opcao == 3:
        resultado_pesquisa = fs.pesquisar(lista_dados[0])
        conexao.send(resultado_pesquisa.encode())
    elif opcao == 4:
        resultado_exclusao = fs.excluir(lista_dados[0])
        conexao.send(resultado_exclusao.encode())

conexao.close()
servidor.close()