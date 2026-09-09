from dataclasses import dataclass


@dataclass
class ScanConfig:
    timeout: float = 1.0
    workers: int = 50

    tcp: bool = True
    udp: bool = False

    service_detection: bool = True
    banner_detection: bool = False

    verbose: bool = False