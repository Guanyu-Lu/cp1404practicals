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

def main():
    print("Welcome to Pythonic Project Management")
    projects=load_data()

def load_data():
    projects = []
    try:
        with open(FILENAME,"r") as in_file:
            in_file.readline()
            for line in in_file:
                parts = line.strip().split()
                if len(parts)==5:
                    date_string=parts[1]
                    date = datetime.datetime.strptime(date_string, "%d/%m/%Y").date()
                    projects.append(Project(parts[0],date,int(parts[2]),float(parts[3]),int(parts[4])))
    except FileNotFoundError:
        print(f"Sorry,{FILENAME} not found.")
    return projects









