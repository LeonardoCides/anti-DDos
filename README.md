# 🛡️ Sentinel-DDoS: Detection & Mitigation System

![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![PHP](https://img.shields.io/badge/PHP-8.x-777BB4?style=for-the-badge&logo=php&logoColor=white)
![Status](https://img.shields.io/badge/Status-In--Development-orange?style=for-the-badge)

A hybrid defense system designed to monitor network traffic, identify anomalous patterns, and mitigate Distributed Denial of Service (DDoS) attacks in real-time.

---

## 🏗️ Architecture

This project uses a dual-stack architecture to balance performance and accessibility:

* **Python Engine (Backend):** Handles raw socket sniffing, packet inspection (L3/L4/L7), and real-time analysis using statistical thresholds.
* **PHP Dashboard (Frontend/API):** Provides a web-based interface to visualize attack logs, manage IP blacklists, and configure mitigation rules.

## ✨ Features

* **Real-time Traffic Analysis:** Monitors packet velocity and connection states.
* **Threshold-Based Mitigation:** Automatically triggers defensive actions (via IPTables/NFTables) when traffic exceeds defined limits.
* **Web Dashboard:** Live monitoring of requests, bandwidth usage, and blocked IP history.
* **Adaptive Filtering:** Identifies and blocks common patterns like SYN Flood, UDP Flood, and ICMP Smurfing.
* **Persistent Logging:** Detailed logs stored for forensic analysis.

## 🛠️ Tech Stack

- **Python 3.x:** Using `scapy`, `requests`, and `psutil`.
- **PHP 8.x:** Core engine for the administrative dashboard.
- **Database:** MySQL/MariaDB (to store logs and blacklists).
- **System Integration:** Linux IPTables for hardware-level blocking.

---

## 🚀 Quick Start

### 1. Requirements
Ensure you have the following installed:
- Linux OS (Ubuntu/Debian recommended)
- Python 3.10+
- Apache/Nginx + PHP 8.1+
- Root privileges (required for packet manipulation)

### 2. Installation
```bash
# Clone the repository
git clone [https://github.com/youruser/sentinel-ddos.git](https://github.com/LeonardoCides/anti-DDos)
cd anti-DDos


# Install Python dependencies
pip install -r requirements.txt

# Configure the Web Dashboard
cp dashboard/config.sample.php dashboard/config.php
