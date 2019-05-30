import random as rd

dataTypes = ["\"temperature\"", "\"humidity\"", "\"vibration\""]
acceptables = ['00', '01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12',
               '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27',
               '28', '29', '30']

string = "["

for i in range(500):
    dataPoint = "{\n\t\"signature\": " + str(rd.randint(0, 10)) + ",\n"

    timeStamp = "2019-" + acceptables[rd.randint(1, 6)] + "-" + acceptables[rd.randint(1, 30)] + " " + acceptables[rd.randint(0, 24)]

    dataPoint = dataPoint + "\t\"timeStamp\": \"" + timeStamp + "\",\n"
    dataPoint = dataPoint + "\t\"dataType\": " + \
        dataTypes[rd.randint(0, 2)] + ",\n"
    dataPoint = dataPoint + "\t\"dataValue\": " + \
        str(rd.randint(10, 100)) + "\n}"
    if(i < 499):
        dataPoint = dataPoint + ",\n"
    string = string + dataPoint

string = string + "]"

f = open("randomData.json", "w")
f.write(string)
f.close()
