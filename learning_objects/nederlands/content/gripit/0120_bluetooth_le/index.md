---
hruid: org_dwengo_gripit_bluetooth_le
version: 1
language: nl
title: "Bluetooth Low Energy met de Halberd"
description: "Wissel berichten uit tussen de Halberd en een computer via Bluetooth Low Energy."
keywords: ["fiche", "gripit", "halberd", "bluetooth", "ble", "python"]
educational_goals: [
	{source: Source, id: id}
]
copyright: dwengo
licence: dwengo
content_type: text/markdown
available: true
target_ages: [14, 15, 16, 17, 18]
difficulty: 2
estimated_time: 30
skos_concepts: [
	'http://ilearn.ilabt.imec.be/vocab/curr1/s-computers-en-systemen'
]
teacher_exclusive: false
---

<div class="dwengo_content fiche">
	<h1 class="title">Bluetooth Low Energy met de Halberd</h1>
	<h2 class="subtitle">Verstuur en ontvang berichten met een computer</h2>
	<div class="items">
		<div class="info_item item">
			<h3 class="info_item_title">Bluetooth Low Energy</h3>
			<p class="info_item_content">
				Bluetooth Low Energy (BLE) is geschikt om kleine berichten draadloos uit te wisselen. De Halberd is het BLE-apparaat dat adverteert; de computer zoekt de Halberd, maakt verbinding en wisselt daarna berichten uit.
			</p>
			<p class="info_item_content">
				Dit voorbeeld gebruikt de Nordic UART Service via de Adafruit Bluefruit-bibliotheek. De computer schrijft naar de RX-karakteristiek, die de Halberd ontvangt. De Halberd stuurt berichten naar de TX-karakteristiek; de computer ontvangt die als notificaties.
			</p>
		</div>
		<div class="info_item item">
			<h3 class="info_item_title">Voor je begint</h3>
			<ol class="info_item_content">
				<li>Gebruik een Arduino-omgeving met de board support package <em>Adafruit nRF52 by Adafruit</em>. Die bevat de Bluefruit-bibliotheek.</li>
				<li>Selecteer de Halberd-boardconfiguratie die overeenkomt met de aanwezige Adafruit UF2-bootloader en SoftDevice-stack. Installeer of overschrijf de bootloader en SoftDevice niet met dit voorbeeld.</li>
				<li>Upload het programma als UF2-bestand volgens de uploadfiche. Na de herstart adverteert de Halberd als <code>Halberd-BLE</code>.</li>
				<li>Schakel Bluetooth in op de computer en installeer Python 3.9 of nieuwer.</li>
				<li>Open een terminal op de computer en installeer de Python-bibliotheek met <code>py -m pip install bleak</code>.</li>
			</ol>
		</div>
		<div class="info_item item">
			<h3 class="info_item_title">Berichtrichting</h3>
			<div class="dwengo_content table_container">
				<table>
					<tr><th>Van</th><th>Naar</th><th>Nordic UART-karakteristiek</th></tr>
					<tr><td>Computer</td><td>Halberd</td><td>RX: schrijven</td></tr>
					<tr><td>Halberd</td><td>Computer</td><td>TX: notificaties</td></tr>
				</table>
			</div>
			<p class="info_item_content">
				Verzend tekstberichten met een regeleinde (<code>\n</code>). Zo weet de Halberd waar een bericht eindigt.
			</p>
		</div>
	</div>

	<div class="dwengo_content dwengo-code-simulator">
		<pre>
<code class="language-cpp" data-filename="halberd_ble_uart.cpp">
#include &lt;bluefruit.h&gt;

BLEUart bleuart;
String ontvangenBericht;
unsigned long vorigBerichtTijdstip = 0;
unsigned int teller = 0;

void startAdvertising() {
  Bluefruit.Advertising.addFlags(BLE_GAP_ADV_FLAGS_LE_ONLY_GENERAL_DISC_MODE);
  Bluefruit.Advertising.addTxPower();
  Bluefruit.Advertising.addService(bleuart);
  Bluefruit.ScanResponse.addName();
  Bluefruit.Advertising.restartOnDisconnect(true);
  Bluefruit.Advertising.setInterval(32, 244);
  Bluefruit.Advertising.setFastTimeout(30);
  Bluefruit.Advertising.start(0);
}

