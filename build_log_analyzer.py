

import re

from collections import Counter

from datetime import datetime

import pandas as pd


def parse_log(file_path):

    with open(file_path, 'r') as file:

        log_data = file.read()

    return log_data


def extract_errors(log_data):

    error_patterns = ['.*ERROR.*', '.*(Exception|crash).*']

    errors = []

    for pattern in error_patterns:

        matches = re.finditer(pattern, log_data)

        for match in matches:

            timestamp = datetime.strptime(match.group(1), '%Y-%m-%d %H:%M:%S')

            message = match.group().split('ERROR', 1)[1] if 'ERROR' in match.group() else match.group()[len('Exception'):].strip()

            errors.append((timestamp, message))

    return sorted(errors, key=lambda x: x[0])


def main():

    log_data = parse_log('system.log')

    error_logs = extract_errors(log_data)


    df = pd.DataFrame(error_logs, columns=['Timestamp', 'Error Message'])

    print(df)


if __name__ == '__main__ider: