

import socket

SERVER_ADDRESS = '192.168.0.102'
SERVER_PORT = 8001


socket_servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#solicita ao windows para ouvir na porta 8000
socket_servidor.bind((SERVER_ADDRESS,SERVER_PORT))
socket_servidor.listen()

#aguarda conexão cliente
#debug
print(f'servidor ouvindo em {SERVER_ADDRESS}:{SERVER_PORT} pronto para receber conexões...')
socket_cliente, cliente_addr = socket_servidor.accept()

#debug
print(f'cliente conectado com sucesso. {cliente_addr[0]}:{cliente_addr[1]}')

#receber dado do cleinte
dado_recebido = socket_cliente.recv(1024)
dado_recebido = dado_recebido.decode()

#resposta ao browser
minha_info = 'foi'
msg = 'online e roteando'
resposta = f'HTTP/1.1 200 OK\r\n\r\n{msg}.'

#responder para o cliente
socket_cliente.sendall(resposta.encode('utf-8'))




#encerrar a coexão
socket_cliente.close()
 