## Trabalho 2: Sockets, Arquivos e Funções
Elaborar um sistema que utilize os recursos de programação para administração de redes
de computadores – Sockets, Arquivos e Funções.
- [x] O sistema deve incluir dados (a serem definidos pelo aluno) recebidos pelo cliente e
enviados para o servidor. O servidor deve fazer a inclusão dos dados.
- [x] Em ver dados do servidor o programa cliente deve solicitar os dados e o programa
servidor deve enviar os dados cadastrados no arquivo texto no servidor.
- [x] Em pesquisar dados o programa cliente deve ler um dado e enviar ao servidor. O
programa servidor deve então retornar dados/indicação de inexistência de registros
da pesquisa.
- [x] Em solicitar exclusão de dados o programa cliente deve enviar solicitação ao
servidor indicando o dado a ser excluído. O programa servidor deve validar os dados
e realizar a exclusão, retornando o indicativo ao cliente.

## Requisitos
- python 3.8.10


## Instalação
Realize um clone desse repositório.

## Rodando o Código

Necessário iniciar o servidor primeiro com o comando 

```bash
  python servidor/servidor.py
```

Depois iniciar o cliente

```bash
  python cliente/cliente.py
```

## Demostração


https://github.com/filipevmimbarcas/trabalho-02-sockets/assets/42503069/41ca126b-f122-4fb5-919c-90eba707f69d



## Referência 

- [virtualenv](https://docs.python.org/pt-br/3/library/venv.html)