void setup() {
  Bluefruit.begin();
  Bluefruit.setName("Halberd-BLE");
  bleuart.begin();
  startAdvertising();
}

void loop() {
  while (bleuart.available()) {
    char teken = (char) bleuart.read();

    if (teken == '\n') {
      bleuart.print("Halberd ontving: ");
      bleuart.println(ontvangenBericht);
      ontvangenBericht = "";
    } else {
      ontvangenBericht += teken;
    }
  }

  if (millis() - vorigBerichtTijdstip >= 2000) {
    vorigBerichtTijdstip = millis();
    bleuart.print("Teller van Halberd: ");
    bleuart.println(teller++);
  }
}
</code>
		</pre>
	</div>

	<div class="dwengo_content dwengo-code-simulator">
		<pre>
<code class="language-python" data-filename="halberd_ble.py">
import asyncio

from bleak import BleakClient, BleakScanner

APPARAATNAAM = "Halberd-BLE"
UART_RX = "6E400002-B5A3-F393-E0A9-E50E24DCCA9E"  # Computer schrijft naar Halberd.
UART_TX = "6E400003-B5A3-F393-E0A9-E50E24DCCA9E"  # Halberd stuurt notificaties naar computer.


def ontvangen_van_halberd(_, gegevens: bytearray):
    print("Halberd:", gegevens.decode("utf-8").strip())


async def main():
    print(f"Zoeken naar {APPARAATNAAM}...")
    apparaat = await BleakScanner.find_device_by_name(APPARAATNAAM, timeout=10.0)

    if apparaat is None:
        print("Halberd niet gevonden. Controleer of Bluetooth aanstaat en de Halberd adverteert.")
        return

    async with BleakClient(apparaat) as client:
        print("Verbonden. Berichten van de Halberd verschijnen hieronder.")
        await client.start_notify(UART_TX, ontvangen_van_halberd)

        while True:
            bericht = await asyncio.to_thread(input, "Bericht voor Halberd (stop om af te sluiten): ")
            if bericht.lower() == "stop":
                break

            await client.write_gatt_char(UART_RX, (bericht + "\n").encode("utf-8"), response=False)


asyncio.run(main())
</code>
		</pre>
	</div>

	<div class="items">
		<div class="info_item item">
			<h3 class="info_item_title">Testen</h3>
			<ol class="info_item_content">
				<li>Upload eerst het Halberd-programma en wacht tot de Halberd opnieuw is opgestart.</li>
				<li>Sla het Python-programma op als <code>halberd_ble.py</code>.</li>
				<li>Voer het uit met <code>py halberd_ble.py</code>.</li>
				<li>Typ een bericht en druk op Enter. De computer ontvangt daarna <code>Halberd ontving: ...</code>.</li>
				<li>Wacht ook twee seconden: de computer ontvangt dan <code>Teller van Halberd: ...</code>. Daarmee test je de richting van Halberd naar computer.</li>
				<li>Typ <code>stop</code> om de verbinding netjes te sluiten.</li>
			</ol>
		</div>
		<div class="info_item item">
			<h3 class="info_item_title">Problemen oplossen</h3>
			<ul class="info_item_content">
				<li>Verschijnt de Halberd niet? Druk eenmaal op de resetknop en start het Python-programma opnieuw. De Halberd moet als <code>Halberd-BLE</code> adverteren.</li>
				<li>Krijg je een fout over <code>bleak</code>? Installeer de bibliotheek in dezelfde Python-omgeving waarmee je het programma uitvoert: <code>py -m pip install bleak</code>.</li>
				<li>Gebruik de RX-UUID uitsluitend om van de computer naar de Halberd te schrijven en abonneer je uitsluitend op de TX-UUID voor berichten van de Halberd.</li>
			</ul>
		</div>
	</div>
</div>