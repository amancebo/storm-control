#!/usr/bin/python
#
## @file
#
# This controls a Thorlabs TDC001 motor controller using micro-manager.
#
# Hazen 04/13
#

import MMCorePy
import time

mmc = MMCorePy.CMMCore()

port = "COM11"
mmc.loadDevice(port, "SerialManager", port)
mmc.initializeDevice(port)
mmc.waitForSystem()

mmc.setProperty(port, "AnswerTimeout", 1.0)
mmc.setProperty(port, "Handshaking", "Off")
mmc.setProperty(port, "DelayBetweenCharsMs", 0.0)

if 0:
    time.sleep(1)
    print "1"

    time.sleep(1)
    print "2"
    mmc.setProperty(port, "BaudRate", 115200)
    time.sleep(1)
    print "3"

    time.sleep(1)
    print "4"

    time.sleep(1)
    print "5"
    mmc.setProperty(port, "Parity", "None")
    time.sleep(1)
    print "6"
    mmc.setProperty(port, "StopBits", 1)
    time.sleep(1)
    print "7"

device_name = "MotorZStage"
mmc.loadDevice(device_name, "Thorlabs", device_name)
mmc.setProperty(device_name, "Port", port)
print "1"

mmc.initializeDevice(device_name)
print "2"

time.sleep(1)

mmc.unloadAllDevices()


#
# The MIT License
#
# Copyright (c) 2014 Zhuang Lab, Harvard University
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
#
 
