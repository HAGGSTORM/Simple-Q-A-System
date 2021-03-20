import csv
choose = []
fill = []
judge = []

with open('test.csv','r',newline='',encoding='utf-8') as f1:
    file_reader = csv.reader(f1)
    for row in file_reader:
        if row[0] == '1':
            choose.append(row[1:])
        if row[0] == '2':
            fill.append(row[1:])
        if row[0] == '3':
            judge.append(row[1:])



def get_choose():
    return choose


def get_fill():
    return fill


def get_judge():
    return  judge