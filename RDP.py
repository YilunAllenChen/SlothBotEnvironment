import random as rd
import requests
import time

dataTypes = ['temperature', 'humidity', 'vibration']
acceptables = ['00', '01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12',
               '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27',
               '28', '29', '30']

dataValueCache = 50
hostname = '192.168.137.1'

for month in acceptables[0:6]:
    for day in acceptables[1:31]:
        dataSet = '['
        for hour in acceptables[0:24:2]:
            for agent in range(10):
                dataPoint = {
                    'signature': agent,
                    'timeStamp': int('2019' + month + day + hour),
                    'dataType': dataTypes[0],
                    'dataValue': dataValueCache
                }
                if(dataValueCache > 100):
                    dataValueCache = dataValueCache + rd.randint(-3, 1)
                elif(dataValueCache < 0):
                    dataValueCache = dataValueCache + rd.randint(-1, 3)
                else:
                    dataValueCache = dataValueCache + rd.randint(-2, 2)
                dataSet = dataSet + str(dataPoint) + ',\n'
                time.sleep(0.00001)
        dataSet = dataSet[0:-2] + ']'
        dataSet = dataSet.replace("\'","\"")
        r = requests.post('http://' + hostname + '/dataPost', data=dataSet, headers={'content-type': 'application/json'})
        pastebin_url = r.text 
    print('Temperature | Month: ' + month + " : " + pastebin_url)

for month in acceptables[0:6]:
    for day in acceptables[1:31]:
        dataSet = '['
        for hour in acceptables[0:24:1]:
            for agent in range(10):
                dataPoint = {
                    'signature': agent,
                    'timeStamp': int('2019' + month + day + hour),
                    'dataType': dataTypes[1],
                    'dataValue': dataValueCache
                }
                if(dataValueCache > 800):
                    dataValueCache = dataValueCache + rd.randint(-3, 1)
                elif(dataValueCache < 30):
                    dataValueCache = dataValueCache + rd.randint(-1, 3)
                else:
                    dataValueCache = dataValueCache + rd.randint(-2, 2)
                dataSet = dataSet + str(dataPoint) + ',\n'
        dataSet = dataSet[0:-2] + ']'
        dataSet = dataSet.replace("\'","\"")
        r = requests.post('http://' + hostname + '/dataPost', data=dataSet, headers={'content-type': 'application/json'})
        pastebin_url = r.text 
    print('Humidity | Month: ' + month + " : " + pastebin_url)


for month in acceptables[0:6]:
    for day in acceptables[1:31]:
        dataSet = '['
        for hour in acceptables[0:24:4]:
            for agent in range(7):
                dataPoint = {
                    'signature': agent,
                    'timeStamp': int('2019' + month + day + hour),
                    'dataType': dataTypes[2],
                    'dataValue': dataValueCache
                }
                if(dataValueCache > 500):
                    dataValueCache = dataValueCache + rd.randint(-3, 1)
                elif(dataValueCache < 0):
                    dataValueCache = dataValueCache + rd.randint(-1, 3)
                else:
                    dataValueCache = dataValueCache + rd.randint(-2, 2)
                dataSet = dataSet + str(dataPoint) + ',\n'
        dataSet = dataSet[0:-2] + ']'
        dataSet = dataSet.replace("\'","\"")
        r = requests.post('http://' + hostname + '/dataPost', data=dataSet, headers={'content-type': 'application/json'})
        pastebin_url = r.text 
    print('Vibration | Month: ' + month + " : " + pastebin_url)
