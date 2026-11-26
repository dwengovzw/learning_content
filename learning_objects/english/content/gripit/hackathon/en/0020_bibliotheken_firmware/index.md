---
hruid: org_dwengo_gripit_hackathon_bibliotheken_firmware
version: 1
language: en
title: "Basic communication with BLE"
description: "Establish a first BLE connection using the Halberd library and blink the LED."
keywords: ["gripit", "hackathon", "halberd", "arduino", "servo", "sensor", "ble"]
educational_goals: []
copyright: dwengo
licence: dwengo
content_type: text/markdown
available: true
target_ages: [18]
difficulty: 3
estimated_time: 25
skos_concepts: ['http://ilearn.ilabt.imec.be/vocab/curr1/s-computers-en-systemen']
teacher_exclusive: false
---

# Basic communication with BLE

## Make Halberd talk to airo-robots

### What do the libraries do?

The libraries needed for the gripper are included in the [Dwengo nRF52 core](https://github.com/dwengovzw/dwengo_nrf52_core). Install or update `Dwengo nRF52 Boards` to version 1.0.1 or newer through Boards Manager, as described in the previous step; you do not need to install the libraries separately.

- `DwengoCompatibilityLayer` makes functions that are also available in the [Dwengo simulator](https://blockly.dwengo.org) usable in the Arduino IDE.
- `HalberdGripper` implements the Airo Gripper Protocol (AGP) over BLE. Your sketch describes the axes and poses and decides how the motors respond.
- `HalberdGripperSensor` reads the analogue pressure sensor and VL53L4CD distance sensor on the fingertip module. The sensor library is optional for the first BLE example.

### Use the included examples

1.  Install or update `Dwengo nRF52 Boards` to version 1.0.1 or newer through Boards Manager, as described in the previous learning object. This installs the libraries and their examples.
2.  Select Halberd and open *File \> Examples \> HalberdGripper* or *File \> Examples \> HalberdGripperSensor*. All examples from both libraries are included in the core.

### Firmware for basic communication

The code on the Halberd board is called its *firmware*. The `identify_only` example tests the Bluetooth Low Energy (BLE) connection between your computer and Halberd. No gripper, servos or sensors are needed: the firmware does not drive motors or implement gripper movement.

1. Open *File \> Examples \> HalberdGripper \> identify_only*. Save your own copy if you want to edit it. The example contains this code:

```cpp
#include <HalberdGripper.h>

HalberdGripper gripper;

void setup() {
  Serial.begin(115200);

  gripper.configureAxis(0, 0.0f, 0.079f, 0.25f);

  if (!gripper.begin("my-first-gripper")) {
    Serial.println("Failed to start HalberdGripper BLE");
    while (true) {
      delay(1000);
    }
  }
  Serial.println("HalberdGripper advertising as my-first-gripper");
}

void loop() {
  gripper.update();
  delay(10);
}
```

`configureAxis` describes a placeholder axis required by the Python driver. Its limits and speed are descriptive values here: no position is measured and nothing moves. `begin` starts BLE and makes the board discoverable as `my-first-gripper`. If startup fails, an error is printed and the sketch stops in the `while` loop. `gripper.update()` handles tasks including the LED blink and must be called regularly.

2. Give each team a unique name in `gripper.begin(...)`. Also update the text in the following `Serial.println(...)` so the message matches. Use exactly the same name in Python.
3. Select Halberd and the correct port, then verify and upload the sketch. Open the serial monitor at 115200 baud. With the default name, `HalberdGripper advertising as my-first-gripper` appears; an error message means BLE did not start.

### Test the connection with Python

Leave Halberd powered on and enable Bluetooth on your computer. Install the Python driver in a virtual environment using Python 3.11 or newer. On Windows PowerShell, run:

```powershell
py -3 -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install "airo-robots[halberd]"
```

On macOS or Linux, run:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install "airo-robots[halberd]"
```

Check with `python --version` that the active environment uses Python 3.11 or newer. Keep this environment for the later Python step.

Save the following as `identify.py`. If you changed the name in the firmware, use the same name here:

```python
from airo_robots.grippers import HalberdBLEGripper

gripper = HalberdBLEGripper.connect(name="my-first-gripper")
try:
    gripper.identify()
finally:
    gripper.disconnect()
```

Run `python identify.py` in the active environment. The `identify` command briefly blinks Halberd's built-in LED so you can recognise the connected board. The library handles the blinking; the sketch does not need to control the LED itself. `disconnect()` closes the connection.

If connection fails, check the board's power, Bluetooth, exact name, serial message and whether another application is already connected. For an import error, check that the virtual environment is active. Next you can prepare firmware for a real parallel gripper.
