################ Function Definitions ################

# Shows the user what options they have
def displayMenu():

  # This option will involve you adding a student and a collection for their grades to a dictionary!
  print("1. Add a Student")
 
  
  # This option will involve you removing a pair from a dictionary!
  print("2. Remove a Student")

  # This option will require you to grab a student from a dictionary and add a quiz grade to it's corresponding collection of grades!
  # You'll also need to use a pre-written function that ensures the user is entering a valid grade (a decimal number)
  print("3. Add Quiz Grade for Student")

  # This option will require you to use a loop to list all of the grades for an INDIVIDUAL student!
  print("4. List a Student's Quiz Grades")

  # This option will have you write a function that takes in a student's grade as a number and return the letter grade equivalent!
  print("5. Get Student's Letter Grade")

  print("6. Quit")

# Prompts the user to enter a numeric grade
# This function works, and ensures the user entered a valid float for the grade
# It's not important HOW this function works, but how to USE this function
def getNumberGradeFromUser():

  val = None

  while(val == None):
    try:
      test = float(input("Enter a Grade: "))
      val = test
    except:
      val = None

  return val

#Return the letter grade for this student
def getLetterGrade(grade):
  if(grade >= 90):
    return "A"
  elif(grade >= 80):
    return "B"
  elif(grade >= 70):
    return "C"
  elif(grade >= 60):
    return "D"
  else:
    return "F"

################ Main Program ################

studentName = {}
key = ""
grade = ""  
option = (0)
# Application Loop
while option != "6":
  displayMenu()
  print()
  option = input("Enter a choice: ")
  
    # Option 1: Add a student
  if option == "1":
    name = input("Enter a Student's Name: ")
    studentName[name] = []
    print()
    print(f"{name} has been added!")
    print()
    
  # Option 2: Remove a student
  elif option == "2":
    name = input("Enter a Student's Name: ")
    if name in studentName:
      studentName.pop(name)
      print()
      print(f"{name} Removed!")
      print()
      
  # Option 3: Add a quiz grade for a student
  elif option == "3":
    print()
    name = input("Enter a Student's Name: ")
    grade = getNumberGradeFromUser() 
    print()
    studentName[name].append(grade)
    print()
    print(f"{name}'s grade has been added!")
    print()
      
  # Option 4: List a student's quiz grades
  elif option =="4":
    print()
    name = input("Enter a Student's Name: ")
    if name in studentName:
      print(f"{name}'s Grades: ") #print dictionary key and value#
      print()
    else:
      studentName[name] = []
      print()
 
  # Option 5: Get a student's letter grade
  elif option =="5":
    print()
    name = input("Enter a Student's Name: ")
    if name in studentName:
      print(f"{studentName} has a grade of: {getLetterGrade}")
      #modules objects 
# mean() method is used to calculate the mean of the list

  
  # Prompt the user to select an option
