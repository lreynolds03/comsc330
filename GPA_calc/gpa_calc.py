import os
import scipy.stats as stats
import re
import numpy as np  # Needed for mathematical operations such as square root

# Define the paths to the data directories
# Realtive path to the data directory
base_path = './COMSC330_Project/Data'
# Absolute path to the data directory
#base_path = '/Users/kocki/Desktop/PYTHON/COMSC330_Project/Data'
sections_path = os.path.join(base_path, 'Sections')
groups_path = os.path.join(base_path, 'Groups')
runs_path = os.path.join(base_path, 'Runs')

# Function to calculate GPA based on a detailed grading scale
def calculate_gpa(grades):
    """
    Calculates GPA considering detailed grading scale.
    Excludes non-GPA affecting grades like I, W, P, NP.
    """
    # Map of grade values
    grade_values = {
        'A+': 4.3, 'A': 4.0, 'A-': 3.7,
        'B+': 3.3, 'B': 3.0, 'B-': 2.7,
        'C+': 2.3, 'C': 2.0, 'C-': 1.7,
        'D+': 1.3, 'D': 1.0, 'D-': 0.7,
        'F': 0.0
    }
    # Filter out valid grades and calculate GPA
    valid_grades = [grade_values[grade] for grade in grades if grade in grade_values]
    return round(sum(valid_grades) / len(valid_grades) if valid_grades else 0, 1)

# Function to perform a single sample Z-test correctly
def perform_z_test(sample_mean, population_mean, population_std, n):
    """
    Computes the Z-score for a single sample against the population mean,
    considering the sample size for standard error calculation.
    """
    standard_error = population_std / np.sqrt(n)  # Calculate the standard error
    z_score = (sample_mean - population_mean) / standard_error  # Z-score formula
    return z_score

# Function to list available .run files and let the user choose one
def list_and_choose_run():
    """
    Lists available .run files and prompts the user to select one for processing.
    Validates user input and handles invalid inputs gracefully.
    """
    run_files = [f for f in os.listdir(runs_path) if f.endswith('.run')]
    print("Available .run files:")
    for idx, file in enumerate(run_files, start=1):
        print(f"{idx}. {file}")
    print("Enter the number of the run file you want to process, or 0 to exit:")

    while True:  # Input validation loop
        try:
            choice = input()
            if choice.strip() == '0':
                return None  # User chose to exit
            choice = int(choice)
            if 1 <= choice <= len(run_files):
                return run_files[choice - 1]  # Return the selected file name
            else:
                print("Invalid choice. Please enter a number from the list or 0 to exit.")
        except ValueError:
            print("Invalid input. Please enter a number.")

# Main function orchestrating the GPA analysis
def run_gpa_analysis(run_file):
    """
    Processes the selected run file to perform GPA analysis across groups and sections.
    Utilizes detailed grading scale and single-sample Z-test for significance comparison.
    """
    if run_file is None:
        return  # Exit if user chose not to select a run file

    with open(os.path.join(runs_path, run_file), 'r') as file:
        groups = file.read().splitlines()[1:]  # Ignore the first line (run name)

    for group_file in groups:
        with open(os.path.join(groups_path, group_file), 'r') as file:
            sections = file.read().splitlines()[1:]  # Ignore the first line (group name)
        
        group_gpas = []  # List to store all section GPAs within the group
        for section_file in sections:
            with open(os.path.join(sections_path, section_file), 'r') as file:
                lines = file.read().splitlines()
                section_name, credit_hours = re.split(r'\s{2,}', lines[0].strip())
                grades = [line.split(',')[-1].strip('"') for line in lines[1:]]  # Extract grades
                
                section_gpa = calculate_gpa(grades)
                group_gpas.append(section_gpa)
        
        group_gpa = sum(group_gpas) / len(group_gpas) if group_gpas else 0
        n = len(group_gpas)  # Number of sections for Z-test calculation
        
        # Comparing each section's GPA to the group's GPA using Z-test
        for section_gpa in group_gpas:
            z_score = perform_z_test(section_gpa, group_gpa, stats.tstd(group_gpas, ddof=1), n)
            significant_difference = z_score <= -2 or z_score >= 2
            print(f"Section GPA: {section_gpa}, Group GPA: {group_gpa:.1f}, Significant Difference: {significant_difference}")
        
        print(f"Group: {group_file}, Group GPA: {group_gpa:.1f}")

# Loop to continuously run the program until the user decides to exit
if __name__ == "__main__":
    while True:
        run_file_choice = list_and_choose_run()
        if run_file_choice is None:
            print("Program terminated by the user.")
            break
        run_gpa_analysis(run_file_choice)