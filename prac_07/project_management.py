"""
Project Management
Estimate: 100 minutes
Actual:    minutes
"""
#from operator import itemgetter
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

def main():
    print("Welcome to Pythonic Project Management")
    projects=load_data()
    choice=input(f"{MENU}\n>>>").upper()
    while choice != 'Q':
        if choice == "D":
            display_projects(projects)
        elif choice == "U":
            update_projects(projects)
        choice = input(f"{MENU}\n>>>").upper()

def load_data():
    projects = []
    try:
        with open(FILENAME,"r") as in_file:
            in_file.readline()
            for line in in_file:
                parts = line.strip().split('\t')
                if len(parts)==5:
                    date_string=parts[1]
                    date = datetime.datetime.strptime(date_string, "%d/%m/%Y").date()
                    projects.append(Project(parts[0],date,int(parts[2]),float(parts[3]),int(parts[4])))
    except FileNotFoundError:
        print(f"Sorry,{FILENAME} not found.")
    print(f"Loaded {len(projects)} projects from {FILENAME}")
    return projects

def display_projects(projects):
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
    for i,project in enumerate(projects,0):
        print(f"{i} {project}")
    project_choice=int(input("Project choice:"))
    if not project_choice <0 or project_choice >= len(projects):
        print(projects[project_choice])
        new_percentage=int(input("New percentage:"))
        new_priority=int(input("New priority:"))
        projects[project_choice].completed_percentage,projects[project_choice].priority = new_percentage,new_priority

main()







