from scanner.models import ScanResult


def print_result(result: ScanResult):

    print()
    print("=" * 65)
    print(f"Target: {result.target}")
    print(f"Started: {result.started_at}")
    print(f"Finished: {result.finished_at}")
    print("=" * 65)

    print(
        f"{'PORT':<8}"
        f"{'PROTO':<8}"
        f"{'STATE':<16}"
        f"{'SERVICE':<20}"
        f"{'LATENCY':<10}"
    )

    print("-" * 65)

    for item in result.ports:

        if item.state.value not in (
            "open",
            "open|filtered"
        ):
            continue

        latency = (
            f"{item.latency_ms} ms"
            if item.latency_ms is not None
            else "-"
        )

        print(
            f"{item.port:<8}"
            f"{item.protocol.value:<8}"
            f"{item.state.value:<16}"
            f"{(item.service or '-'):<20}"
            f"{latency:<10}"
        )

    print("=" * 65)