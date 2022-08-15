import serial
import time
import bpy
import threading

arduinoSerialData = serial.Serial('COM7', '9600')
lamp = bpy.data.objects['LED']
red_bulb = bpy.data.objects['Bulb-red']
red_bulb_brightness = red_bulb.data.materials['red-glow'].node_tree.nodes["Emission"].inputs[1]

green_bulb = bpy.data.objects['Bulb-green']
green_bulb_brightness = green_bulb.data.materials['green-glow'].node_tree.nodes["Emission"].inputs[1]

blue_bulb = bpy.data.objects['Bulb-blue']
blue_bulb_brightness = blue_bulb.data.materials['blue-glow'].node_tree.nodes["Emission"].inputs[1]

s = bpy.context.scene
f = s.objects['red']
g = s.objects['green']
h = s.objects['yellow']


def record():
    f.data.body = str(round(translate(values[0], -100, 100, 1, 100), 2))
    g.data.body = str(round(translate(values[1], -100, 100, 1, 100), 2))
    h.data.body = str(round(translate(values[2], -100, 100, 1, 100), 2))


def translate(value, leftMin, leftMax, rightMin, rightMax):
    # width of each range of values
    leftSpan = leftMax - leftMin
    rightSpan = rightMax - rightMin

    # convert the left range into float
    valueScaled = float(value - leftMin) / float(leftSpan)

    # convert to right range
    return rightMin + (valueScaled * rightSpan)

def changeLight():
    # print(theData)
    if changeLight.counter == 3:
        changeLight.counter = 0
        # red_bulb_brightness.default_value = translate(theData, -100, 100, 1, 100)
        # print('red')

changeLight.counter = 0
values = [-100, -100, -100]
input = [0]

red_bulb_brightness.default_value = translate(values[0], -100, 100, 1, 100)
green_bulb_brightness.default_value = translate(values[1], -100, 100, 1, 100)
blue_bulb_brightness.default_value = translate(values[2], -100, 100, 1, 100)
 
def runLoop():
    global theData
    while True:
        if arduinoSerialData.inWaiting() > 0:
            try:
                input[0] = arduinoSerialData.readline()
                myData = int(input[0])
            except:
                v = (str(input[0]))[2]
                if v == 'x':
                    changeLight.counter += 1
                if v == 'y':
                    print('y')
                if v == 'z':
                    arduinoSerialData.close()
                
            changeLight()
                
            theData = myData
            # print(values)
            record()
            if changeLight.counter == 0:
                if values[0] >= -100:                    
                    values[0] = values[0] + theData
                    red_bulb_brightness.default_value = translate(values[0], -100, 100, 1, 100)
                else:
                    values[0] = -100
            if changeLight.counter == 1:
                if values[1] >= -100: 
                    values[1] = values[1] + theData
                    green_bulb_brightness.default_value = translate(values[1], -100, 100, 1, 100)
                else:
                    values[1] = -100                    
            if changeLight.counter == 2:
                if values[2] >= -100: 
                    values[2] = values[2] + theData
                    blue_bulb_brightness.default_value = translate(values[2], -100, 100, 1, 100)
                else:
                    values[2] = -100
            
# runLoop()
runLoop.counter = 0
threading.Thread(target=runLoop).start()

# arduinoSerialData.close()