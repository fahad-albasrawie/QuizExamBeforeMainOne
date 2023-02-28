import random
print('FILANTECH | PYTHON PROJECT | QUIZE EXAM PROGRAM')
print('Created by: HORMUUD UNIVERSITY STUDENT\n\t\tSpecifically_B-CS5&B-IT4STUDENTS\n\t\t\tVersion 1.2 22-07-2020')
Questions = ['The first letter of an identifier should be...\n 1) a keyword      2) letter    3) a number',
            'In C language, when the user enters a value or a variable, his/her input is held by...\n printf()		2) scanf()		3) getch();		4) none ',
            'Keywords can not be used as ...\n 1)	float 		2) int 		3) viriable		4) identfiers',
            'A relational opretors checks the relationship between two operands\n 1)	correct		2) incorrect ',
            'In programming language, the storage area or the container used to hold data is called ...\n 1)	increment 		2) variable		3) loops	4)relational operators',
            'In Ms excel, the sheet is said to be ...\n 1) database   2) slides    3)  document	4)  spreatsheeet',
            'Where the statements are written in ppt is called...\n 1) database   2) slides    3)  document	4)  spreatsheeet',
            'All formulas in Excel must begin with an equals sign (=).\n 1) right   2) wrong',
            '... feeds data and programs into computers\n 1) softwares      2) hardwares    3) inputs     4) input devices',
            'These sequence numbers are 10101101\n 1) Human language		2) Hachine language    3) Assembly language',
            'What is called this sign (==)in computer programming language? \n 1) assignment operator		2) increment sign   3) equal sign',
            'What logical operator does this function (. True only if the operand is 0\n 1) &&		2) ||   3) !',
            'What is called this symbol (!) in programming language?\n 1) amprecend		2) double quontation   3) nor  4) curly bracket',
            'The other name that is called the programmer is\n 1. 1) coder		2) hacker    3) network engineer	4)none',
            '... is a computer that serves up information to other computers on a network.\n 1) internet   2) network icon    3) server	4) none ',
            'Python is \n 1. Human laguage  2. Computer language',
            'for is one of\n 1. flow cotroll    2. logical operator ',
            'Fucntion is not an important in programming\n 1. may be    2. may not be',
            'Whenever working with excel, where the content is entered?\n 1) rows   2) columns   3) table		4) cells'
             ]
student_Marks = 0
average_Marks = 0
total_Corrected_Answer = 0
total_Questions = 0
non_Displayed_Questions = 0
dispalyed_Questions = []

