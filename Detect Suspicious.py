import re
from collections import Counter

def detect_suspicious_activity(log_file, threshold=10):
    """
    Detect suspicious activity by identifying IPs with failed login attempts exceeding a threshold.
    Args:
        log_file (str): Path to the log file.
        threshold (int): Maximum allowed failed login attempts per IP before flagging.
    Returns:
        dict: Dictionary of flagged IPs and their failed login counts.
    """
    ip_pattern = r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'  # Pattern to extract IP addresses
    failure_pattern = r'HTTP/1\.\d" 401'  # Pattern to identify failed logins (HTTP 401 status)
    failed_logins = Counter()

    with open(log_file, 'r') as file:
        for line in file:
            if re.search(failure_pattern, line):  # Check for failed login entry
                ip_match = re.search(ip_pattern, line)
                if ip_match:
                    ip_address = ip_match.group(1)
                    failed_logins[ip_address] += 1

    # Filter IPs exceeding the threshold
    flagged_ips = {ip: count for ip, count in failed_logins.items() if count > threshold}
    return flagged_ips


if __name__ == "__main__":
    log_file_path = "sample.log"  # Path to your log file
    threshold = 10  # Configure the threshold for failed login attempts
    suspicious_ips = detect_suspicious_activity(log_file_path, threshold)

    if suspicious_ips:
        print("Suspicious Activity Detected:")
        print(f"{'IP Address':<20}{'Failed Login Attempts'}")
        for ip, count in suspicious_ips.items():
            print(f"{ip:<20}{count}")
    else:
        print("No suspicious activity detected.")
