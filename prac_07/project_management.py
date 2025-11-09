"""
Project Management
Estimate: 100 minutes
Actual:    minutes
"""
from prac_07.project import Project
import datetime

FILENAME = 'projects.txt'
MENU="""
- (L)oad projects  
- (S)ave projects  
- (D)isplay projects  
- (F)ilter projects by date
- (A)dd new project  
- (U)pdate project
- (Q)uit"""
NAME_INDEX=0
DATE_INDEX=1
PRIORITY_INDEX=2
COST_INDEX=3
COMPLETED_PERCENTAGE_INDEX=4
DATA_LENGTH=5
MINIMUM_VALUE=0
MAXIMUM_VALUE=100
DATE_FORMAT = "%d/%m/%Y"

def main():
    """Run the Project Management Program, loading and saving data."""
    print("Welcome to Pythonic Project Management")
    projects=load_data(FILENAME)
    choice=input(f"{MENU}\n>>>").upper()
    while choice != 'Q':
        if choice == 'L':
            filename = input("Please enter filename:")
            projects=load_data(filename)
        elif choice == "D":
            display_projects(projects)
        elif choice == "U":
            update_projects(projects)
        elif choice == "A":
            add_new_projects(projects)
        elif choice == "F":
            filter_project(projects)
        elif choice == "S":
            save_projects(projects)
        else:
            print("Invalid choice, please try again.")
        choice = input(f"{MENU}\n>>>").upper()
    save_choice=input(f"Would you like to save to {FILENAME}?").upper()
    if save_choice == 'Y':
        save_projects(projects)
    print("Thank you for using custom-built project management software.")

def load_data(filename):
    """Load project data from the file, returning a list of Project objects."""
    projects = []
    try:
        with open(filename,"r") as in_file:
            in_file.readline()  # Skip header line
            for line in in_file:
                parts = line.strip().split('\t')
                if len(parts)==DATA_LENGTH:
                    date_string=parts[DATE_INDEX]
                    date = datetime.datetime.strptime(date_string, DATE_FORMAT).date()
                    projects.append(Project(parts[NAME_INDEX],date,int(parts[PRIORITY_INDEX]),float(parts[COST_INDEX]),int(parts[COMPLETED_PERCENTAGE_INDEX])))
    except FileNotFoundError:
        print(f"Sorry,{filename} not found.")
    print(f"Loaded {len(projects)} projects from {filename}")
    return projects

def display_projects(projects):
    """Display incomplete and completed projects, sorted by priority."""
    incompleted_projects=[project for project in projects if project.completed_percentage < 100]
    completed_projects=[project for project in projects if project.completed_percentage == 100]
    incompleted_projects.sort()
    completed_projects.sort()
    print("Incomplete projects: ")
    for project in incompleted_projects:
        print(f"\t{project}")
    print("Completed projects: ")
    for project in completed_projects:
        print(f"\t{project}")

def update_projects(projects):
    """Select a project and update its completion percentage and priority."""
    for i,project in enumerate(projects,0):
        print(f"{i} {project}")
    try:
        project_choice=int(input("Project choice:"))
        if not project_choice <0 or project_choice >= len(projects):
            print(projects[project_choice])
            new_percentage =int(input("New percentage:"))
            if not new_percentage < MINIMUM_VALUE or new_percentage > MAXIMUM_VALUE:
                projects[project_choice].completed_percentage=new_percentage
            new_priority=int(input("new priority:"))
            if not new_priority < MINIMUM_VALUE or new_priority > MAXIMUM_VALUE:
                projects[project_choice].priority=new_priority
    except ValueError:
        print("Invalid number.")


def get_valid_input(prompt,number_type):
    """Get a valid input from the user."""
    value = get_valid_number(prompt,number_type)
    while value < MINIMUM_VALUE or value > MAXIMUM_VALUE:
        print(f"Invalid {prompt}, please try again.")
        value = get_valid_number(prompt, number_type)
    return value


def add_new_projects(projects):
    """Add a new project to the list based on user input."""
    print("Let's add a new project")
    name=input("Name:")
    start_date_string=input("Start date (dd/mm/yy):")
    priority=get_valid_input("priority",int)
    estimate_cost = get_valid_estimated_cost()
    completed_percentage=get_valid_input("Percent complete:",int)
    start_date = datetime.datetime.strptime(start_date_string, DATE_FORMAT).date()
    projects.append(Project(name,start_date,priority,estimate_cost,completed_percentage))


def get_valid_estimated_cost():
    """Get a valid estimated cost."""
    estimate_cost = get_valid_number("Cost estimate: $", float)
    while estimate_cost < 0:
        print("Invalid estimate_cost, please try again.")
        estimate_cost = get_valid_number("Cost estimate:", float)
    return estimate_cost


def filter_project(projects):
    """Filter and display projects starting on or after a specified date."""
    filer_date_string=input("Show projects that start after date (dd/mm/yy):")
    filer_date = datetime.datetime.strptime(filer_date_string, DATE_FORMAT).date()
    filter_dates=[project for project in projects if project.start_date >= filer_date]
    for project in filter_dates:
        print(project)

def save_projects(projects):
    """Save all projects to a file"""
    filename=input("Please enter filename to save the projects:")
    if len(filename.strip()) == 0:
        filename=FILENAME
    with open(filename,"w") as out_file:
        print("Name	Start Date\tPriority\tCost Estimate\tCompletion Percentage",file=out_file)
        for project in projects:
            print(",".join([project.name,str(project.start_date),str(project.priority),
                            str(project.estimate_cost),str(project.completed_percentage)]),file=out_file)
    print(f"{len(projects)} projects have been saved to {filename}.")

def get_valid_number(prompt,number_type):
    """Get a valid number from the user."""
    is_valid=False
    number=0 #Set the initial value to 0
    while not is_valid:
        try:
            number=number_type(input(f"{prompt.title()}:"))
            is_valid=True
        except ValueError:
            print("Invalid input. Try again.")
    return number

main()







