def input_name():
    while True:
        name = input("Enter student name: ")
        if name.isalpha():
            return name
        else:
            print("Invalid name, please enter letters only.")

def input_student_id():
    while True:
        student_id = input("Enter student ID: ")
        if student_id.isdigit() and len(student_id) == 9:
            return student_id
        else:
            print("Invalid ID, must be equal to 9 digits.")

def input_mark_subject(subject_name):
    while True:
        mark = input("Enter" + subject_name +"marks: ")
        if mark.isdigit():
            mark = float(mark)
            if 0 <= mark <= 100:
                return mark
            else:
                print("Invalid mark, must be between 0-100.")
        else:
            print("Invalid mark, please enter digits only.")

total_students = 0
count_a = 0
count_b = 0
count_c = 0 
count_f = 0
total_marks = 0

while True:
    print("*********** Enter information ***********")
    name = input_name()
    student_id = input_student_id()
    
    test_mark = input_mark_subject("test")
    project_mark = input_mark_subject("project")
    workshop_mark = input_mark_subject("workshop")
    exam_mark = input_mark_subject("exam")
    
    ca_marks = (test_mark * 0.4) + (project_mark * 0.3) + (workshop_mark * 0.3)
    module_marks = (ca_marks * 0.5) + (exam_mark * 0.5)
    
    if ca_marks < 40 or exam_mark < 40:
        module_grade = "F"
        remarks = "Restudy"
        comments = "Don't get discouraged, keep trying!"
    elif module_marks >= 75:
        module_grade = "A"
        remarks = "Pass with A grade"
        comments = "Well done!"
    elif module_marks >= 65:
        module_grade = "B"
        remarks = "Pass with B grade"
        comments = "Almost can get an A grade, work harder!"
    else:
        module_grade = "C"
        remarks = "Pass with C grade"
        comments = "Please be careful, you only qualified for a C."
    
    print("*********** Result ***********")
    print(f"Student name: {name}")
    print(f"Student ID: {student_id}")
    print(f"Test Marks: {test_mark}, Project Marks: {project_mark}, Workshop Marks: {workshop_mark}, Exam Marks: {exam_mark}")
    print(f"Module Marks: {module_marks}, Module Grade: {module_grade}, Remarks: {remarks}")
    print(comments)
    print("*********** Result ***********")

    total_students += 1
    total_marks += module_marks
    
    if module_grade == "A":
        count_a += 1
    elif module_grade == "B":
        count_b += 1
    elif module_grade == "C":
        count_c += 1
    else:
        count_f += 1
        
    choice = input("Do you want to enter another student record? [Y/y] for Yes, [N/n] for No: ")
    if choice == 'n'or choice == 'N' :
        break

if total_students > 0:
    average_marks = total_marks / total_students
    print(f"There is/are {total_students} students' record(s) inputted, and the average marks is: {average_marks}")
    print(f"Total number of A grade: {count_a}")
    print(f"Total number of B grade: {count_b}")
    print(f"Total number of C grade: {count_c}") 
    print(f"Total number of F grade: {count_f}")
else:
    print("No student records were entered.")
 




def quick_grade_check():
    print("\n" + "🎊" * 15 + "✨" * 5)
    print("🎯🔍📊 Quick Grade Check 📈🔍🎯")
    print("✨" * 5 + "🎊" * 15)
    
    score_input = input("🎯🎯 Enter module score (0-100): ")
    
    if score_input.isdigit():
        score = int(score_input)
        
        if score < 0 or score > 100:
            print("❌🚫 Score must be between 0-100! 🚫❌")
            return
            
        if score >= 75:
            grade = "A"
            comment = "🎉🎊🏆 Well done! Excellent work! 🏆🎊🎉"
        elif score >= 65:
            grade = "B"
            comment = "👍⭐😊 Almost can get an A grade, work harder! 😊⭐👍"
        elif score >= 40:
            grade = "C" 
            comment = "⚠️🤔📝 Please be careful, you only qualified for a C. 📝🤔⚠️"
        else:
            grade = "F"
            comment = "💪🔥🚀 Don't get discouraged, keep trying! 🚀🔥💪"
            
        print(f"📊✅🎉 Result: {score} points → Grade {grade} 🎉✅📊")
        print(f"💡🌟 {comment} 🌟💡")
            
    else:
        print("❌🤦‍♂️ Please enter a valid number! 🤦♀️❌")

print("\n🎮🕹️ Do you want to use the quick grade check? 🕹️🎮")
choice = input("🎯👉 Enter Y to use, any other key to exit: 👈🎯")

if choice == 'Y' or choice == 'y':
    quick_grade_check()

print("\n🙏❤️ Thank you for using the Student Management System! ❤️🙏")
print("👋😊⭐ Have a great day! ⭐😊👋")
print("🌈🎉🎊 Come back anytime! 🎊🎉🌈")