import re
from collections import Counter

def find_most_frequent_endpoint(log_file):
    """
    Identify the most frequently accessed endpoint in the log file.
    Args:
        log_file (str): Path to the log file.
    Returns:
        tuple: The most accessed endpoint and its access count.
    """
    endpoint_pattern = r'\"(?:GET|POST|PUT|DELETE) (\/\S*) HTTP'  # Pattern to extract endpoints
    endpoint_counter = Counter()

    with open(log_file, 'r') as file:
        for line in file:
            match = re.search(endpoint_pattern, line)
            if match:
                endpoint = match.group(1)
                endpoint_counter[endpoint] += 1

    # Find the most accessed endpoint
    most_common = endpoint_counter.most_common(1)  # Get the top-most endpoint
    if most_common:
        return most_common[0]  # Return the endpoint and its count
    else:
        return None, 0


if __name__ == "__main__":
    log_file_path = "sample.log"  # Path to your log file
    most_accessed_endpoint, access_count = find_most_frequent_endpoint(log_file_path)

    if most_accessed_endpoint:
        print("Most Frequently Accessed Endpoint:")
        print(f"{most_accessed_endpoint} (Accessed {access_count} times)")
    else:
        print("No endpoints found in the log file.")
