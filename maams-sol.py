def makeStudent(info, *details):
    separator = "-"
    if separator in info:
        my_info_list = my_info.split("-")
        name = my_info_list[0]
        ID = int(my_info_list[1])
        dept = my_info_list[2]
    else:
        name = info[:15]
        ID = int(info[15:23])
        dept = info[23:]
    basic_information = (name, ID, dept)
    if len(details) == 2:
        courses = details[0]
        grades = details[1]
    elif len(details) == 1:
        courses = list(details[0].keys())
        grades = list(details[0].values())
    elif len(details) == 0:
        courses = []
        grades = []
    dict1 = {'basic_info': basic_information, 'courses':
             courses, 'grades': grades}
    return dict1
