##
## EPITECH PROJECT, 2022
## B-MUL-100-LYN-1-1-myradar-basile.fouquet
## File description:
## generator
##

import sys
import os
import random

def count_file_in_dir(dir_path):
    count = 0
    for path in os.listdir(dir_path):
        if os.path.isfile(os.path.join(dir_path, path)):
            count += 1
    return count

def create_file(path):
    path += "/" + str(count_file_in_dir(path)) + ".rdr"
    os.system("touch " + path)
    return path

def generate_script():
        path = create_file(sys.argv[2])
        file = open(path, 'w')
        buffer = ""
        plane = int(sys.argv[3])
        tower = int(sys.argv[4])
        for i in range(plane):
            line = "A " + str(random.randint(50, 1870)) + " " + str(random.randint(50, 1030))
            line += " " + str(random.randint(50, 1870)) + " " + str(random.randint(50, 1030))
            line += " " +str(random.randint(20, 150)) + " " + str(random.randint(0, 6)) + "\n"
            buffer += line
        for i in range(tower):
            line = "T " + str(random.randint(50, 1870)) + " " + str(random.randint(50, 1030))
            line += " " + str(random.randint(30, 200)) + "\n"
            buffer += line
        file.write(buffer[:-1])
        file.close()
        return path

def main():
        if sys.argv[1] == "-ce" or sys.argv[1] == "-ec":
            os.system("./my_radar " + generate_script())
            exit(0)
        if sys.argv[1] == "-c":
            sys.stdout.write(generate_script())
            exit(0)
        if sys.argv[1] == "-e":
            os.system("./my_radar " + sys.argv[2])
            exit(0)
        if sys.argv[1] == "-rm":
            if sys.argv[2] == "-all":
                os.system("rm -r " + sys.argv[3] + "/*.rdr")
            else:
                os.system("rm" + sys.argv[2])
            exit(0)
        sys.stdout.write("invalid argument use :\n -c to create\n -e to create and execute\n -rm to delete\n")
        exit(84)

main()

##  3ww