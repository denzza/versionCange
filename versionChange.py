import os
import re

def replace_versions(directory, replacements, excluded_files):
    report = {}
    excluded_report = []

    # Walk through each file in the directory
    for root, dirs, files in os.walk(directory):
        # Ignore '.git' directories
        dirs[:] = [d for d in dirs if d != '.git']
        for filename in files:
            filepath = os.path.join(root, filename)
            if filename in excluded_files:
                excluded_report.append(filepath)
                continue

            with open(filepath, 'r', encoding='ISO-8859-1') as file:
                filedata = file.read()

            # Use regular expressions to find the old versions and replace them
            for old_version, new_version in replacements.items():
                filedata, num_replacements = re.subn(old_version, new_version, filedata)
                if num_replacements > 0:
                    report[filepath] = report.get(filepath, 0) + num_replacements

            # If replacements were made, update the file
            with open(filepath, 'w', encoding='UTF-8') as file:
                file.write(filedata)

    return report, excluded_report