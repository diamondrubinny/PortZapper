# ⚡ PortZapper

![License](https://img.shields.io/github/license/diamondrubinny/PortZapper?style=flat-square) ![Python](https://img.shields.io/badge/Python-3-3776AB?style=flat-square&logo=python&logoColor=white) ![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20macOS%20%7C%20Linux-lightgrey?style=flat-square)

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
    git clone https://github.com/diamondrubinny/PortZapper.git
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
```

### Force mode
Kill without the confirmation prompt (useful in scripts):

```bash
zapper 3000 -f
```

> Killing a process owned by another user may require an elevated terminal (`sudo` on macOS/Linux, *Run as administrator* on Windows).

## License
Distributed under the MIT License. See [LICENSE](LICENSE).

## 💼 Commercial license & rights acquisition

PortZapper is free and open source under the MIT License. If you are interested in a **commercial agreement** or custom licensing terms, **white-label / exclusive rights**, or **acquiring full rights to the code**, send your proposal to **[d@rubinny.net](mailto:d@rubinny.net)**.

Please include: who you are (company / contact), how you intend to use the code, and your offer.

> 🇮🇱 מעוניינים ברישיון מסחרי, בזכויות בלעדיות או ברכישת הזכויות בקוד? שלחו הצעה ל-**[d@rubinny.net](mailto:d@rubinny.net)** — כולל פרטי קשר, אופן השימוש המתוכנן וההצעה שלכם.

---

<sub>Created by **Diamond Rubinny** · © 2025–2026 Diamond Rubinny · [rubinny.co.il](https://rubinny.co.il)</sub>
