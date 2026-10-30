# Python Log Analyzer

A lightweight cybersecurity tool developed with Python to analyze system log files and identify potentially suspicious activities.

## Features

- Log file reading and analysis
- Successful login detection
- Failed login attempt detection
- Unauthorized access detection
- IP address extraction
- Suspicious IP identification based on failed login thresholds
- Security event reporting
- Automated unit testing

## Technologies

- Python 3
- Regular Expressions (Regex)
- Collections (Counter)
- Unittest

## Project Structure

```text
python-log-analyzer/
│
├── main.py
├── log_analyzer.py
├── sample.log
├── README.md
├── requirements.txt
│
└── tests/
    └── test_analyzer.py
```

## Installation

Clone the repository:

```bash
git clone YOUR_REPOSITORY_URL
```

Navigate to the project directory:

```bash
cd python-log-analyzer
```

No external dependencies are required.

## Usage

Run the analyzer:

```bash
python3 main.py
```

## Run Tests

Execute automated tests:

```bash
python3 -m unittest discover -s tests -v
```

## Example Output

```text
===== LOG ANALYSIS =====

Total Events: 10
Successful Logins: 3
Failed Logins: 5
Unauthorized Access: 2

===== SUSPICIOUS ACTIVITY REPORT =====

[WARNING] Suspicious IP: 192.168.1.15 (3 failed attempts)

===== UNAUTHORIZED ACCESS REPORT =====

[CRITICAL] Unauthorized access: 192.168.1.20 (2 events)
```

## Detection Logic

The analyzer identifies IP addresses with three or more failed login attempts and flags them as suspicious.

## Learning Objectives

This project was developed to practice:

- Python file handling
- Regular expressions
- Data structures
- Conditional statements
- Functions
- Basic cybersecurity concepts
- Unit testing

## Disclaimer

This project is intended for educational purposes. It uses sample log data and does not perform real-time network monitoring.

## Future Improvements

- Export reports to CSV
- Add timestamp filtering
- Validate IPv4 addresses
- Support additional log formats
- Add graphical statistics

## Author

Developed as a first-year Computer Science learning project.