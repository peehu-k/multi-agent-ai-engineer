

import json

from datetime import datetime, timedelta


def generate_error_report():
    one_week_ago = datetime.now() - timedelta(days=7)
    
    logs_filepath = 'application_logs.json'
    report_filename = 'error_report.json'
    
    try:
        with open(logs_filepath, 'r') as log_file:
            logs = json.load(log_file)
            
        error_patterns = {}
        
        for entry in (entry['timestamp'] for entry in logs if one_week_ago <= datetime.fromisoformat(entry['timestamp']) <= datetime.now()):
            error_type = entry['type'].lower().replace('Error', '')  # Normalize and simplify the key by removing 'Error' prefix/suffix
            error_patterns[error_type] = error_patterns.get(error_type, 0) + 1
        
        with open(report_filename, 'w') as report_file:
            json.dump(error_patterns, reports_file, indent=2)
            
    except FileNotFoundError:
        print(f"The logs file {logs_filepath} does not exist.")
    except ValueError:  # In case of malformed timestamps or errors within the parsing logic.
        print("There was an error processing some log entries, please check for correct timestamp formats and valid types in your logs.")
    
    return report_filename if os.path.exists(report_filename) else None
