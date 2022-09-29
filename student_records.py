from statistics import mean
import csv
import pandas as pd

stu_records = {'Bett James': {'CHEM': [127, 135, 17, 46], 'BIO': [184, 186, 58, 97], 'PHY': [52, 142, 29, 73], 'MATH': [133, 97, 34, 45],
 'CHEM Avg': 52.62, 'BIO Avg': 92.70, 'PHY Avg': 54.44, 'MATH Avg': 52.26, 'Avg Score': 63.00, 'GPA': 3.2, 'Grade': 'D', 'Status': 'Pass'},
 'Namukolo Abrams': {'CHEM': [141, 82, 95, 52], 'BIO': [177, 170, 37, 41], 'PHY': [21, 12, 43, 41], 'MATH': [136, 180, 48, 31],
 'CHEM Avg': 62.97, 'BIO Avg': 66.12, 'PHY Avg': 22.97, 'MATH Avg': 55.01, 'Avg Score': 51.77, 'GPA': 2.6, 'Grade': 'E', 'Status': 'Retake'},
 'Vera Abutu': {'CHEM': [51, 102, 96, 24], 'BIO': [112, 55, 71, 51], 'PHY': [61, 105, 83, 98], 'MATH': [74, 50, 93, 94],
 'CHEM Avg': 38.43, 'BIO Avg': 52.83, 'PHY Avg': 70.44, 'MATH Avg': 67.68, 'Avg Score': 57.34, 'GPA': 2.9, 'Grade': 'D', 'Status': 'Pass'}}
id_name = {'GR-0483': 'Bett James', 'GR-0484': 'Namukolo Abrams', 'GR-0485': 'Vera Abutu'}
headers = ["Name", "ID", "Chem Quiz", "Bio Quiz", "Phy Quiz", "Math Quiz", "Chem HW", "Bio HW", "Phy HW", "Math HW", "Chem Attnd", "Bio Attnd", "Phy Attnd", "Math Attnd"
        , "Chem Exam", "Bio Exam", "Phy Exam", "Math Exam", "Chem AVG", "Bio AVG", "Phy AVG", "Math AVG", 'Avg Score', 'GPA', 'Grade', 'Status']

def try_parse_int(strn):
    '''helper to parse int from string without erroring on empty or misformed string'''
    list_str = strn.strip().split()
    list_int = []
    for i in range(4):
        try:
            list_int.append(int(list_str[i]))
        except Exception:
            list_int.append(0)
    return list_int

def Avg_score(scores):
    """Computes average score to 2 dp"""
    avg_scr = ((scores[0] / 190) * 30) + ((scores[1] / 190) * 15) + ((scores[2] / 96) * 12) + ((scores[3] / 100) * 43)
    return round(avg_scr, 2)

def grade_classifier(avg_scr):
    """returns a students grade"""
    if avg_scr >= 90:
        return 'A'
    elif avg_scr >= 75:
        return 'B'
    elif avg_scr >= 65:
        return 'C'
    elif avg_scr >= 55:
        return 'D'
    elif avg_scr >= 50:
        return 'E'
    else:
        return 'F'

def status_classifier(avg_scr):
    """returns a student's status"""
    if avg_scr >= 55:
        return 'Pass'
    elif avg_scr >= 50:
        return 'Retake'
    else:
        return 'Fail'

def DF(value=None):
    """returs pandas dataframe representaion of stu_records"""
    new_list=[]
    if value != None:
        name_list = value.split(",")
        for name in name_list:
            if name.strip() in id_name.keys():
                name = id_name[name.strip()]
            if name.strip().title() in stu_records.keys():
                new_list.append(row_list(name.strip().title()))
            else:
                print(name + " doesn't exist in the registry")
        DF_stu_record = pd.DataFrame(new_list, columns=headers)
        return DF_stu_record.set_index('ID')
    global DF_stu_records
    for name in stu_records.keys():
        new_list.append(row_list(name))
    DF_stu_records = pd.DataFrame(new_list, columns=headers)
    return DF_stu_records.set_index('ID')

