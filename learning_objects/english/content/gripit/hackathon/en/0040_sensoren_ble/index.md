---
hruid: org_dwengo_gripit_hackathon_sensoren_ble
version: 1
language: en
title: "View sensor readings with Python"
description: "Upload firmware with sensors and view your gripper's readings over BLE."
keywords: ["gripit", "hackathon", "halberd", "arduino", "python", "ble", "sensor"]
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

# View sensor readings with Python

In the previous step you controlled a parallel gripper over BLE. Now you will use the fingertip sensor module to view the pressure voltage and the distance to an object. You need Halberd, a connected sensor module and the same Python environment as before.

### Connect the sensor module

Turn off the power before making connections. Connect the module to Halberd: `3.3V` to `3.3V`, `GND` to `GND`, `SDA` to `D16`, `SCL` to `D15` and `Pres_out` to `A0`. Check the labels, wiring and supply voltage of your module and board. The distance sensor uses I2C via `Wire`; the pressure sensor uses analogue input `A0`.

### Upload the sensor firmware

1. Open *File \> Examples \> HalberdGripper \> parallel_gripper_servo_with_sensors* and save your own copy. The [source code](https://github.com/dwengovzw/dwengo_nrf52_core/tree/main/nrf52/1.0.1/libraries/HalberdGripper/examples/parallel_gripper_servo_with_sensors) is also online.
2. Choose a unique `GRIPPER_NAME` and carry over the safely calibrated servo connections, pulse widths, opening limits and geometry from your previous firmware. This sketch also drives servos, even if you only want to view sensors. Work safely: keep fingers clear and turn off servo power if you do not want movement.
3. Verify and upload the sketch. Open the serial monitor at 115200 baud. Check the startup message and `VL53L4CD detected on Wire.`. If you see `VL53L4CD time-of-flight sensor not found, check wiring!`, turn off power and check the connections.

The sketch declares the `tof` (distance in millimetres) and `pressure` (voltage in volts) channels using `configureSensor`. In `loop()` it reads the sensors and sends the values to the BLE library through `reportSensor`.

### Plot the readings

Use the same working folder and active virtual environment as for `gripper.py`. Install the additional plotting library there once:

```bash
python -m pip install matplotlib
```

Create a new `sensors.py` file in that folder with the code below. The default name matches the sensor sketch; replace `gripper-left-sensors` with your `GRIPPER_NAME` if you changed it. First close `gripper.py` or any other BLE client.

```python
import time
from collections import deque

import matplotlib.pyplot as plt
from airo_robots.grippers import HalberdBLEGripper
from airo_robots.grippers.hardware.halberd_ble.client import HalberdConnectionError

gripper = HalberdBLEGripper.connect(name="gripper-left-sensors")
try:
    names = [sensor.name for sensor in gripper.sensors]
    if "tof" not in names or "pressure" not in names:
        raise RuntimeError(f"Sensors missing from firmware: {names}")

    times = deque(maxlen=300)
    distances = deque(maxlen=300)
    pressures = deque(maxlen=300)
    plt.ion()
    fig, axes = plt.subplots(2, 1, sharex=True)
    distance_line, = axes[0].plot([], [])
    pressure_line, = axes[1].plot([], [])
    axes[0].set_ylabel("Distance (mm)")
    axes[1].set_ylabel("Pressure voltage (V)")
    axes[1].set_xlabel("Time (s)")
    fig.suptitle("Waiting for sensor readings")
    plt.show(block=False)
    started = time.monotonic()

    while plt.fignum_exists(fig.number):
        try:
            readings = gripper.sensor_values
        except HalberdConnectionError as error:
            if str(error) != "No sensor snapshot received from the gripper yet.":
                raise
            plt.pause(0.2)
            continue
        values = dict(zip(names, readings, strict=True))
        times.append(time.monotonic() - started)
        distances.append(values["tof"])
        pressures.append(values["pressure"])
        distance_line.set_data(times, distances)
        pressure_line.set_data(times, pressures)
        fig.suptitle("Latest received sensor readings")
        for axis in axes:
            axis.relim()
            axis.autoscale_view()
        plt.pause(0.2)
finally:
    gripper.disconnect()
```

Run `python sensors.py`. The window plots the latest received distance and pressure voltage over time. Hold an object in front of the distance sensor or gently press the pressure sensor and observe the graphs. Close the window to disconnect.

### What do the values mean?

The pressure value is a voltage, not a calibrated force. A distance reading can be invalid. The example firmware can report `0` before the first valid distance and then keep reporting the last valid distance when a reading fails; the graph therefore does not prove that every value is current or valid. Compare with the serial monitor and do not use these values as a safety stop.

The library only notifies sensors when a value changes. If the window keeps waiting for readings, gently change the sensor input and check the serial output and wiring. Also check the exact BLE name, Bluetooth and that no other client is connected. A lost connection or missing sensor channel produces an error.
