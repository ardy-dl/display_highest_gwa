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
    print(highest_GWA)
    # display name and gwa
