# PortZapper

A cross-platform CLI utility to instantly find and kill processes locking a network port. 

Developers often encounter the `EADDRINUSE` error when restarting servers. PortZapper solves this by identifying the process holding the port and terminating it with a single command.

## Features

* **Cross-Platform:** Works on Windows, macOS, and Linux.
* **Safety First:** Identifies the process name (e.g., `node`, `python`, `nginx`) and asks for confirmation before killing.
* **Force Mode:** Supports a `-f` flag for automated scripts or quick termination.
* **Zero Dependencies:** Only requires `psutil`.

## Installation

1.  Clone the repository:
    ```bash
    git clone [https://github.com/YOUR_USERNAME/PortZapper.git](https://github.com/YOUR_USERNAME/PortZapper.git)
    cd PortZapper
    ```

2.  Install locally:
    ```bash
    pip install .
    ```

## Usage

### Basic Usage
To free up port 3000:

```bash
zapper 3000
