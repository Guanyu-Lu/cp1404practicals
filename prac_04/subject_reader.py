"""
CP1404/CP5632 Practical
Data file -> lists program
"""
FILENAME = "subject_data.txt"

def main():
    """Loads subject data from a file and prints a formatted report."""
    datas = load_data(FILENAME)
    print(datas)
    print_subject_details(datas)

def load_data(filename=FILENAME):
    """Read data from file formatted like: subject,lecturer,number of students."""
    with open(filename,"r") as input_file:
        datas=[line.strip("\n").split(",") for line in input_file]
    for data in datas:
        data[2] = int(data[2])
    return datas

def  print_subject_details(datas):
    """ print subject details from the data file."""
    for data in datas:
        print(f"{data[0]} is taught by {data[1]:12} and has {data[2]:>3} students")

main()
