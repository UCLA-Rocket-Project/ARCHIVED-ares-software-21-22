import datetime
import calendar
d = [
    datetime.datetime(2022, 1, 28, 7, 6, 40),
    datetime.datetime(2022, 1, 28, 7, 8, 55), 
    datetime.datetime(2022, 1, 28, 7, 10, 45), 
    datetime.datetime(2022, 1, 28, 7, 14, 10), 
    datetime.datetime(2022, 1, 28, 7, 15, 5), 
    datetime.datetime(2022, 1, 28, 7, 16, 15), 
    datetime.datetime(2022, 1, 28, 7, 17, 15), 
    datetime.datetime(2022, 1, 28, 7, 18, 25), 
    datetime.datetime(2022, 1, 28, 7, 19, 35), 
    datetime.datetime(2022, 1, 28, 7, 20, 20),
    datetime.datetime(2022, 1, 28, 7, 21, 15),
    datetime.datetime(2022, 1, 28, 7, 22, 10),
    datetime.datetime(2022, 1, 28, 7, 23, 20),
    datetime.datetime(2022, 1, 28, 7, 24, 10),
    datetime.datetime(2022, 1, 28, 7, 25, 10),
    datetime.datetime(2022, 1, 28, 7, 26, 00),
    datetime.datetime(2022, 1, 28, 7, 26, 45),
    datetime.datetime(2022, 1, 28, 7, 27, 25),
    datetime.datetime(2022, 1, 28, 7, 28, 15),
    datetime.datetime(2022, 1, 28, 7, 29, 0),
    datetime.datetime(2022, 1, 28, 7, 24, 10),
    datetime.datetime(2022, 1, 28, 7, 30, 5)
    ]

f = open("adc.csv", "r")

i = 0
time = calendar.timegm(d[i].timetuple()) * 1000

p = 0

while i < len(d):
    l = f.readline()[:-1].split(',')
    print(l)
    print(time)
    if int(l[0]) >= time + 5000:
        data = []
        for x in range(len(l) - 1):
            data.append(0.0)

        n = 0
        
        while int(l[0]) <= time + 15000:
            n += 1
            for j in range(len(data)):
                data[j] = data[j] + float(l[j + 1])
            l = f.readline()[:-1].split(',')
        
        for j in range(len(data)):
            data[j] = data[j] / float(n)
        
        print(p, end = "")
        print(",", end = "")
        print(data)

        i += 1
        p += 50
        time = calendar.timegm(d[i].timetuple()) * 1000