def add():
    """adds a student's record to std_records"""
    name = input("input student's name\n")
    id = input("input student's id\n")
    CHEM_SCORES = input("input student's CHEM scores in this format 'Quiz Homework Attendance Exam'\n")
    BIO_SCORES = input("input student's BIO scores in this format 'Quiz Homework Attendance Exam'\n")
    PHY_SCORES = input("input student's PHY scores in this format 'Quiz Homework Attendance Exam'\n")
    MATH_SCORES = input("input student's MATH scores in this format 'Quiz Homework Attendance Exam'\n")
    name = name.strip().title()
    stu_records[name] = {'CHEM': try_parse_int(CHEM_SCORES), 'BIO': try_parse_int(BIO_SCORES), 'PHY': try_parse_int(PHY_SCORES), 'MATH': try_parse_int(MATH_SCORES)}
    id_name[id] = name
    stu_records[name]['CHEM Avg'] = Avg_score(stu_records[name]['CHEM'])
    stu_records[name]['BIO Avg'] = Avg_score(stu_records[name]['BIO'])
    stu_records[name]['PHY Avg'] = Avg_score(stu_records[name]['PHY'])
    stu_records[name]['MATH Avg'] = Avg_score(stu_records[name]['MATH'])
    stu_records[name]['Avg Score'] = round(mean([stu_records[name]['CHEM Avg'], stu_records[name]['BIO Avg'], stu_records[name]['PHY Avg'], stu_records[name]['MATH Avg']]), 2)
    stu_records[name]['GPA'] = round((stu_records[name]['Avg Score'] / 100) * 5, 1)
    stu_records[name]['Grade'] = grade_classifier(stu_records[name]['Avg Score'])
    stu_records[name]['Status'] = status_classifier(stu_records[name]['Avg Score'])
    print(name + "'s records have been added")
def add_csv(csv_list):
    """adds records from csv file to Dict stu_records"""
    j = len(csv_list) - 1
    while j >= 0:
        if len(csv_list[j]) < len(headers):
            del csv_list[j]
        j -= 1
    try:
        for i in range(1, len(csv_list)):
            stu_records[csv_list[i][0].strip().title()] = {'CHEM': [int(csv_list[i][2].strip()), int(csv_list[i][6].strip()), int(csv_list[i][10].strip()), int(csv_list[i][14].strip())], 'BIO': [int(csv_list[i][3].strip()), int(csv_list[i][7].strip()), int(csv_list[i][11].strip()), int(csv_list[i][15].strip())],
            'PHY': [int(csv_list[i][4].strip()), int(csv_list[i][8].strip()), int(csv_list[i][12].strip()), int(csv_list[i][16].strip())], 'MATH': [int(csv_list[i][5].strip()), int(csv_list[i][9].strip()), int(csv_list[i][13].strip()), int(csv_list[i][17].strip())], 'CHEM Avg': float(csv_list[i][18].strip()),
            'BIO Avg': float(csv_list[i][19].strip()), 'PHY Avg': float(csv_list[i][20].strip()), 'MATH Avg': float(csv_list[i][21].strip()), 'Avg Score': float(csv_list[i][22].strip()), 'GPA': float(csv_list[i][23].strip()), 'Grade': csv_list[i][24].strip(), 'Status': csv_list[i][25].strip()}
            id_name[csv_list[i][1].strip()] = csv_list[i][0].strip()
        print(csv_list)
        print("The contents of the file have been added and can be accessed")
    except Exception:
        print("Unsupported file format, error reading row - " + str(i))

