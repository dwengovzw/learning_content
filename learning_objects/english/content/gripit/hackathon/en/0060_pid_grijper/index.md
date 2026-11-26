---
hruid: org_dwengo_gripit_hackathon_pid_grijper
version: 1
language: en
title: "Pressure-controlled gripper with Python"
description: "Explore the pressure-control firmware and command open and closed poses over BLE."
keywords: ["gripit", "hackathon", "halberd", "arduino", "python", "ble", "pid", "sensor"]
educational_goals: []
copyright: dwengo
licence: dwengo
content_type: text/markdown
available: true
target_ages: [18]
difficulty: 4
estimated_time: 35
skos_concepts: ['http://ilearn.ilabt.imec.be/vocab/curr1/s-computers-en-systemen']
teacher_exclusive: false
---

# Pressure-controlled gripper with Python

The earlier sensor firmware sent readings to the computer. This example also uses the pressure sensor as **feedback**: on a close command, Halberd tries to reach and then maintain a target sensor value. The controller runs on Halberd; Python only sends commands over BLE.

## Prepare safely first

Work under supervision. Turn off all power before changing wiring and check the connections as in the previous sensor activity. Keep fingers, animals and fragile objects clear of the gripper. Ensure you can immediately cut servo power independently of software; a BLE command or a lost connection is not an emergency stop.

The example values are **not automatically safe** for your sensor, servos, mechanism or object. A faulty or disconnected pressure sensor is not reliably detected; the gripper can keep closing until a limit or timeout. The timeout and software limits do not protect against injury or damage. First have the sensor response, movement direction, servo angles, pulse widths and target checked and calibrated for your setup under supervision. Do not treat the pressure reading as calibrated force.

## Explore the firmware

1. In Arduino IDE, open *File \> Examples \> HalberdGripper \> parallel_gripper_servo_with_sensors_pid*. This example is included in `Dwengo nRF52 Boards` version 1.0.1. The [source code](https://github.com/dwengovzw/dwengo_nrf52_core/tree/main/nrf52/1.0.1/libraries/HalberdGripper/examples/parallel_gripper_servo_with_sensors_pid) is also online. First save your own copy.
2. Use a unique `GRIPPER_NAME`. Only carry over settings that have been checked as safe for your setup. The sketch uses two servos on `D1` and `D2`, the pressure sensor on `A0` and the distance sensor on `Wire`. The example's distance offset is specific to its setup and may not suit your sensor.
3. After the safety checks, verify and upload. Note that on startup the sketch commands the servos to the open angle, before any Python command. In the serial monitor at 115200 baud, check for `HalberdGripper advertising as ...`. On distance-sensor, servo-initialisation or BLE failure, `ready` is not enabled; check the error and turn off power before making changes.

## What does the code do?

| Component | Purpose |
|---|---|
| `targetPressure`, `pressureDeadband` | Target and allowed deviation in raw ADC counts, not newtons. |
| `kp`, `ki`, `kd` | Pressure-control gains. By default `ki = kd = 0`: only P contributes. |
| `pressureSpeed(error, dt)` | Calculates a limited servo angular speed from error and time. |
| `OPENING` | Moves to the open angle and then reports the command complete. |
| `ACQUIRE_PRESSURE` | Controls towards the pressure target. After 100 ms continuously in the deadband it reports completion; after 10 s without settling it reports failure. |
| `HOLD_PRESSURE` | Continues regulating pressure after completion. |
| `HOLD` | Stops regulating and holds the last commanded servo angle; it does not automatically open or switch off. |

`onOpen` and `onClose` queue a request for the main loop. `loop()` reads pressure, runs the controller and calls `gripper.update()`. The reported opening width is estimated from the **commanded** servo angle, not measured by a position sensor. `tof` and `pressure` are BLE sensor values; the latter is voltage in volts, while the controller uses raw counts. The distance value can be missing, zero or stale.

The sketch implements `open` and `closed` poses, but no callback for an arbitrary `move` position. The pressure target and gains are in the firmware; Python does not change them in this example.

## Control the poses from Python

Use the existing working folder and virtual environment from the earlier steps. Close `sensors.py` and other BLE clients before connecting. Create a new `pid_gripper.py` file and use the same name as `GRIPPER_NAME` in the firmware. Read the safety instructions above before issuing commands.

```python
import time

from airo_robots.grippers import GenericHalberdGripper
from airo_robots.grippers.hardware.halberd_ble.client import CommandStatus

gripper = GenericHalberdGripper.connect(name="gripper-left-pid")
try:
    def pose(name):
        sequence = gripper.client.move_pose(name)
        deadline = time.monotonic() + 15
        while time.monotonic() < deadline:
            if not gripper.client.is_connected:
                raise ConnectionError("BLE connection lost")
            status = gripper.client.command_status(sequence)
            if status == CommandStatus.DONE:
                return
            if status == CommandStatus.FAILED:
                raise RuntimeError(f"Command {name} failed; check the serial monitor")
            time.sleep(0.1)
        raise TimeoutError(f"No completion for {name}; check the gripper")

    input("Check the area is clear. Press Enter to open, or Ctrl+C to stop: ")
    pose("open")
    input("Check the setup with your supervisor. Enter closes the gripper; Ctrl+C stops: ")
    pose("closed")
    print("Pressure target reached; regulation remains active.")
    input("Check the area is clear. Press Enter to open, or Ctrl+C to stop: ")
    pose("open")
finally:
    gripper.disconnect()
```

Run `python pid_gripper.py`. The first Enter sends an open command; the second sends a close command. The third opens again. An empty or unsuitable object may prevent the pressure target from being reached: the firmware then reports a failure after its timeout. The program explicitly checks `DONE` and `FAILED`, because the driver's ordinary `.wait()` can also return when a command has failed. If an error or timeout occurs, check the serial output; do not automatically continue.

Even after a successful close, pressure regulation continues until you open, stop or disconnect. On `STOP` or disconnect the firmware enters `HOLD`: it retains the last commanded angle and does not necessarily release an object. Interrupting Python disconnects, but does not replace the independent power switch.

## Compare with the readings

Close `pid_gripper.py` before using the graph from the previous step. Change its BLE name to `gripper-left-pid` or your chosen name. The graph shows the last received voltage and distance, not raw error, PID contributions or a guaranteed current distance. Use the graph to explore data, not for safety monitoring.
