import socket

from scanner.models import PortResult, Protocol, PortState


class UDPScanner:

    def __init__(self, timeout: float = 2.0):
        self.timeout = timeout

    def scan(self, target: str, port: int) -> PortResult:

        sock = socket.socket(
            socket.AF_INET,
            socket.SOCK_DGRAM
        )

        sock.settimeout(self.timeout)

        try:
            sock.sendto(b"", (target, port))

            try:
                data, _ = sock.recvfrom(1024)

                return PortResult(
                    port=port,
                    protocol=Protocol.UDP,
                    state=PortState.OPEN
                )

            except socket.timeout:
                return PortResult(
                    port=port,
                    protocol=Protocol.UDP,
                    state=PortState.OPEN_FILTERED
                )

        except ConnectionRefusedError:
            return PortResult(
                port=port,
                protocol=Protocol.UDP,
                state=PortState.CLOSED
            )

        except OSError:
            return PortResult(
                port=port,
                protocol=Protocol.UDP,
                state=PortState.FILTERED
            )

        finally:
            sock.close()