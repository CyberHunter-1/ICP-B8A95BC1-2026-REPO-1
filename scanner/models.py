from dataclasses import dataclass, field
from enum import Enum
from typing import Optional


class Protocol(str, Enum):
    TCP = "tcp"
    UDP = "udp"


class PortState(str, Enum):
    OPEN = "open"
    CLOSED = "closed"
    FILTERED = "filtered"
    OPEN_FILTERED = "open|filtered"
    UNKNOWN = "unknown"


@dataclass
class PortResult:
    port: int
    protocol: Protocol
    state: PortState
    service: Optional[str] = None
    banner: Optional[str] = None
    latency_ms: Optional[float] = None


@dataclass
class ScanResult:
    target: str
    started_at: str
    finished_at: Optional[str] = None
    ports: list[PortResult] = field(default_factory=list)

    @property
    def open_ports(self):
        return [
            result for result in self.ports
            if result.state == PortState.OPEN
        ]