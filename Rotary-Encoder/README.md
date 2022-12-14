# Instructions

## _On Arduino IDE_
- Ensure the Arduino is wired as shown below


![Wiring...](screenshots/rotary4blend.PNG?raw=true "Optional Title")

- Upload the [arduino code][arduinocode] in to your Arduino UNO(ensure the port is correctly set-up)

## _In Blender_
- Open the [betaTest.blend][blendfile] and navigate to the scripting window
- If the script named arduinoScript.py is not available, create a new script with the same name and paste the code from the attached [arduinoScript.py][script] to the new python script within Blender.
- Just before you execute the script you have to paste the python library called [Serial][library] in the following path `C:\Program Files\Blender Foundation\blender-2.83.0-windows64\2.83\python\lib`.
- Ensure you Arduino board is connected to your computer before you execute the python script.


> **Note** 
> I used blender 2.83.0, it worked for me 




[script]: arduinoScript.py
[blendfile]: betaTest.blend
[arduinocode]: Rotary_Encoder/Rotary_Encoder.ino
[library]: serial
