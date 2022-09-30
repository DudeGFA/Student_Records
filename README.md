## Scenario:

Jerome is a teacher at the Grand Rapids High School. Due to the lack of teachers willing to accept in-person teaching positions during the Covid era, Jerome has had to teach Math, Chemistry, Biology and Physics for the 8th grade students. 

The school term is made up of 96 class sessions and attendance is taken each day. Students earn 1 point for each class attendance. Jerome computes percentage class attendance and awards proportional score with a maximum possible score of 12 points for the class attendance contribution to total performance for the school term. 

There are class quizzes every week (19 in total for the term). Each quiz is graded over 10 maximum points. And a max aggregate score of 30 for the quiz contribution to total performance for the school term.

Homework is assigned every week (19 in total for the term). Each homework is graded over 10 maximum points. And a max aggregate score of 15 points for the homework contribution to total performance for the school term.

Exams account for the remaining points. The table below provides the names of the students and their identity codes

| Student name | ID       |
|--------------|----------|
| Bett James   |  GR-0483 |
| Namukolo Abrams| GR-0484 |
| Vera Abutu | GR-0485 |
| Kwame Doga | GR-0486 |
| Lukeman Ahmad | GR-0487 |
| Akin Torey | GR-0488 |
| Luke Brant | GR-0489 |
| James Kenyata | GR-0490 |
| Ngugi Tionga | GR-0491 |
| Okoro Eze | GR-0492 |
| Agatha Chiluba | GR-0493 |
| Mangu Joseph | GR-0494 |
| Longe Jethro | GR-0495 |
| Florence Giwa | GR-0496 |
| Vetiva Lucent | GR-0497 |
| Melody Braimoh | GR-0498 |
| Victor Ihab | GR-0499 |
| Mimi Trucker | GR-0500 |
| Maguel Peter | GR-0501 |
| Wellington Zuba | GR-0502 |

Jerome would like to have a python script that achieve the following.

**SCRIPT CAPABILITIES:**
1. enables him to manually load each students scores by subject for quiz, homework, attendance, and exam using the python input() function. Use as data, the records in the Student Scores table below (Table1.0) 
2. Automatically computes the Average Score, GPA (0 to 5.0), Grade and Status (Pass, Fail, Retake) and stores in a container for each student as per the provided rating scales below 
3. Holds each student’s performance records in a container 
4. Holds each subject performance records in a container for all students 
5. Holds ALL student performance records for ALL subjects in a container. Note: this container should hold all student scores for subjects quiz, homework and exam scores, Average Score, GPA, Grade and Status. All in a Container of containers 

Jerome would also like to have the functionality to query the containers above to fetch any specific performance records such as. 

**SCRIPT UTILITY:**
1. The full performance records of any student by simply providing the student’s name or ID 
2. Any student’s performance for any given subject by simply providing student name/ID and subject name 
3. Fetch the list of students in any of the grade categories (A, B, C, D, E, F) 
4. Fetch the list of students Statuses (Pass, Fail, Retake) 
5. Obtain a response from the script for any student to determine if they passed, failed, or need to retake the subject Implement you code and use the Students Records in the table below to populate your containers

<img src="https://github.com/DudeGFA/Student_Records/blob/main/README_Images/Student_Record_table.png"/>
<img src="https://github.com/DudeGFA/Student_Records/blob/main/README_Images/Grade_and_status_tables.png"/>
CONVERT your containers from item 5 under Script Capabilities above into a dataframe identical to the table below and save to an excel or csv file:
<img src="https://github.com/DudeGFA/Student_Records/blob/main/README_Images/Records_CSV_sample.png"/>
USAGE:

    clone this repo using "git clone https://github.com/DudeGFA/Student_Records.git"
    
    run the script "student_records.py" using "python ./student_records.py"

You are required to input a command, available options include:

### A. add

   Used to add a student's records to the container of records
 
        Input student's name    
        Input student's ID  
        Input student's scores in various subjects in this format: 'Quiz_score HW_score Attnd_score Exam_score'
   
### B. load     
   Used to print out students' records. Entails 5 sub commands:         \
    i. full - prints all records of specified students              
    ii. subject - prints a student's record for a particular subject   
    iii. grades - Outputs names of students with a specific grade   
    iv. statuses - Outputs name and status of all students  
    v. status - Ouputs status of a particular student   
    **Student's records can be load using either student's name or ID**
### C. read
   Command to read records from a csv file  
   
    Input filepath
    
### D. save
   Command to write records to a csv file       
   You could either write to a new file or append rows to an existing file.
   
    Input filepath
    
### E. exit
   Exits the script
