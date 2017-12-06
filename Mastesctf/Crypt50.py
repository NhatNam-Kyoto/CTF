'''import random

encode = ""
start = random.randint(0, len(key)-1)
i = start
for c in flag:
    encode += chr(ord(c) ^ ord(key[i]))
    i += 1
    i %= len(key)
print chr(len(flag)) + chr(start) + encode

# flag format: matesctf{}
# matesctf{z4nh_c4_tu0j_th4nh_xu4n_d3_|_4m_crypt0}
'''

from binascii import unhexlify, hexlify
import socket, time, sys


cipherX = unhexlify("149b56fc2483ff434ccb79acca959c2e51825f31da9552fbf58ddc97764bd912398e4fc9aa4ed777619205892095c1c90a")[:-1]
flag = "matesctf{"

f = open("data", "wb")
key = dict()
st = set()
while 1:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(("125.235.240.167", 13337))
    data = s.recv(1024)
    start= data[1]
    cipher = data[2]

    key[start] = chr(cipher ^ ord('m'))
    f.write((hexlify(data) + "\n".encode('utf-8')))

    st.add(data)
    if(len(st) == 48):
        break
print(data)
f.close()
flag = ""
for i in range(48):
    flag += (chr(ord(key[i]) ^ cipherX[i]))
    sys.stdout.write(flag + '\n')
    sys.stdout.flush()
    time.sleep(3)
