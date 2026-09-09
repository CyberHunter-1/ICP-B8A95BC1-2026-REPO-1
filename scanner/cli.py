import argparse

from scanner.config import ScanConfig
from scanner.discovery.target import (
    parse_ports,
    validate_target
)
from scanner.engine.scanner import Scanner
from scanner.output.console import print_result
from scanner.output.json import save_json


def build_parser():

    parser = argparse.ArgumentParser(
        description="Modular Network Port Scanner"
    )

    parser.add_argument(
        "target",
        help="IPv4/IPv6 address or hostname"
    )

    parser.add_argument(
        "-p",
        "--ports",
        default="1-1024",
        help="Ports: 80,443 or 1-1024"
    )

    parser.add_argument(
        "--udp",
        action="store_true",
        help="Enable UDP scanning"
    )

    parser.add_argument(
        "-t",
        "--timeout",
        type=float,
        default=1.0
    )

    parser.add_argument(
        "-w",
        "--workers",
        type=int,
        default=50
    )

    parser.add_argument(
        "--json",
        help="Save results to JSON file"
    )

    return parser


def main():

    parser = build_parser()
    args = parser.parse_args()

    try:
        target = validate_target(args.target)
        ports = parse_ports(args.ports)

    except ValueError as error:

        parser.error(str(error))

    config = ScanConfig(
        timeout=args.timeout,
        workers=args.workers,
        udp=args.udp
    )

    scanner = Scanner(config)

    print(
        f"[+] Scanning {target}"
        f" ({len(ports)} ports)"
    )

    result = scanner.scan(
        target,
        ports
    )

    print_result(result)

    if args.json:

        save_json(
            result,
            args.json
        )

        print(
            f"[+] Results saved to {args.json}"
        )