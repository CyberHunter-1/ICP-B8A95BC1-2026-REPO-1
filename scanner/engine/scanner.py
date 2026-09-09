from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime, timezone

from scanner.config import ScanConfig
from scanner.detection.service import identify_service
from scanner.models import ScanResult
from scanner.protocols.tcp import TCPScanner
from scanner.protocols.udp import UDPScanner


class Scanner:

    def __init__(self, config: ScanConfig):

        self.config = config

        self.tcp_scanner = TCPScanner(
            timeout=config.timeout
        )

        self.udp_scanner = UDPScanner(
            timeout=config.timeout
        )

    def scan(self, target: str, ports: list[int]) -> ScanResult:

        started = datetime.now(timezone.utc).isoformat()

        result = ScanResult(
            target=target,
            started_at=started
        )

        jobs = []

        with ThreadPoolExecutor(
            max_workers=self.config.workers
        ) as executor:

            if self.config.tcp:

                for port in ports:
                    jobs.append(
                        executor.submit(
                            self.tcp_scanner.scan,
                            target,
                            port
                        )
                    )

            if self.config.udp:

                for port in ports:
                    jobs.append(
                        executor.submit(
                            self.udp_scanner.scan,
                            target,
                            port
                        )
                    )

            for job in as_completed(jobs):

                port_result = job.result()

                if (
                    self.config.service_detection
                    and port_result.state.value == "open"
                ):
                    port_result.service = identify_service(
                        port_result.port
                    )

                result.ports.append(port_result)

        result.ports.sort(
            key=lambda x: (x.protocol.value, x.port)
        )

        result.finished_at = datetime.now(
            timezone.utc
        ).isoformat()

        return result