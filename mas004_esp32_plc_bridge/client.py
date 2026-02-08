from __future__ import annotations

import socket
from dataclasses import dataclass

from ping3 import ping


@dataclass
class EspWatchdog:
    host: str
    timeout_s: float = 1.0
    down_after: int = 3
    _fails: int = 0

    def check(self) -> bool:
        if not self.host:
            return True
        try:
            ok = ping(self.host, timeout=self.timeout_s, unit="s") is not None
        except Exception:
            ok = False
        self._fails = 0 if ok else (self._fails + 1)
        return self._fails < max(1, int(self.down_after))


class EspPlcBridgeClient:
    """
    Simple unencrypted line protocol client.
    Send: <key>=<value>\n or <key>=?\n
    Receive: optional single line (same format).
    """

    def __init__(self, host: str, port: int, timeout_s: float = 1.0, watchdog: EspWatchdog | None = None):
        self.host = (host or "").strip()
        self.port = int(port or 0)
        self.timeout_s = float(timeout_s)
        self.watchdog = watchdog

    def is_alive(self) -> bool:
        if self.watchdog is None:
            return True
        return self.watchdog.check()

    def read(self, key: str) -> str:
        return self.exchange(f"{key}=?")

    def write(self, key: str, value: str) -> str:
        return self.exchange(f"{key}={value}")

    def exchange(self, line: str) -> str:
        if not self.host or self.port <= 0:
            raise RuntimeError("ESP host/port not configured")
        if self.watchdog and not self.watchdog.check():
            raise RuntimeError("ESP watchdog reports down")

        payload = ((line or "").strip() + "\n").encode("utf-8")
        with socket.create_connection((self.host, self.port), timeout=self.timeout_s) as sock:
            sock.settimeout(self.timeout_s)
            sock.sendall(payload)
            return _recv_line(sock)


def _recv_line(sock: socket.socket, limit: int = 8192) -> str:
    data = bytearray()
    while len(data) < limit:
        chunk = sock.recv(1)
        if not chunk:
            break
        data.extend(chunk)
        if chunk == b"\n":
            break
    return bytes(data).decode("utf-8", errors="replace").strip()
