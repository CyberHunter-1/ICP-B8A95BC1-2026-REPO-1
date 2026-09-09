import ipaddress


def validate_target(target: str) -> str:
    """
    Validate a single IPv4/IPv6 address or hostname.
    """

    try:
        return str(ipaddress.ip_address(target))
    except ValueError:
        if not target or len(target) > 253:
            raise ValueError(f"Invalid target: {target}")

        return target


def parse_ports(port_expression: str) -> list[int]:
    """
    Parse:

        80
        80,443
        20-25
        22,80,443
        1-1000
    """

    ports = set()

    for item in port_expression.split(","):
        item = item.strip()

        if "-" in item:
            start, end = item.split("-", 1)

            start = int(start)
            end = int(end)

            if start < 1 or end > 65535 or start > end:
                raise ValueError(f"Invalid port range: {item}")

            ports.update(range(start, end + 1))

        else:
            port = int(item)

            if not 1 <= port <= 65535:
                raise ValueError(f"Invalid port: {port}")

            ports.add(port)

    return sorted(ports)