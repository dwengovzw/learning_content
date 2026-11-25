---
hruid: org_dwengo_gripit_hackathon_bibliotheken_firmware
version: 1
language: en
title: "Gripper libraries and BLE firmware"
description: "Install the Halberd libraries and prepare your gripper firmware."
keywords: ["gripit", "hackathon", "halberd", "arduino", "servo", "sensor", "ble"]
educational_goals: []
copyright: dwengo
licence: dwengo
content_type: text/markdown
available: true
target_ages: [18]
difficulty: 3
estimated_time: 35
skos_concepts: ['http://ilearn.ilabt.imec.be/vocab/curr1/s-computers-en-systemen']
teacher_exclusive: false
---

# Gripper libraries and BLE firmware

## Make Halberd talk to airo-robots

### What do the libraries do?

[HalberdGripper](https://github.com/dwengovzw/Blockly-for-Dwenguino/tree/unified/backend/compilation/hardware/dwengo/nrf52/1.0.0/libraries/HalberdGripper) implements the Airo Gripper Protocol (AGP) over BLE. Your sketch describes the axes and poses and decides how the motors respond. [HalberdGripperSensor](https://github.com/dwengovzw/Blockly-for-Dwenguino/tree/unified/backend/compilation/hardware/dwengo/nrf52/1.0.0/libraries/HalberdGripperSensor) reads the analogue pressure sensor and VL53L4CD distance sensor on the fingertip module. The sensor library is optional for the first BLE example.

These libraries are also used by the online programming environment, but are not automatically available in your Arduino sketchbook. The board package supplies Servo and Bluefruit, among others; you must also install the [DwengoCompatibilityLayer](https://github.com/dwengovzw/Blockly-for-Dwenguino/tree/unified/backend/compilation/hardware/dwengo/nrf52/1.0.0/libraries/DwengoCompatibilityLayer) and both gripper libraries separately.

### Install from GitHub

1.  Download the libraries individually: [DwengoCompatibilityLayer.zip](https://raw.githubusercontent.com/dwengovzw/Blockly-for-Dwenguino/refs/heads/unified/backend/compilation/hardware/dwengo/nrf52/1.0.0/libraries/DwengoCompatibilityLayer/DwengoCompatibilityLayer.zip), [HalberdGripper.zip](https://raw.githubusercontent.com/dwengovzw/Blockly-for-Dwenguino/refs/heads/unified/backend/compilation/hardware/dwengo/nrf52/1.0.0/libraries/HalberdGripper/HalberdGripper.zip) and [HalberdGripperSensor.zip](https://raw.githubusercontent.com/dwengovzw/Blockly-for-Dwenguino/refs/heads/unified/backend/compilation/hardware/dwengo/nrf52/1.0.0/libraries/HalberdGripperSensor/HalberdGripperSensor.zip). The sensor library is optional for the first BLE example.
2.  In Arduino IDE, choose *Sketch \> Include Library \> Add .ZIP Library...* and select the downloaded ZIP files one at a time. Install at least `DwengoCompatibilityLayer` and `HalberdGripper`; install `HalberdGripperSensor` if you use the sensor examples.
3.  Restart the IDE, select Halberd and check under *File \> Examples* that the `HalberdGripper` examples appear and, if installed, the `HalberdGripperSensor` examples too.

### Prepare a parallel gripper

1.  Open *File \> Examples \> HalberdGripper \> parallel_gripper_servo*. The [source code](https://github.com/dwengovzw/Blockly-for-Dwenguino/tree/unified/backend/compilation/hardware/dwengo/nrf52/1.0.0/libraries/HalberdGripper/examples/parallel_gripper_servo) is also online. Save your own copy before editing.
2.  Choose a unique `GRIPPER_NAME` for your team and use exactly that name in Python. The example configures a parallel axis, `open` and `closed` poses, callbacks and position updates. Call `gripper.update()` regularly in `loop()`.
3.  Dwengo board package 1.0.0 does not define the sketch's `SERVO_1` and `SERVO_2` names. In your copy, replace them with `D1` and `D2` respectively. This preserves the original example's pin numbers; the board definition identifies D1 and D2 as SERVO2 and SERVO3 respectively. Always check your board's labels and wiring.
4.  Adapt the servo connections, pulse widths, opening limits in metres, geometry and angle calculation to your mechanism. The sketch drives two servos; do not rely on its introductory description when it differs from the code. Its sensor values are simulated.
5.  Verify and upload the adapted sketch. Open the serial monitor at 115200 baud to see the startup message; Halberd then advertises under the chosen name.

**Test safely:** turn power off before wiring, check GND, 5V and PWM, and use a suitable servo power supply. Start without an object and with small, controlled movements; keep fingers clear. The example's servo angles and geometry are not a universally safe calibration. Switch off power if motion is unexpected.

The example reports a calculated target/intermediate position, not a measured finger opening. Specified speed and grasp force are not automatically enforced physical limits. Test and implement limits, stop behaviour and feedback as needed; a lost connection is not an emergency stop.

### Optional: real sensors

See *HalberdGripperSensor \> read_pressure_and_distance* for a serial sensor test and *HalberdGripper \> parallel_gripper_servo_with_sensors* for BLE integration. Also replace the servo aliases in that integration sketch as above. Follow each sketch's wiring and I2C bus: the integration sketch uses `Wire` and pressure on `A0`. Check the module and supply voltage before connecting it. Pressure voltage is not directly calibrated force; a distance reading can be invalid.
