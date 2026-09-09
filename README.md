# Network Port Scanner

A modular Python-based network port scanner for identifying TCP and UDP network services on authorized hosts.

The project is designed as a beginner-level cybersecurity application while introducing practical concepts such as network sockets, TCP/UDP protocols, concurrency, service identification, input validation, and structured security reporting.

> **Authorized use only:** Scan systems and networks that you own or have explicit permission to test.

---

## Project Overview

### Real-World Problem

Network administrators and security professionals need to identify which network services are exposed on a host.

An open port can indicate that a service is listening and potentially reachable over the network. Port scanning is therefore an important part of:

* Network administration
* Asset discovery
* Security assessments
* Attack-surface identification
* Troubleshooting
* Authorized penetration testing

### Difficulty

**Beginner**

### Primary Language

**Python**

### Key Technologies

* Python `socket`
* TCP
* UDP
* Thread-based concurrency
* Regular Python data structures
* JSON
* Command-line interfaces
* Unit testing

---

# Features

The scanner is designed to support:

* TCP port scanning
* UDP port scanning
* Custom port ranges
* Individual port selection
* Multiple-port selection
* Concurrent scanning
* Configurable connection timeout
* Configurable worker count
* Basic service identification
* Port-state classification
* Terminal reporting
* JSON reporting
* Target validation
* Port-range validation
* Modular architecture

---

# Project Architecture

```text
                         main.py
                            │
                            ▼
                           CLI
                            │
                            ▼
                     Scanner Engine
                            │
              ┌─────────────┴─────────────┐
              │                           │
              ▼                           ▼
        TCP Scanner                  UDP Scanner
              │                           │
              └─────────────┬─────────────┘
                            ▼
                    Service Detection
                            │
                            ▼
                       Scan Results
                            │
                  ┌─────────┴─────────┐
                  ▼                   ▼
              Console               JSON
               Output              Report
```

---

# Directory Structure

```text
network-port-scanner/
│
├── main.py
├── README.md
├── requirements.txt
├── pyproject.toml
├── .gitignore
│
├── scanner/
│   ├── __init__.py
│   ├── cli.py
│   ├── config.py
│   ├── models.py
│   │
│   ├── discovery/
│   │   ├── __init__.py
│   │   ├── host.py
│   │   └── target.py
│   │
│   ├── protocols/
│   │   ├── __init__.py
│   │   ├── tcp.py
│   │   └── udp.py
│   │
│   ├── detection/
│   │   ├── __init__.py
│   │   ├── service.py
│   │   └── banner.py
│   │
│   ├── engine/
│   │   ├── __init__.py
│   │   ├── scanner.py
│   │   └── workers.py
│   │
│   ├── output/
│   │   ├── __init__.py
│   │   ├── console.py
│   │   ├── json.py
│   │   └── csv.py
│   │
│   └── utils/
│       ├── __init__.py
│       ├── logging.py
│       └── ports.py
│
└── tests/
    ├── test_target.py
    ├── test_tcp.py
    ├── test_udp.py
    └── test_models.py
```

---

# Module Responsibilities

## `main.py`

The single application entry point.

```text
main.py
   ↓
scanner.cli
```

Run the application with:

```bash
python3 main.py
```

---

## `scanner/cli.py`

Handles:

* Command-line arguments
* Target input
* Port input
* Timeout configuration
* Worker configuration
* UDP selection
* JSON output

---

## `scanner/models.py`

Contains the application's data models.

Example:

```python
PortResult
ScanResult
Protocol
PortState
```

This gives all modules a common representation of scan results.

---

## `scanner/discovery/`
