# PROJECT_CONTEXT - MAS-004_ESP32-PLC-Bridge

## Role in MAS-004
- Subproject (not orchestration owner).
- Provides ESP32 PLC transport/probe capability for MAS-004.
- Intended to be controlled/integrated by the main project `MAS-004_RPI-Databridge`.

## Repository Scope
- Package: `mas004_esp32_plc_bridge/`
- Main loop: `service.py`
- Client transport: `client.py`
- Config model: `config.py`
- Entry point: `mas004-esp32-bridge`

## Protocol Summary
- Plain TCP line protocol.
- Write: `KEY=VALUE\n`
- Read: `KEY=?\n`
- Optional watchdog ping via `ping3`.

## Runtime Paths
- Config: `/etc/mas004_esp32_plc_bridge/config.json`
- Systemd unit: `mas004-esp32-plc-bridge.service`
- Pi repo path: `/opt/MAS-004_ESP32-PLC-Bridge`

## Integration Boundary
- This repo should remain a transport/probe component.
- Parameter rules and business routing stay in the main Databridge repo.

## Last Reviewed
- Date: 2026-03-04
- Local HEAD baseline during creation: `154ff41`
