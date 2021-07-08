student_1 = {'Maths' : 40, 'Science' : 90, 'Ethics' : 60, 'Name' : 'Chandler'}
student_2 = {'Maths' : 70, 'Science' : 70, 'Ethics' : 30, 'Name' : 'Joey'}
student_3 = {'Maths' : 60, 'Science' : 80, 'Ethics' : 80, 'Name' : 'Ross'}

student_list = [student_1, student_2, student_3]

def Mathematics(student_list):
    highest_score_maths = 0
    student_name = ''
    for every_student in student_list:
        if(every_student.get('Maths') > highest_score_maths):
            highest_score_maths = every_student.get('Maths')
            student_name = every_student.get('Name')

    print(f'Highest score in Mathematics is {highest_score_maths} by {student_name}.')

def Science(student_list):
    highest_score_science = 0
    student_name = ''
    for every_student in student_list:
        if(every_student.get('Science') > highest_score_science):
            highest_score_science = every_student.get('Science')
            student_name = every_student.get('Name')

    print(f'Highest score in Science is {highest_score_science} by {student_name}.')

def Ethics(student_list):
    highest_score_ethics = 0
    student_name = ''
    for every_student in student_list:
        if(every_student.get('Ethics') > highest_score_ethics):
            highest_score_ethics = every_student.get('Ethics')
            student_name = every_student.get('Name')

    print(f'Highest score in Ethics is {highest_score_ethics} by {student_name}.')

Mathematics(student_list)
Science(student_list)
Ethics(student_list)




