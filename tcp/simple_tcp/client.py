import socket

# 서버의 주소. hostname 또는 ip address를 사용할 수 있다.

HOST='127.0.0.1'

# 서버에서 지정해 놓은 포트번호
PORT = 9999

# 소켓 객체를 생성
# 주소 체계(address family)로 IPv4, 소켓 타입으로 TCP 사용
client_socket=socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 지정한 HOST와 PORT를 사용하여 서버에 접속한다.
client_socket.connect((HOST, PORT))

# 메시지를 전송한다.
client_socket.sendall('안녕'.encode())

# 메시지 수신
data=client_socket.recv(1024)
print('Received', repr(data.decode()))

# 소켓 닫기
client_socket.close()

