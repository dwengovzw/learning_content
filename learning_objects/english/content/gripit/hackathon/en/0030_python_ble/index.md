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

### Install the Python driver

First upload the adapted `parallel_gripper_servo` firmware from the previous step and leave Halberd powered on. Enable Bluetooth on your computer. This firmware uses AGP, not the Nordic UART Service used by other BLE examples.

Create a virtual environment using Python 3.11 or newer in your working folder and install the driver. On Windows PowerShell, run:

    py -3 --version
    py -3 -m venv .venv
    .\.venv\Scripts\Activate.ps1
    python -m pip install "airo-robots[halberd]"

On macOS or Linux, run:

    python3 --version
    python3 -m venv .venv
    source .venv/bin/activate
    python -m pip install "airo-robots[halberd]"

Check with `python --version` that the activated environment uses Python 3.11 or newer. On Linux the Bluetooth service must be running and your user must have access to BlueZ. The [airo-mono documentation](https://github.com/airo-ugent/airo-mono/blob/main/airo-robots/airo_robots/grippers/hardware/halberd_ble.md) describes the driver and additional features.

### Connect, open and close

Save this as `gripper.py`. Replace the name with your `GRIPPER_NAME`. First test without an object, after safely calibrating the firmware's movements and limits.

``` python
from airo_robots.grippers import HalberdBLEGripper

print("Found:", HalberdBLEGripper.discover())
gripper = HalberdBLEGripper.connect(name="gripper-left")
try:
    gripper.identify()
    gripper.open().wait()
    gripper.close().wait()
    gripper.open().wait()
finally:
    gripper.disconnect()
```

Run `python gripper.py`. The LED briefly blinks at `identify()`; the gripper opens, closes and opens again. `wait()` waits for the firmware's completion message, not an independent measurement. If movement is missing or an error occurs, check the firmware and disconnect power if necessary.

For a parallel gripper you can also use `gripper.move(0.02).wait()`: the requested opening here is 0.02 metres and must be within your calibrated range. The driver clips requests to the limits declared by the firmware. Other mechanisms can use `GenericHalberdGripper` with their own axes and poses.

### Troubleshooting

- No gripper found? Check Bluetooth, power, the AGP firmware, the exact name and whether another client is already connected. A connected gripper does not advertise.
- Several grippers have the same name? Give each team a unique name in the sketch; otherwise the driver reports an ambiguous name. If necessary use `connect(name="gripper-left", address="...")` with the address from discovery.
- Import error? Activate the same virtual environment in which you installed the package. Check your Python version and reinstall in that environment.
- No completion? Check the serial output, callbacks, `reportPosition()` and `update()`. A reported position does not prove that the mechanism actually moved.

### Hackathon task

Test your design with different everyday objects. For each object, record the opening width, result and possible causes of failure. Change one property at a time and compare again. Use sensors only after calibration and explicitly implement how the gripper should respond to contact, blockage and lost connections.
