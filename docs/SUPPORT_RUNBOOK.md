# SUPPORT_RUNBOOK - MAS-004_ESP32-PLC-Bridge

## 1. Positioning
- Subproject owned operationally by `MAS-004_RPI-Databridge`.
- Changes here must be validated against main project behavior.

## 2. Local Setup
- `python -m venv .venv`
- `.\.venv\Scripts\Activate.ps1`
- `python -m pip install -U pip`
- `python -m pip install -e .`

## 3. Pi Deployment
- Pull:
  - `ssh mas004-rpi "cd /opt/MAS-004_ESP32-PLC-Bridge && git pull --ff-only"`
- Restart:
  - `ssh mas004-rpi "sudo systemctl restart mas004-esp32-plc-bridge.service"`
- Logs:
  - `ssh mas004-rpi "sudo journalctl -u mas004-esp32-plc-bridge.service -n 120 --no-pager"`

## 4. Verification
- Service active: `systemctl is-active mas004-esp32-plc-bridge.service`
- Config values valid (`host`, `port`, `watchdog_host`, `simulation`).
- Probe messages stable (no repeated connect failures).

## 5. Sync Rule
- Use main repo scripts:
  - `MAS-004_RPI-Databridge/scripts/mas004_multirepo_status.ps1`
  - `MAS-004_RPI-Databridge/scripts/mas004_multirepo_sync.ps1`
- Do not force overwrite dirty Pi working trees.
