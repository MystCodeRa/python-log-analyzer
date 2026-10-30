
# Import required libraries
import re
from collections import Counter


# Define a function to analyze security log files
def analyze_logs(file_path):

    # Store analysis results and initialize counters
    results = {
        "total_events": 0,
        "successful_logins": 0,
        "failed_logins": 0,
        "unauthorized_access": 0,
        "failed_ips": Counter(),
        "unauthorized_ips": Counter()
    }

    # Open the log file in read mode
    with open(file_path, "r", encoding="utf-8") as file:

        # Read the file line by line
        for line in file:

            # Remove unnecessary whitespace and newline characters
            line = line.strip()

            # Skip empty lines
            if not line:
                continue

            # Count each non-empty log entry
            results["total_events"] += 1

            # Search for an IPv4 address in the current log entry
            ip_match = re.search(
                r"\b(?:\d{1,3}\.){3}\d{1,3}\b",
                line
            )

            # Extract the IP address if a match is found
            ip = ip_match.group() if ip_match else None

            # Identify successful login attempts
            if "Login successful" in line:
                results["successful_logins"] += 1

            # Identify failed login attempts
            elif "Failed login" in line:
                results["failed_logins"] += 1

                # Count failed attempts for each IP address
                if ip:
                    results["failed_ips"][ip] += 1

            # Identify unauthorized access events
            elif "Unauthorized access" in line:
                results["unauthorized_access"] += 1

                # Track unauthorized access by IP address
                if ip:
                    results["unauthorized_ips"][ip] += 1

    # Return all collected analysis results
    return results
