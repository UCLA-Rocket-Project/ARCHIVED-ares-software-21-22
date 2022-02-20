import serial, time, socket, os

port = '/dev/serial/by-path/platform-fd500000.pcie-pci-0000:01:00.0-usb-0:1.4:1.0'
labels = ['chamber 1', 'chamber 2', 'chamber 3']
log = open('/home/ubuntu/logs/thermocouple.csv', 'a')

def millis():
    return int(time.time_ns() / 1000000)

while True:
    try:
        serial_port = serial.Serial(port, 9600, timeout=0.1)
    except:
        continue
    finally:
        break

ip = '127.0.0.1'
port = 2000
client = socket.socket(family = socket.AF_INET, type = socket.SOCK_DGRAM)

prev = millis()

while True:
    try:
        line = serial_port.readline()
    except:
        os._exit(1)
    data = line[:-1].split(',')
    if len(data) == len(labels):
        now = millis()
        log.write(str(now) + ',' + line)
        if now > prev + 100:
            for l, d in zip(labels, data):
                d = "{:.1f}".format(d)
                bytes = (l + ' ' + l + '=' + d + ' ' + str(now * 1000000)).encode()
                client.sendto(bytes, port)
            prev = now