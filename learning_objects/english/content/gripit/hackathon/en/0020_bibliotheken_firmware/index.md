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

These libraries are also used by the online programming environment, but are not automatically available in your Arduino sketchbook. The board package supplies Servo and Bluefruit, among others; install the two gripper libraries separately.

### Install from GitHub

1.  Open the [unified branch of Blockly-for-Dwenguino](https://github.com/dwengovzw/Blockly-for-Dwenguino/tree/unified) and choose *Code \> Download ZIP*. Extract the complete archive. The ZIP contains the whole repository, not just the libraries.
2.  In the extracted directory, find `backend/compilation/hardware/dwengo/nrf52/1.0.0/libraries`. Copy the complete `HalberdGripper` and `HalberdGripperSensor` folders, including `library.properties`, `src` and `examples`.
3.  In Arduino IDE open *File \> Preferences* and find the *Sketchbook location*. Place both folders directly in its `libraries` subfolder, creating it if needed. The result should be, for example, `libraries/HalberdGripper/library.properties`, not an extra nested folder.
4.  Restart the IDE, select Halberd and check that both libraries' examples appear under *File \> Examples*. Do not use *Add .ZIP Library* with the complete repository ZIP: it is not an individual Arduino library.

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
