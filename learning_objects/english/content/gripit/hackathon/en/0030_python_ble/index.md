---
hruid: org_dwengo_gripit_hackathon_python_ble
version: 1
language: en
title: "Control your gripper with Python and BLE"
description: "Connect airo-robots to your Halberd gripper and try a simple grasping task."
keywords: ["gripit", "hackathon", "halberd", "python", "ble", "airo"]
educational_goals: []
copyright: dwengo
licence: dwengo
content_type: text/markdown
available: true
target_ages: [18]
difficulty: 3
estimated_time: 30
skos_concepts: ['http://ilearn.ilabt.imec.be/vocab/curr1/s-computers-en-systemen']
teacher_exclusive: false
---

# Control your gripper with Python and BLE

## From a wireless connection to a first grasping task

### Prepare your program

First upload the adapted `parallel_gripper_servo` firmware from the previous step and leave Halberd powered on. Enable Bluetooth on your computer. This firmware uses AGP, not the Nordic UART Service used by other BLE examples.

Use the same working folder and virtual environment as for `identify.py`. If you open a new terminal, reactivate the existing environment with `.\.venv\Scripts\Activate.ps1` in Windows PowerShell or `source .venv/bin/activate` on macOS or Linux. There is no need to recreate the environment or reinstall the driver.

### Connect, open and close

Create a new `gripper.py` file in the same working folder and save this code in it. Replace the name with your `GRIPPER_NAME`. First test without an object, after safely calibrating the firmware's movements and limits.

``` python
from airo_robots.grippers import HalberdBLEGripper

print("Found:", HalberdBLEGripper.discover())
gripper = HalberdBLEGripper.connect(name="my-first-gripper")
try:
    gripper.identify()
    gripper.open().wait()
    gripper.close().wait()
    gripper.open().wait()
finally:
    gripper.disconnect()
```

Run `python gripper.py`. The LED briefly blinks at `identify()`; the gripper opens, closes and opens again. `wait()` waits for the firmware's completion message, not an independent measurement. If movement is missing or an error occurs, check the firmware and disconnect power if necessary.

To move to a specific opening, for example with `gripper.move(0.02).wait()`, the firmware must also implement an `onMove` callback. The basic `parallel_gripper_servo` example only supports the `open` and `closed` poses; use adapted firmware with safely calibrated limits for other target positions.

### Troubleshooting

- No gripper found? Check Bluetooth, power, the AGP firmware, the exact name and whether another client is already connected. A connected gripper does not advertise.
- Several grippers have the same name? Give each team a unique name in the sketch; otherwise the driver reports an ambiguous name. If necessary use `connect(name="gripper-left", address="...")` with the address from discovery.
- Import error? Activate the same virtual environment in which you installed the package. Check your Python version and reinstall in that environment.
- No completion? Check the serial output, callbacks, `reportPosition()` and `update()`. A reported position does not prove that the mechanism actually moved.

### Hackathon task

Test your design with different everyday objects. For each object, record the opening width, result and possible causes of failure. Change one property at a time and compare again. Explicitly implement how the gripper should respond to contact, blockage and lost connections.
