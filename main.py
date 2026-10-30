
from log_analyzer import analyze_logs

results = analyze_logs("sample.log")

print("===== LOG ANALYSIS =====")

print("Total Events:", results["total_events"])
print("Successful Logins:", results["successful_logins"])
print("Failed Logins:", results["failed_logins"])
print("Unauthorized Access:", results["unauthorized_access"])

print("\nFailed Login IP Addresses:")

for ip, count in results["failed_ips"].items():
    print(f"{ip}: {count} attempts")



    
# Define the threshold for suspicious login attempts
SUSPICIOUS_THRESHOLD = 3

print("\n===== SUSPICIOUS ACTIVITY REPORT =====")

# Check each IP address for repeated failed login attempts
suspicious_found = False

for ip, count in results["failed_ips"].items():

    # Flag IP addresses that reach the threshold
    if count >= SUSPICIOUS_THRESHOLD:
        print(f"[WARNING] Suspicious IP: {ip} ({count} failed attempts)")
        suspicious_found = True

# Display a message if no suspicious activity is detected
if not suspicious_found:
    print("No suspicious activity detected.")


    
# Display unauthorized access events
print("\n===== UNAUTHORIZED ACCESS REPORT =====")

# Check whether any unauthorized access was detected
if results["unauthorized_ips"]:

    # Display each IP address associated with unauthorized access
    for ip, count in results["unauthorized_ips"].items():
        print(f"[CRITICAL] Unauthorized access: {ip} ({count} events)")

else:
    print("No unauthorized access detected.")






