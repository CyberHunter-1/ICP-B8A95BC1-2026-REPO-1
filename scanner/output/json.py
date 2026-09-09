import json
from dataclasses import asdict

from scanner.models import ScanResult


def save_json(result: ScanResult, filename: str):

    with open(filename, "w", encoding="utf-8") as file:

        json.dump(
            asdict(result),
            file,
            indent=4
        )