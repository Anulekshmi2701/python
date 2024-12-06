import re
from collections import Counter

def count_requests_per_ip(log_file):
    """
    Count the number of requests made by each IP address from the log file.
    Args:
        log_file (str): Path to the log file.
    Returns:
        dict: Dictionary with IP addresses as keys and request counts as values.
    """
    ip_pattern = r'^(\d+\.\d+\.\d+\.\d+)'  # Pattern to extract IP addresses
    ip_counter = Counter()

    with open(log_file, 'r') as file:
        for line in file:
            match = re.match(ip_pattern, line)
            if match:
                ip = match.group(1)
                ip_counter[ip] += 1

    return ip_counter


def display_sorted_ip_requests(ip_counts):
    """
    Display the sorted list of IP addresses and their request counts.
    Args:
        ip_counts (Counter): Counter object with IP addresses and their counts.
    """
    print("IP Address           Request Count")
    print("--------------------  --------------")
    for ip, count in ip_counts.most_common():
        print(f"{ip:<20} {count}")


if __name__ == "__main__":
    log_file_path = "sample.log"  # Path to your log file
    ip_requests = count_requests_per_ip(log_file_path)
    display_sorted_ip_requests(ip_requests)
