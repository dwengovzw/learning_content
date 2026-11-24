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

# Programming Halberd with Arduino

## From a working development environment to your own robotic gripper

### The challenge

Design, build and program a gripper that can pick up different everyday objects. As in [Grip-\>IT](https://www.dwengo.org/gripit/), you will combine mechanics, electronics and software. In this learning path you will set up your development environment, make the gripper accessible over Bluetooth Low Energy (BLE), and control it from Python.

You will need a Halberd, a USB data cable, a Bluetooth-enabled computer, Arduino IDE 2 and later Python 3.11 or newer. Physical movement also requires a correctly connected and powered servo gripper. First familiarise yourself with your kit's hardware and power supply.

### Install the board package

1.  Install [Arduino IDE](https://www.arduino.cc/en/software/). Open *File \> Preferences* and add this URL under *Additional Boards Manager URLs*, keeping any existing URLs:\
    `https://dwengovzw.github.io/dwengo_nrf52_core/package_dwengo_index.json`
2.  Open *Tools \> Board \> Boards Manager*, search for `Dwengo nRF52 Boards` and install it.
3.  Connect Halberd with the USB data cable. Under *Tools \> Board*, select `Halberd nRF52840 (DWENGO)`, and under *Tools \> Port* select the corresponding port.
4.  Open *File \> Examples \> 01.Basics \> Blink*. Click *Verify* and then *Upload*. Check that the built-in LED blinks.

Official instructions and updates are available in the [Dwengo nRF52 core](https://github.com/dwengovzw/dwengo_nrf52_core). This installation uses the existing bootloader; do not casually select *Burn Bootloader* or a different board definition.

### If uploading fails

Check the data cable, power supply, board selection and port. Disconnect other devices to identify the correct port, and close applications using the serial port. Read the full IDE error; ask an organiser for help if the board or bootloader is not recognised.
