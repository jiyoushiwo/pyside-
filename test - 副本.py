# import serial
#
# serialPort = "COM7"
# baudRate = 9600
# ser = serial.Serial(serialPort,baudRate,timeout=0.5)
# print("参数设置：串口：%s，波特率：%d"%(serialPort,baudRate))
# while 1:
#     str = ser.readline().decode('utf-8')
#     print(str)
# ser.close()


import serial
serialPort = "COM3"
baudRate = 9600
myser = serial.Serial(serialPort,baudRate,timeout=9.5)
while(1):
    data = myser.readline()
    # print(data)
    # print(type(data))

    data = data.strip()#去除串口的\r\n
    data = int(data.decode('utf-8','ignore'))

    print(data)
    print(type(data))


