# MAS-004_ESP32-PLC-Bridge

Basis-Client und Daemon fuer die Kommunikation zur ESP32-PLC ueber TCP.

## Protokoll (vereinfacht)
- Unverschluesselt, textbasiert, zeilenweise.
- Schreiben: `KEY=VALUE\n`
- Lesen: `KEY=?\n`
- Antwort: optional `KEY=VALUE` oder `ACK/NAK`.

## Service-Dateien
- `systemd/mas004-esp32-plc-bridge.service`
- `scripts/install.sh`
- `scripts/run.sh`
- `scripts/default_config.json`

## Installation auf Raspi
```bash
cd /opt/MAS-004_ESP32-PLC-Bridge
python3 -m venv .venv
source .venv/bin/activate
pip install -U pip
pip install -e .
chmod +x scripts/*.sh
./scripts/install.sh
```

## Config
`/etc/mas004_esp32_plc_bridge/config.json`

- `enabled`: Service aktiv/inaktiv
- `simulation`: wenn `true`, keine Live-Verbindung
- `host`, `port`: ESP32 Endpoint
- `watchdog_host`: Host fuer Ping-Watchdog
- `timeout_s`, `poll_interval_s`