def load():
    """loads student's records"""
    print("What data would you like to load?")
    print("input 'full' to load the full performance record of any student")
    print("Input 'subject' to load any student's performance for any give subject")
    print("Input 'grades'  to fetch the list of students in any of the grade categories (A,B,C,D,E,F)")
    print("Input 'statuses' to fetch the list of students Statuses(Pass, Fail, Retake)")
    print("Input 'status' to determine if a specific student passed, failed or need to retake the subject")
    action = input()
    if action == 'full':
        key = input("enter students' names or ids as comma separated values\nEnter 'all' to print all students' records\n" ).strip()
        if key.lower() == 'all':
            print(DF())
            return
        if key in id_name.keys():
            key = id_name[key]
        try:
            print(DF(key))
        except KeyError:
            print("invalid key/name")
    elif action == 'subject':
        name = input("enter student's name or id\n").strip()
        if name in id_name.keys():
            name = id_name[name]
        subject = input("input subject either 'CHEM'/'PHY'/'BIO'/'MATH'\n")
        try:
            print("Quiz: " + str(stu_records[name][subject.strip().upper()][0]))
            print("Homework: " + str(stu_records[name][subject.strip().upper()][1]))
            print("Attendance: " + str(stu_records[name][subject.strip().upper()][2]))
            print("Exam: " + str(stu_records[name][subject.strip().upper()][3]))
        except KeyError:
            print("Invalid name/subject\n")
    elif action == 'grades':
        grade = input("enter grade category\n")
        if grade.upper().strip() not in ['A', 'B', 'C', 'D', 'E', 'F']:
            print("invalid grade")
            return
        print("List of students with grade " + grade + ":")
        [print(name) for name in stu_records.keys() if stu_records[name]['Grade'] == grade.upper().strip()]
    elif action == 'statuses':
        [print(name + "-" + stu_records[name]['Grade']) for name in stu_records.keys()]
    elif action == 'status':
        name = input("input student's name/id\n")
        if name in id_name.keys():
            name = id_name[name]
        try:
            print(stu_records[name.strip()]['Status'])
        except KeyError:
            print("invalid name")
    else:
        print("invalid input")

def row_list(name):
    """returns a student's full records as a list"""
    row=[name, list(id_name.keys())[list(id_name.values()).index(name)]]
    for i in range(4):
        row.append(stu_records[name]['CHEM'][i])
        row.append(stu_records[name]['BIO'][i])
        row.append(stu_records[name]['PHY'][i])
        row.append(stu_records[name]['MATH'][i])
    row.append(stu_records[name]['CHEM Avg'])
    row.append(stu_records[name]['BIO Avg'])
    row.append(stu_records[name]['PHY Avg'])
    row.append(stu_records[name]['MATH Avg'])
    row.append(stu_records[name]['Avg Score'])
    row.append(stu_records[name]['GPA'])
    row.append(stu_records[name]['Grade'])
    row.append(stu_records[name]['Status'])
    return row

def entry():
    """entry function
        options:
            'add' To add student's record manually
            'load' to output student records
            'exit' to exit script
            'save' to write records to csv file
            'read' to read student records from csv file
    """
    action = input("input 'add' To add student record\ninput 'load' to output student records\ninput 'exit' to exit script\ninput 'save' to write to file\ninput 'read' to read student records from file\n")
    if action.lower().strip() == 'add':
        add()
    elif action.lower().strip() == 'load':
        load()
    elif action.lower().strip() == 'save':
        csv_file = input("input file name\n")
        print("Do you want to write to a new file or append records to an existing file")
        action = input("input 'a' to append or 'w' to write\n")
        try:
            with open(csv_file, action) as csvfile:
                writer = csv.writer(csvfile)
                if action == 'w':
                    writer.writerow(headers)
                for name in stu_records.keys():
                    writer.writerow(row_list(name))
        except FileNotFoundError:
            print("File not found")

    elif action.lower().strip() == 'read':
        file_path = input("input file path\n")
        try:
            with open(file_path, 'r') as file:
                csv_list = csv.reader(file)
                add_csv(list(csv_list))
        except FileNotFoundError:
            print("File not found")
    elif action.lower().strip() == 'exit':
        print("Goodbye!")
        return
    else:
        print('command not recognized')
    entry()

print("Welcome!, Would you like to save or load student's records?")
entry()