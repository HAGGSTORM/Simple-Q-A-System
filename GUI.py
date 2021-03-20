import tkinter as tk
import random
from get_csv import *
import csv
from tkinter.messagebox import showinfo

information = []

def Print_point():#计算总得分
    window4 = tk.Tk()
    window4.title("总分")
    window4.geometry("200x200")
    tk.Label(window4, text=f"你的得分是{int(information[2]+information[3]+information[4])}").pack()
    with open('point.csv', 'a', newline='', encoding='utf-8') as f1:
        file_writer = csv.writer(f1)
        file_writer.writerow(information)

def JQ(judge):
    def get_judge_point():
        judge_point = 0
        for i in range(question_num):
            if answer[i] == questions_seq[i].get():
                judge_point += per_point
        information.append(judge_point)
        print(information)
        window3.destroy()
        Print_point()

    questions_seq = []
    question_num = 2#判断题个数
    per_point = 10 / question_num#判断题分数
    window3 = tk.Tk()
    window3.title("判断题（填写对或错）")
    width = 200#根据题目个数改变窗口大侠小
    height = 50
    total_size = str(width)+'x'+ str(question_num * height+20)
    window3.geometry(total_size)
    questions = random.sample(range(len(judge)), question_num)
    answer = []
    for k in questions:
        answer.append(judge[k][-1])
    for i in range(len(questions)):
        tk.Label(window3, text=str(i + 1) + '.' + judge[questions[i]][0]).pack()
        questions_seq.append(tk.Entry(window3, show=None))
        questions_seq[i].pack()
    tk.Button(window3, text="确认提交填空题", width=20, command=get_judge_point).pack()

    window3.mainloop()


def FQ(fill):#填空题界面
    def get_fill_point():#计算填空题分数
        fill_point = 0
        for i in range(question_num):
            if answer[i] == questions_seq[i].get():
                fill_point += per_point
        information.append(fill_point)
        print(information)
        window2.destroy()
        JQ(get_judge())

    questions_seq = []
    question_num = 3#填空题个数
    per_point = 45 / question_num#填空题分数
    window2 = tk.Tk()
    window2.title("填空题")
    width = 200#根据题目个数改变窗口大侠小
    height = 50
    total_size = str(width)+'x'+ str(question_num * height+20)
    window2.geometry(total_size)
    questions = random.sample(range(len(fill)), question_num)
    answer = []
    for k in questions:
        answer.append(fill[k][-1])
    for i in range(len(questions)):
        tk.Label(window2, text=str(i + 1) + '.' + fill[questions[i]][0]).pack()
        questions_seq.append(tk.Entry(window2, show=None))
        questions_seq[i].pack()
    tk.Button(window2, text="确认提交填空题", width=20, command=get_fill_point).pack()
    #
    window2.mainloop()


def MCQ(choose):#选择题界面
    def get_choose_point():#计算分数函数
        choose_point = 0
        for i in range(question_num):
            if answer[i] == questions_seq[i].get():
                choose_point += per_point
        information.append(choose_point)
        print(information)
        window1.destroy()
        FQ(get_fill())

    trans = {'A':1,'B':2,'C':3,'D':4}
    questions_seq = []
    question_num = 2#选择题个数
    per_point = 45 / question_num#选择题分数
    window1 = tk.Tk()
    window1.title("选择题")
    width = 200
    height = 150
    total_size = str(width)+'x'+ str(question_num * height+20)#根据个数改变界面大小
    window1.geometry(total_size)
    questions = random.sample(range(len(choose)),question_num)
    answer = []
    for k in questions:
        answer.append(trans[choose[k][-1]])
    q1 = tk.IntVar()
    q2 = tk.IntVar()
    q3 = tk.IntVar()
    questions_seq.append(q1)
    questions_seq.append(q2)
    questions_seq.append(q3)
    for i in range(len(questions)):
        tk.Label(window1, text=str(i+1)+'.'+choose[questions[i]][0]).pack()
        for j in range(1,len(choose[i])-1):
            tk.Radiobutton(window1,text=choose[i][j],variable=questions_seq[i],value=j).pack()
    tk.Button(window1,text="确认提交选择题", width=20, command=get_choose_point).pack()#提交后自动计算分数


    window1.mainloop()


window = tk.Tk()#信息填写界面，填写名字与学号
window.title("请填写名字与学号")
window.geometry("340x140")
tk.Label(window,text="名字:").grid(row=0,column=0,padx=20,pady=10)
tk.Label(window,text="学号:").grid(row=1,column=0,padx=20,pady=10)

name = tk.Entry(window,show=None)
name.grid(row=0,column=1,padx=15,pady=10)
number = tk.Entry(window,show=None)
number.grid(row=1,column=1,padx=15,pady=10)


def get_infomation():
    if name.get() == '' or  number.get() == '':
        showinfo(title = '提示',message = '请输入姓名和学号')#未输入会提示用户输入
    else:
        information.append(name.get())
        information.append(number.get())#获取名字与学号
        window.destroy()
        MCQ(get_choose())



tk.Button(window,text="开始考试",width=10,command=get_infomation).grid(row=3,column=0,padx=25,pady=10)
#开始考试按钮，按下进入选额题
tk.Button(window,text="退出",width=10,command=window.quit).grid(row=3,column=1,padx=25,pady=10)
#退出考试按钮，按下退出


window.mainloop()
