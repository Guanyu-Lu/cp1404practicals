"""
CP1404/CP5632 Practical
Data file -> lists program
"""
FILENAME = "subject_data.txt"

def main():
    """Loads subject data from a file and prints a formatted report."""
    subject_datas = load_subject_data(FILENAME)
    print(subject_datas)
    print_subject_details(subject_datas)

def load_subject_data(filename=FILENAME):
    """Read subject data from file formatted like: subject,lecturer,number of students."""
    with open(filename,"r") as input_file:
        subject_datas=[line.strip("\n").split(",") for line in input_file]
    for subject_data in subject_datas:
        subject_data[2] = int(subject_data[2])
    return subject_datas

def  print_subject_details(subject_datas):
    """ print subject details from the data file."""
    for subject_data in subject_datas:
        print(f"{subject_data[0]} is taught by {subject_data[1]:12} and has {subject_data[2]:>3} students")

main()
