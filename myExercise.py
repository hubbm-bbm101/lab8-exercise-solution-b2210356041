import sys


class NameNotFoundException(Exception):
    pass


student_info = {}  # Student Name: (University,Department)


def load_students(path):
    try:
        with open(path, 'r') as studentsFile:
            for line in studentsFile.readlines():
                line_fragments = line.strip('\n').split(':')
                info_fragments = line_fragments[1].split(',')
                student_info.update({line_fragments[0]: tuple(info_fragments)})
    except IOError:
        print("Error! Could not read \'" + path + "\'!")


def start():
    if len(sys.argv) != 3:
        print("Error! Not enough arguments entered.")
        return

    load_students(sys.argv[1])

    names = sys.argv[2].split(',')
    for name in names:
        try:
            if name not in student_info.keys():
                raise NameNotFoundException()
            print("Name: " + name + ", University: " + student_info[name][0] + "," + student_info[name][1])
        except NameNotFoundException:
            print("No record of \'" + name + "\' was found!")


start()
