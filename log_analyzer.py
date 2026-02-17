

import pandas as pd

from datetime import datetime

import logging


# Configure basic logging

logging.basicConfig(filename='log_analyzer.log', level=loggingclilogging.INFO)

logger = logging.getLogger()


def read_logs(file_path):

    try:

        df = pd.read_csv(file_path, parse_dates=['timestamp'])

        logger.info('Logs successfully loaded')

        return df

    except Exception as e:

        logger.error(f'Error reading logs file: {e}', exc_info=True)

        raise


def filter_by_level(df, log_level):

    try:

        filtered_logs = df[df['level'] == log_level]

        logger.info(f'Filtered logs by level {log_level}')

        return filtered_logs

    except Exception as e:

        logger.error(f'Error filtering logs by level: {e}', exc_info=True)

        raise


def count_entries_by_service(df):

    try:

        entry_counts = df['service'].value_counts()

        logger.info('Counted entries for each service')

        return entry_counts

    except Exception as e:

        logger.error(f'Error counting log entries by services: {e}', exc_info=True)

        raise


def most_common_ip(df):

    try:

        common_ips = df['clientIP'].mode().iloc[0]

        logger.info('Identified the most frequent IP')

        return common_ips

    except Exception as e:

        logging.error(f'Error identifying most common IPs in logs: {e}', exc_info=True)

        raise


def main():

    try:

        log_df = read_logs('example.log')  # Replace with the path to your actual log file

        if not pd.isnull(log_df).any().item():

            high_severity_logs = filter_by_level(log_df, 'ERROR')

            print("High Severity Logs:\n", high_severity_logs)

            
            service_counts = count_entries_by_service(log_df)

            for service, count in service_counts.items():

                logging.info(f'{service} appears {count} times')

                
            frequent_ip = most_common_ip(log_df)

            print("Most Common IP:", frequent_ip)

        else:

            logger.warning('Empty logs, no entries to analyze')

    except Exception as e:

        logging.error('General error during log analysis', exc_info=True)


if __name__ == "__main__":

    main()

