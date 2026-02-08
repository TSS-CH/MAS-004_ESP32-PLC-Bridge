# MAS-004_ESP32-PLC-Bridge

Basis-Client fuer die Kommunikation zur ESP32-PLC ueber TCP.

## Protokoll (vereinfacht)
- Unverschluesselt, textbasiert, zeilenweise.
- Schreiben: `KEY=VALUE\n`
- Lesen: `KEY=?\n`
- Antwort: optional `KEY=VALUE` oder `ACK/NAK`.

## Watchdog
- Optionaler Ping-Watchdog via `ping3`.
- Bei `down_after` aufeinanderfolgenden Fehlern wird das Device als down betrachtet.

## Beispiel
```python
from mas004_esp32_plc_bridge import EspPlcBridgeClient, EspWatchdog

wd = EspWatchdog(host="192.168.2.10", timeout_s=1.0, down_after=3)
cli = EspPlcBridgeClient("192.168.2.10", 5000, timeout_s=1.0, watchdog=wd)
print(cli.write("TTP00002", "8"))
```
