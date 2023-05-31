from versionChange import replace_versions

#############  CONFIG  ###########################################################
replacements = {
    'OLD_VERSION_1': 'NEW_VERSION_1',
    'OLD_VERSION_2': 'NEW_VERSION_2',
    # Add more old_version:new_version pairs as needed
}
# These are the files to be excluded from replacement
excluded_files = ['excluded_file_1.xsd', 'excluded_file_2.wsdl']

#exampel of project directory: 'C:/Application/Code/project_name' 
directory = '/path/to/your/project'

#############  END CONFIG  ########################################################

report, excluded_report = replace_versions(directory, replacements, excluded_files)

if not report:
    print("No replacements made in the project files")
else:
    for filepath, num_replacements in report.items():
        print(f'Replaced strings in {filepath} ({num_replacements} replacements)')

print("\nFiles excluded from replacement:")
for filepath in excluded_report:
    print(filepath)