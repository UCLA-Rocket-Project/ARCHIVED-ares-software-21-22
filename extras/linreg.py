import numpy as np
from sklearn.linear_model import LinearRegression

f = open("calibration1.csv", 'r')

pressures = []
voltages = [[] for _ in range(9)]

while True:
    l = f.readline().replace(' ', '').replace('\n', '').split(',')
    pressures.append(float(l[0]))
    for i in range(2, len(l)):
        voltages[i - 2].append(float(l[i]))
    
    if (l[0] == '1000'):
        break


for i in range(9):
    x = np.array(voltages[i]).reshape((-1, 1))
    y = np.array(pressures)
    model = LinearRegression().fit(x, y)
    print(str(i + 1) + "," + str("%.5f" % round(model.coef_[0], 5)) + "," + str("%.5f" % round(model.intercept_, 5)) + "," + str("%.3f" % round(model.score(x, y), 3)))