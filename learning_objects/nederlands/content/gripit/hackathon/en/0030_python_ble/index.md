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

<div class="dwengo_content fiche">
<h1 class="title">Control your gripper with Python and BLE</h1>
<h2 class="subtitle">From a wireless connection to a first grasping task</h2>
<div class="items">
<div class="info_item item">
<h3 class="info_item_title">Install the Python driver</h3>
<p>First upload the adapted <code>parallel_gripper_servo</code> firmware from the previous step and leave Halberd powered on. Enable Bluetooth on your computer. This firmware uses AGP, not the Nordic UART Service used by other BLE examples.</p>
<p>Create a virtual environment using Python 3.11 or newer in your working folder and install the driver. On Windows PowerShell, run:</p>
<pre><code>py -3 --version
py -3 -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install "airo-robots[halberd]"</code></pre>
<p>On macOS or Linux, run:</p>
<pre><code>python3 --version
python3 -m venv .venv
source .venv/bin/activate
python -m pip install "airo-robots[halberd]"</code></pre>
<p>Check with <code>python --version</code> that the activated environment uses Python 3.11 or newer. On Linux the Bluetooth service must be running and your user must have access to BlueZ. The <a href="https://github.com/airo-ugent/airo-mono/blob/main/airo-robots/airo_robots/grippers/hardware/halberd_ble.md">airo-mono documentation</a> describes the driver and additional features.</p>
</div>
<div class="example_item item">
<h3 class="info_item_title">Connect, open and close</h3>
<p>Save this as <code>gripper.py</code>. Replace the name with your <code>GRIPPER_NAME</code>. First test without an object, after safely calibrating the firmware's movements and limits.</p>
<pre><code class="language-python">from airo_robots.grippers import HalberdBLEGripper

print("Found:", HalberdBLEGripper.discover())
gripper = HalberdBLEGripper.connect(name="gripper-left")
try:
    gripper.identify()
    gripper.open().wait()
    gripper.close().wait()
    gripper.open().wait()
finally:
    gripper.disconnect()</code></pre>
<p>Run <code>python gripper.py</code>. The LED briefly blinks at <code>identify()</code>; the gripper opens, closes and opens again. <code>wait()</code> waits for the firmware's completion message, not an independent measurement. If movement is missing or an error occurs, check the firmware and disconnect power if necessary.</p>
<p>For a parallel gripper you can also use <code>gripper.move(0.02).wait()</code>: the requested opening here is 0.02 metres and must be within your calibrated range. The driver clips requests to the limits declared by the firmware. Other mechanisms can use <code>GenericHalberdGripper</code> with their own axes and poses.</p>
</div>
<div class="info_item item">
<h3 class="info_item_title">Troubleshooting</h3>
<ul>
<li>No gripper found? Check Bluetooth, power, the AGP firmware, the exact name and whether another client is already connected. A connected gripper does not advertise.</li>
<li>Several grippers have the same name? Give each team a unique name in the sketch; otherwise the driver reports an ambiguous name. If necessary use <code>connect(name="gripper-left", address="...")</code> with the address from discovery.</li>
<li>Import error? Activate the same virtual environment in which you installed the package. Check your Python version and reinstall in that environment.</li>
<li>No completion? Check the serial output, callbacks, <code>reportPosition()</code> and <code>update()</code>. A reported position does not prove that the mechanism actually moved.</li>
</ul>
</div>
<div class="info_item item">
<h3 class="info_item_title">Hackathon task</h3>
<p>Test your design with different everyday objects. For each object, record the opening width, result and possible causes of failure. Change one property at a time and compare again. Use sensors only after calibration and explicitly implement how the gripper should respond to contact, blockage and lost connections.</p>
</div>
</div>
</div>
