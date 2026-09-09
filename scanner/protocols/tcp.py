import socket
import time

from scanner.models import PortResult, Protocol, PortState


class TCPScanner:

    def __init__(self, timeout: float = 1.0):
        self.timeout = timeout

    def scan(self, target: str, port: int) -> PortResult:

        start = time.perf_counter()

        sock = socket.socket(
            socket.AF_INET,
            socket.SOCK_STREAM
        )

        sock.settimeout(self.timeout)

        try:
            result = sock.connect_ex((target, port))

            latency = (time.perf_counter() - start) * 1000

            if result == 0:
                state = PortState.OPEN
            else:
                state = PortState.CLOSED

            return PortResult(
                port=port,
                protocol=Protocol.TCP,
                state=state,
                latency_ms=round(latency, 2)
            )

        except socket.timeout:
            return PortResult(
                port=port,
                protocol=Protocol.TCP,
                state=PortState.FILTERED
            )

        except OSError:
            return PortResult(
                port=port,
                protocol=Protocol.TCP,
                state=PortState.FILTERED
            )

        finally:
            sock.close()