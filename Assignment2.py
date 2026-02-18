# Program Name: Assignment2.py
# Course: IT3883/Section W01
# Student Name: Odam Tong
# Assignment Number: Lab#2
# Due Date: 02/18/ 2026
# Purpose: This program is to create a program in python that will read an input file with students and 
# their grades and calculate their average grade and display them in descending order. I used classroom materials
# python help from the web: https://www.geeksforgeeks.org/python/help-function-in-python/

def calculate_AVG(file_path):
    students = []   # Creating an empty list to store students and grades
    with open(file_path, 'r') as file:   # Opening the file as read mode

        for line in file: # Looping through each line in the file
            parts = line.split() # Splitting the line into parts
            name = parts[0] # The first part is for the student's name
            scores = [] # The rest of the parts are for the scores, convert them to floats
            for score in parts[1:]:
                scores.append(float(score))

            # I'm calculating the average score below by adding all scores and dividing the count
            if len(scores) > 0:
                average = sum(scores) / len(scores)
            else:
                average = 0  # If there are no scores, average is 0
            students.append((name, average)) # Adding the name and average to the students list

    # Sort the students list by average score in descending order
    students.sort(key=lambda x: x[1], reverse=True)

    # Print the names and averages of each students
    for student in students:
        print(f"{student[0]} {student[1]:.2f}")  # Print with two decimal places


#This is where run the program, but I have to identify the file name 
# and its path of where I placed the file in my Users directory.
calculate_AVG("Assignment2input.txt")
