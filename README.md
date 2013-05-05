pyraspi
=======

### Overview

Python scripts for GPIO input and output. 

### Setup

#### LED

Install newest version of the RPi Python library 
```bash
sudo apt-get install python-rpi.gpio python3-rpi.gpio
```

#### LCD PLATE

Clone the Adafruit repo
```bash
git clone git@github.com:adafruit/Adafruit-Raspberry-Pi-Python-Code.git
```

Copy these files into the lcd-plate directory (ignored by .gitignore)
- Adafruit_CharLCDPlate.py
- Adafruit_I2C.py
- Adafruit_MCP230xx.py
- Adafruit_LCDtest.py

#### REST SERVER

Install the Bottle framework

```bash
sudo apt-get install python-bottle python-bottle-doc
```

Start the server 
```bash
sudo ./Server.py
```

