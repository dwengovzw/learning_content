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

<div class="dwengo_content fiche">
<h1 class="title">Gripper libraries and BLE firmware</h1>
<h2 class="subtitle">Make Halberd talk to airo-robots</h2>
<div class="items">
<div class="info_item item">
<h3 class="info_item_title">What do the libraries do?</h3>
<p><a href="https://github.com/dwengovzw/Blockly-for-Dwenguino/tree/unified/backend/compilation/hardware/dwengo/nrf52/1.0.0/libraries/HalberdGripper">HalberdGripper</a> implements the Airo Gripper Protocol (AGP) over BLE. Your sketch describes the axes and poses and decides how the motors respond. <a href="https://github.com/dwengovzw/Blockly-for-Dwenguino/tree/unified/backend/compilation/hardware/dwengo/nrf52/1.0.0/libraries/HalberdGripperSensor">HalberdGripperSensor</a> reads the analogue pressure sensor and VL53L4CD distance sensor on the fingertip module. The sensor library is optional for the first BLE example.</p>
<p>These libraries are also used by the online programming environment, but are not automatically available in your Arduino sketchbook. The board package supplies Servo and Bluefruit, among others; install the two gripper libraries separately.</p>
</div>
<div class="info_item item">
<h3 class="info_item_title">Install from GitHub</h3>
<ol>
<li>Open the <a href="https://github.com/dwengovzw/Blockly-for-Dwenguino/tree/unified">unified branch of Blockly-for-Dwenguino</a> and choose <em>Code &gt; Download ZIP</em>. Extract the complete archive. The ZIP contains the whole repository, not just the libraries.</li>
<li>In the extracted directory, find <code>backend/compilation/hardware/dwengo/nrf52/1.0.0/libraries</code>. Copy the complete <code>HalberdGripper</code> and <code>HalberdGripperSensor</code> folders, including <code>library.properties</code>, <code>src</code> and <code>examples</code>.</li>
<li>In Arduino IDE open <em>File &gt; Preferences</em> and find the <em>Sketchbook location</em>. Place both folders directly in its <code>libraries</code> subfolder, creating it if needed. The result should be, for example, <code>libraries/HalberdGripper/library.properties</code>, not an extra nested folder.</li>
<li>Restart the IDE, select Halberd and check that both libraries' examples appear under <em>File &gt; Examples</em>. Do not use <em>Add .ZIP Library</em> with the complete repository ZIP: it is not an individual Arduino library.</li>
</ol>
</div>
<div class="info_item item">
<h3 class="info_item_title">Prepare a parallel gripper</h3>
<ol>
<li>Open <em>File &gt; Examples &gt; HalberdGripper &gt; parallel_gripper_servo</em>. The <a href="https://github.com/dwengovzw/Blockly-for-Dwenguino/tree/unified/backend/compilation/hardware/dwengo/nrf52/1.0.0/libraries/HalberdGripper/examples/parallel_gripper_servo">source code</a> is also online. Save your own copy before editing.</li>
<li>Choose a unique <code>GRIPPER_NAME</code> for your team and use exactly that name in Python. The example configures a parallel axis, <code>open</code> and <code>closed</code> poses, callbacks and position updates. Call <code>gripper.update()</code> regularly in <code>loop()</code>.</li>
<li>Dwengo board package 1.0.0 does not define the sketch's <code>SERVO_1</code> and <code>SERVO_2</code> names. In your copy, replace them with <code>D1</code> and <code>D2</code> respectively. This preserves the original example's pin numbers; the board definition identifies D1 and D2 as SERVO2 and SERVO3 respectively. Always check your board's labels and wiring.</li>
<li>Adapt the servo connections, pulse widths, opening limits in metres, geometry and angle calculation to your mechanism. The sketch drives two servos; do not rely on its introductory description when it differs from the code. Its sensor values are simulated.</li>
<li>Verify and upload the adapted sketch. Open the serial monitor at 115200 baud to see the startup message; Halberd then advertises under the chosen name.</li>
</ol>
<p><strong>Test safely:</strong> turn power off before wiring, check GND, 5V and PWM, and use a suitable servo power supply. Start without an object and with small, controlled movements; keep fingers clear. The example's servo angles and geometry are not a universally safe calibration. Switch off power if motion is unexpected.</p>
<p>The example reports a calculated target/intermediate position, not a measured finger opening. Specified speed and grasp force are not automatically enforced physical limits. Test and implement limits, stop behaviour and feedback as needed; a lost connection is not an emergency stop.</p>
</div>
<div class="info_item item">
<h3 class="info_item_title">Optional: real sensors</h3>
<p>See <em>HalberdGripperSensor &gt; read_pressure_and_distance</em> for a serial sensor test and <em>HalberdGripper &gt; parallel_gripper_servo_with_sensors</em> for BLE integration. Also replace the servo aliases in that integration sketch as above. Follow each sketch's wiring and I2C bus: the integration sketch uses <code>Wire</code> and pressure on <code>A0</code>. Check the module and supply voltage before connecting it. Pressure voltage is not directly calibrated force; a distance reading can be invalid.</p>
</div>
</div>
</div>
