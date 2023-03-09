##############################
# Блок підключення бібліотек #
##############################
# -*- coding: utf-8 -*-
import sys

###########################
# Блок реалізації функцій #
###########################
def print_file(file_name):
    file = open(file_name, 'r')
    for i in file:
        print(i)
    file.close()

def create(test_file_path = "example.txt"):
    file = open(test_file_path, "r")
    file_output = open(sys.argv[0], "w")
    for line in file:
        file_output.write(line)
    file.close()
