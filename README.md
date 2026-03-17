# MAS-004_ESP32-PLC-Bridge

Basis-Client und Daemon fuer die Kommunikation zur ESP32-PLC ueber TCP.

## Python fuer Schulung und Entwicklung
- Teamstandard fuer neue Entwicklungsrechner: `Python 3.13.x`
- `Python 3.12.x` ist als Fallback okay, wenn `3.13` auf dem Zielsystem nicht sauber verfuegbar ist
- `Python 3.14` derzeit nicht als Schulungsstandard verwenden
- `requires-python = ">=3.9"` im `pyproject.toml` beschreibt nur die technische Mindestversion, nicht die empfohlene Teamversion

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
python3.13 -m venv .venv
# alternativ auf Systemen ohne 3.13: python3.12 -m venv .venv
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
