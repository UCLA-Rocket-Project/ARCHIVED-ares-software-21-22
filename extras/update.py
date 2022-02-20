import socket

labels = ["load_cell", "low_press", "lox", "fuel", "high_press", "lox_fill", "pneumatics", "fuel_manifold", "lox_manifold", "pt9"]

file = open('/home/ubuntu/logs/adc.csv', 'r')
client = socket.socket(family = socket.AF_INET, type = socket.SOCK_DGRAM)

while True:
    line = file.readline()
    if not line:
        break
    data = line[:-1].split(',')
    time = data[0]
    data = data[1:]
    if (len(data) == len(labels)):
        for l, d in zip(labels, data):
            bytes = (l + ' ' + l + '=' + d + ' ' + str(int(time) * 1000000)).encode()
            client.sendto(bytes, ('127.0.0.1', 2000))
