import os
import re

# Assuming the base_path is set relative to the script's location for simplicity
script_dir = os.path.dirname(__file__)  # Directory where the script is located
base_path = './COMSC330_Project/Data'
sections_path = os.path.join(base_path, 'Sections')
groups_path = os.path.join(base_path, 'Groups')
runs_path = os.path.join(base_path, 'Runs')

# Mapping grades to their corresponding GPA values
grade_values = {
    'A+': 4.3, 'A': 4.0, 'A-': 3.7,
    'B+': 3.3, 'B': 3.0, 'B-': 2.7,
    'C+': 2.3, 'C': 2.0, 'C-': 1.7,
    'D+': 1.3, 'D': 1.0, 'D-': 0.7,
    'F': 0.0
}

def calculate_gpa(grades):
    """Calculates GPA given a list of grades."""
    valid_grades = [grade_values[grade] for grade in grades if grade in grade_values]
    return round(sum(valid_grades) / len(valid_grades), 1) if valid_grades else 0

def list_and_choose_run():
    """Lists available .run files and prompts the user to select one for processing."""
    run_files = [f for f in os.listdir(runs_path) if f.endswith('.run')]
    print("Available .run files:")
    for idx, file in enumerate(run_files, start=1):
        print(f"{idx}. {file}")
    print("Enter the number of the run file you want to process, or 0 to exit:")

    while True:
        choice = input().strip()
        if choice == '0':
            return None
        elif choice.isdigit() and 1 <= int(choice) <= len(run_files):
            return run_files[int(choice) - 1]
        else:
            print("Invalid choice. Please enter a valid number from the list or 0 to exit.")

def run_gpa_analysis(run_file):
    """Analyzes GPA for groups and sections within a selected run file."""
    if run_file is None:
        print("Exiting program.")
        return
    
    with open(os.path.join(runs_path, run_file), 'r') as file:
        groups = file.read().splitlines()[1:]  # Skip the run name

    for group_file in groups:
        with open(os.path.join(groups_path, group_file), 'r') as file:
            sections = file.read().splitlines()[1:]  # Skip the group name
        
        group_gpas = []
        total_students = 0
        for section_file in sections:
            with open(os.path.join(sections_path, section_file), 'r') as file:
                lines = file.read().splitlines()
                grades = [line.split(',')[-1].strip('"') for line in lines[1:]]
                
                section_gpa = calculate_gpa(grades)
                group_gpas.append(section_gpa)
                total_students += len(grades)

                print(f"Section {section_file}: Students: {len(grades)}, GPA: {section_gpa}")
        
        group_gpa = round(sum(group_gpas) / len(group_gpas), 1) if group_gpas else 0
        print(f"Group {group_file}: Courses: {len(group_gpas)}, Students: {total_students}, GPA: {group_gpa}")

if __name__ == "__main__":
    while True:
        selected_run_file = list_and_choose_run()
        if selected_run_file is None:
            break
        run_gpa_analysis(selected_run_file)
