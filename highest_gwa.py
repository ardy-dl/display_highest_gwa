# Write a Python program that read a file containing the name of 20 students together with their GWA. 
# The program will outputs the name of the student who got the highest GWA (including the GWA).

# name a list
master_list = []
# open class_record.txt (read)
with open("class_record.txt") as ref_file:
    for line in ref_file:
        # seperate name and gwa by using list
        name, GWA = line.strip().split(",")
        master_list.append({"name": name, "GWA":float(GWA)})
    # find the highest gwa
    highest_GWA = min(master_list, key=lambda x: x["GWA"]) 
    # find all the students who got the highest grade
    best_students = [student for student in master_list if student["GWA"] == highest_GWA["GWA"]]

    # for designing
    from termcolor import colored
    from pyfiglet import Figlet

    # display name and gwa 
    if len(best_students) == 1:
        f = Figlet(font = "banner3-D")
        design_1 = colored(highest_GWA["name"], "is the highest with the GWA of", highest_GWA["GWA"], color= "green", attrs = ["italic"])
        print(design_1)
    else:
        f = Figlet(font = "banner3-D")
        design_2 = colored("Here are the students who got the highest GWA of " + str(highest_GWA["GWA"]), "yellow", attrs = ["bold"])
        print(design_2)
        for students in best_students:
            design_3 = colored(students["name"] + " - " + str(students["GWA"]), "blue", attrs = ["underline"])
            print(design_3)