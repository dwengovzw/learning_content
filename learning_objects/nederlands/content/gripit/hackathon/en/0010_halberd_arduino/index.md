---
hruid: org_dwengo_gripit_hackathon_halberd_arduino
version: 1
language: en
title: "Programming Halberd with Arduino"
description: "Install the Halberd board package and upload your first program."
keywords: ["gripit", "hackathon", "halberd", "arduino"]
educational_goals: []
copyright: dwengo
licence: dwengo
content_type: text/markdown
available: true
target_ages: [18]
difficulty: 2
estimated_time: 20
skos_concepts: ['http://ilearn.ilabt.imec.be/vocab/curr1/s-computers-en-systemen']
teacher_exclusive: false
---

<div class="dwengo_content fiche">
<h1 class="title">Programming Halberd with Arduino</h1>
<h2 class="subtitle">From a working development environment to your own robotic gripper</h2>
<div class="items">
<div class="info_item item">
<h3 class="info_item_title">The challenge</h3>
<p>Design, build and program a gripper that can pick up different everyday objects. As in <a href="https://www.dwengo.org/gripit/">Grip-&gt;IT</a>, you will combine mechanics, electronics and software. In this learning path you will set up your development environment, make the gripper accessible over Bluetooth Low Energy (BLE), and control it from Python.</p>
<p>You will need a Halberd, a USB data cable, a Bluetooth-enabled computer, Arduino IDE 2 and later Python 3.11 or newer. Physical movement also requires a correctly connected and powered servo gripper. First familiarise yourself with your kit's hardware and power supply.</p>
</div>
<div class="info_item item">
<h3 class="info_item_title">Install the board package</h3>
<ol>
<li>Install <a href="https://www.arduino.cc/en/software/">Arduino IDE</a>. Open <em>File &gt; Preferences</em> and add this URL under <em>Additional Boards Manager URLs</em>, keeping any existing URLs:<br><code>https://dwengovzw.github.io/dwengo_nrf52_core/package_dwengo_index.json</code></li>
<li>Open <em>Tools &gt; Board &gt; Boards Manager</em>, search for <code>Dwengo nRF52 Boards</code> and install it.</li>
<li>Connect Halberd with the USB data cable. Under <em>Tools &gt; Board</em>, select <code>Halberd nRF52840 (DWENGO)</code>, and under <em>Tools &gt; Port</em> select the corresponding port.</li>
<li>Open <em>File &gt; Examples &gt; 01.Basics &gt; Blink</em>. Click <em>Verify</em> and then <em>Upload</em>. Check that the built-in LED blinks.</li>
</ol>
<p>Official instructions and updates are available in the <a href="https://github.com/dwengovzw/dwengo_nrf52_core">Dwengo nRF52 core</a>. This installation uses the existing bootloader; do not casually select <em>Burn Bootloader</em> or a different board definition.</p>
</div>
<div class="info_item item">
<h3 class="info_item_title">If uploading fails</h3>
<p>Check the data cable, power supply, board selection and port. Disconnect other devices to identify the correct port, and close applications using the serial port. Read the full IDE error; ask an organiser for help if the board or bootloader is not recognised.</p>
</div>
</div>
</div>
