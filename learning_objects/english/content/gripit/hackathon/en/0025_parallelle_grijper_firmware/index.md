---
hruid: org_dwengo_gripit_hackathon_parallelle_grijper_firmware
version: 1
language: en
title: "Firmware for a parallel gripper"
description: "Prepare firmware to control a parallel gripper over BLE."
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

# Firmware for a parallel gripper

In the previous step you tested the BLE connection without a gripper. Now you will prepare firmware that turns Bluetooth commands into movements of a real parallel gripper.

### Understand the example

In Arduino IDE, open *File \> Examples \> HalberdGripper \> parallel_gripper_servo*. The [source code](https://github.com/dwengovzw/dwengo_nrf52_core/tree/main/nrf52/1.0.1/libraries/HalberdGripper/examples/parallel_gripper_servo) is also online. Save your own copy before editing.

The firmware drives two servos through `SERVO_1` and `SERVO_2`. Together they move one axis: the distance between the gripper's fingers. The sketch defines two poses, `open` and `closed`. When it receives a corresponding BLE command, a callback sets a new target width.

The `widthToAngle` function converts the desired distance between the fingers into a servo angle. This conversion is called the gripper's inverse kinematics. In `loop()`, the calculated width moves towards the target; `reportPosition()` reports that value and `gripper.update()` handles communication.

### Adapt and upload the firmware

1. Choose a unique `GRIPPER_NAME` for your team. Use exactly the same name in the following Python step.
2. Adapt the servo connections, pulse widths, opening limits in metres, geometry and angle calculation to your mechanism. Check your board's labels and wiring. The defaults are not suitable for every gripper.
3. Verify and upload the firmware to Halberd. Open the serial monitor at 115200 baud and check for the startup message `HalberdGripper advertising as ...` with your name.

**Test safely:** turn power off before wiring, check GND, 5V and PWM, and use a suitable servo power supply. Start without an object and with small, controlled movements; keep fingers clear. Switch off power if motion is unexpected.

The example reports a calculated target/intermediate position, not a measured finger opening. Specified speed and grasp force are not automatically enforced physical limits. Test and implement limits, stop behaviour and feedback as needed; a lost connection is not an emergency stop.

In the next step you will connect Python to this firmware and test the `open` and `closed` poses.