for random_Questions in Questions:

    if total_Questions == 10:
        break
    else:
    
        i = random.randint(0, len(Questions)  -1)
        #print(i, end='. ')

        non_Displayed_Questions = Questions[i]

        if non_Displayed_Questions in dispalyed_Questions:
            continue
        else:
                        
            print(i, end='. ')
        
            print(non_Displayed_Questions)
            secret_Answer = 0
            user_Answer = 0
            if i == 0:
                secret_Answer = 2
                try:
                    user_Answer = int (input())
                except ValueError:
                    print('Follow the instruction: The answer could be 1. or 2.')
                if user_Answer == secret_Answer:
                    print('Correct!')
                    student_Marks += 2
                    total_Corrected_Answer +=1
                else:
                    print('Incorrect.')

            elif i == 1:
                secret_Answer = 2
                try:
                    user_Answer = int (input())
                except ValueError:
                    print('Follow the instruction: The answer could be 1. or 2.')
                if user_Answer == secret_Answer:
                    print('Correct!')
                    student_Marks += 2
                    total_Corrected_Answer +=1
                else:
                    print('Incorrect.')

            elif i == 2:
                secret_Answer = 3
                try:
                    user_Answer = int (input())
                except ValueError:
                    print('Follow the instruction: The answer could be 1. or 2.')
                if user_Answer == secret_Answer:
                    print('Correct!')
                    student_Marks += 2
                    total_Corrected_Answer +=1
                else:
                    print('Incorrect.')

            elif i == 3:
                secret_Answer = 2
                try:
                    user_Answer = int (input())
                except ValueError:
                    print('Follow the instruction: The answer could be 1. or 2.')
                if user_Answer == secret_Answer:
                    print('Correct!')
                    student_Marks += 2
                    total_Corrected_Answer +=1
                else:
                    print('Incorrect.')

            elif i == 4:
                secret_Answer = 2
                try:
                    user_Answer = int (input())
                except ValueError:
                    print('Follow the instruction: The answer could be 1. or 2.')
                if user_Answer == secret_Answer:
                    print('Correct!')
                    student_Marks += 2
                    total_Corrected_Answer +=1
                else:
                    print('Incorrect.')

            elif i == 5:
                secret_Answer = 4
                try:
                    user_Answer = int (input())
                except ValueError:
                    print('Follow the instruction: The answer could be 1. or 2.')
                if user_Answer == secret_Answer:
                    print('Correct!')
                    student_Marks += 2
                    total_Corrected_Answer +=1
                else:
                    print('Incorrect.')

            elif i == 6:
                secret_Answer = 2
                try:
                    user_Answer = int (input())
                except ValueError:
                    print('Follow the instruction: The answer could be 1. or 2.')
                if user_Answer == secret_Answer:
                    print('Correct!')
                    student_Marks += 2
                    total_Corrected_Answer +=1
                else:
                    print('Incorrect.')

            elif i == 7:
                secret_Answer = 1
                try:
                    user_Answer = int (input())
                except ValueError:
                    print('Follow the instruction: The answer could be 1. or 2.')
                if user_Answer == secret_Answer:
                    print('Correct!')
                    student_Marks += 2
                    total_Corrected_Answer +=1
                else:
                    print('Incorrect.')

            elif i == 8:
                secret_Answer = 4
                try:
                    user_Answer = int (input())
                except ValueError:
                    print('Follow the instruction: The answer could be 1. or 2.')
                if user_Answer == secret_Answer:
                    print('Correct!')
                    student_Marks += 2
                    total_Corrected_Answer +=1
                else:
                    print('Incorrect.')

            elif i == 9:
                secret_Answer = 2
                try:
                    user_Answer = int (input())
                except ValueError:
                    print('Follow the instruction: The answer could be 1. or 2.')
                if user_Answer == secret_Answer:
                    print('Correct!')
                    student_Marks += 2
                    total_Corrected_Answer +=1
                else:
                    print('Incorrect.')

            elif i == 10:
                secret_Answer = 3
                try:
                    user_Answer = int (input())
                except ValueError:
                    print('Follow the instruction: The answer could be 1. or 2.')
                if user_Answer == secret_Answer:
                    print('Correct!')
                    student_Marks += 2
                    total_Corrected_Answer +=1
                else:
                    print('Incorrect.')

            elif i == 11:
                secret_Answer = 3
                try:
                    user_Answer = int (input())
                except ValueError:
                    print('Follow the instruction: The answer could be 1. or 2.')
                if user_Answer == secret_Answer:
                    print('Correct!')
                    student_Marks += 2
                    total_Corrected_Answer +=1
                else:
                    print('Incorrect.')

            elif i == 12:
                secret_Answer = 3
                try:
                    user_Answer = int (input())
                except ValueError:
                    print('Follow the instruction: The answer could be 1. or 2.')
                if user_Answer == secret_Answer:
                    print('Correct!')
                    student_Marks += 2
                    total_Corrected_Answer +=1
                else:
                    print('Incorrect.')

            elif i == 13:
                secret_Answer = 1
                try:
                    user_Answer = int (input())
                except ValueError:
                    print('Follow the instruction: The answer could be 1. or 2.')
                if user_Answer == secret_Answer:
                    print('Correct!')
                    student_Marks += 2
                    total_Corrected_Answer +=1
                else:
                    print('Incorrect.')

            elif i == 14:
                secret_Answer = 3
                try:
                    user_Answer = int (input())
                except ValueError:
                    print('Follow the instruction: The answer could be 1. or 2.')
                if user_Answer == secret_Answer:
                    print('Correct!')
                    student_Marks += 2
                    total_Corrected_Answer +=1
                else:
                    print('Incorrect.')

            elif i == 15:
                secret_Answer = 2
                try:
                    user_Answer = int (input())
                except ValueError:
                    print('Follow the instruction: The answer could be 1. or 2.')
                if user_Answer == secret_Answer:
                    print('Correct!')
                    student_Marks += 2
                    total_Corrected_Answer +=1
                else:
                    print('Incorrect.')

            elif i == 16:
                secret_Answer = 1
                try:
                    user_Answer = int (input())
                except ValueError:
                    print('Follow the instruction: The answer could be 1. or 2.')
                if user_Answer == secret_Answer:
                    print('Correct!')
                    student_Marks += 2
                    total_Corrected_Answer +=1
                else:
                    print('Incorrect.')

            elif i == 17:
                secret_Answer = 2
                
                try:
                    user_Answer = int (input())
                except ValueError:
                    print('Follow the instruction: The answer could be 1. or 2.')
                if user_Answer == secret_Answer:
                    print('Correct!')
                    student_Marks += 2
                    total_Corrected_Answer +=1
                else:
                    print('Incorrect.')

            elif i == 18:
                secret_Answer = 4
                try:
                    user_Answer = int (input())
                except ValueError:
                    print('Follow the instruction: The answer could be 1. or 2.')
                if user_Answer == secret_Answer:
                    print('Correct!')
                    student_Marks += 2
                    total_Corrected_Answer +=1
                else:
                    print('Incorrect.')
            



            
            total_Questions += 1

            dispalyed_Questions.append(non_Displayed_Questions)
            
average_Marks = float (total_Corrected_Answer / 10 * 100)

print('\n\n\n\n************Test Finished***********')
print('.............................................')
print('Results\n........')
print('Marks: ' + str (student_Marks))
print('Average: ' + str (average_Marks))
if average_Marks >=70:
    print('Passed')
else:
    print('Failed')
    
