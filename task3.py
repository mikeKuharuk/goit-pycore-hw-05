import re
import sys
from collections import defaultdict


def parse_log_line(line: str) -> dict | None:
    if not isinstance(line, str) or line == "":
        return None

    date_time_pattern = r"\d{4}-\d\d-\d\d \d\d:\d\d:\d\d "
    match = re.search(date_time_pattern, line)
    if not match:
        return None

    log_timing = match.group(0)
    line = re.sub(date_time_pattern, "", line)

    log_tag, log_line = line.split(" ", 1)
    log_tag = log_tag.strip()

    parsed_line = {
        "date": log_timing,
        "tag": log_tag,
        "line": log_line,
    }
    return parsed_line

def load_logs(file_path: str) -> list:
    file_content = ""
    try:
        with open(file_path) as file:
            file_content = file.read()
    except FileNotFoundError:
        print("File not found!")
        return []

    log_lines = file_content.split("\n")
    formated_logs = list(filter(None, map(parse_log_line, log_lines)))

    return formated_logs

def filter_logs_by_level(logs: list, level: str) -> list:
    filtered_logs = []
    for log in logs:
        if log["tag"] == level.upper():
            filtered_logs.append(log)
    return filtered_logs

def count_logs_by_level(logs: list) -> dict:
    logs_count = defaultdict(int)
    for log in logs:
        logs_count[log["tag"]] += 1
    return logs_count

def display_log_counts(counts: dict):

    # Formating metadata to support any tags with same format output with nice table
    first_column_name = "Log counts"
    second_column_name = "Amount"
    divider = "|"
    max_header_size = max([len(key) for key in counts])
    inner_spacing = 2
    outer_spacing = 4

    # Visually separating logs program output
    print("\n")

    title_string = f"{outer_spacing * " " + max_header_size * " " + first_column_name +
             inner_spacing * " " + divider + inner_spacing * " " + second_column_name}"
    print(title_string)

    subtitle_string = f"{(outer_spacing + max_header_size + len(first_column_name) + inner_spacing)*"-"+
                         divider + (inner_spacing+len(second_column_name)+outer_spacing)*"-"}"
    print(subtitle_string)

    for tag, count in counts.items():
        spase_size = ((max_header_size - len(tag)) + inner_spacing + len(first_column_name) + outer_spacing)
        print(f"{tag + spase_size * " " + divider + " " + str(count)}")

def display_logs(logs: list):
    if len(logs) == 0:
        print("No logs found")

    for log in logs:
        print(f"{log['date']}- {log['line']}")

def main():

    if len(sys.argv) > 1:
        # Expected that first argument is path to target folder, all other args ignored
        directory_in_sys_argument = sys.argv[1]
        logs = load_logs(directory_in_sys_argument)
        log_counts = count_logs_by_level(logs)
        display_log_counts(log_counts)

        if len(sys.argv) == 3:
            print(f"\n Log details for level '{str(sys.argv[2]).upper()}':")
            filtered_logs = filter_logs_by_level(logs, sys.argv[2])
            display_logs(filtered_logs)

    else:
        print("No args provided! Please provide a directory path as argument")

        directory_in_sys_argument = "logs.log"
        logs = load_logs(directory_in_sys_argument)
        log_counts = count_logs_by_level(logs)
        display_log_counts(log_counts)

if __name__ == "__main__":
    main()
