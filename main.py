 # Student_Info_Demo.py
# 此文件是对学生管理系统GUI界面的一个简单演示

from tkinter import *
from tkinter.ttk import *
from tkinter.messagebox import *
import pymysql
# import tkinter as tk
# from tkinter import ttk
# from tkinter.ttk import *
# from nltk.tag import str2tuple
# import os
# from PIL import Image, ImageTk


# 部署GUI界面

# 1.设置窗口对象
window = Tk()
window.geometry("920x680+200+100")
window.title('学生成绩管理系统')
window.resizable(0,0)
window["bg"]="White" # 白色

# 2.设置最上面的图片,这个不是很好弄，先是要弄一张合适的图片，要去修改分辨率
# 905*115比较好
top_image = PhotoImage(file="img.png")
top_label = Label(window,image=top_image)
top_label.place(x=3,y=3)



# 3.设置容器 / 分区
# 此处采用 panedWindow 和 LabelFrame 容器控件
window.left_pane = PanedWindow(width=201,height=670)  # 这里是规定容器的长宽
window.right_pane = PanedWindow(width=702,height=670)
window.left_pane.place(x=5,y=125) # 这里是决定将这个容器放在哪个位置
window.right_pane.place(x=211,y=125) # 这个坐标应该指的是左上角的点的位置
window.right_top_frame = LabelFrame(window.right_pane,text="在此添加学生信息",width = 650,height = 150)
window.right_top_frame.place(x = 14,y = 10) # 注意，这里的坐标是相对坐标，是相对于当前所属控件的坐标


# 4.设置若干按钮
# window.style_button = ttk.Style()
# window.style_button.configure('s_button',width=10,font=("Helvetica",17,"bold"))

window.button_show = Button(window,text=" 查询所有",width=10)
window.button_show.place(x = 40, y = 200)
window.button_best = Button(window,text="查询第一",width=10)
window.button_best.place(x = 40 , y = 250 )
window.button_delete = Button(window,text="删除末尾",width=10,state=DISABLED)
window.button_delete.place(x = 40 , y = 300)


# 5.在LabelFrame容器内设置若干控件
# 提前定义好相应变量，后面可以作为连接数据库的参数
sid = StringVar()
sname = StringVar()
cid = StringVar()
score = StringVar()

window.label_sid = Label(window.right_top_frame,text="学生编号")
window.label_sid.place(x = 5, y = 20)
window_input_sid = Entry(window.right_top_frame,width=16,textvariable=sid).place(x = 85, y = 18 )
# sid = window_input_sid.get()

window.label_sname = Label(window.right_top_frame,text="学生姓名")
window.label_sname.place(x = 350, y = 20 )
window_input_sname = Entry(window.right_top_frame,width=16,textvariable=sname).place(x = 447, y = 18)
# Entry(window,textvariable=sid)
# sname = window_input_sname.get()
#

window.label_cid = Label(window.right_top_frame,text="课程名称")
window.label_cid.place(x = 5, y = 60 )
window_input_cid = Entry(window.right_top_frame,width=16,textvariable=cid).place(x = 85 , y = 58)
# cid = window_input_cid.get()
#

window.label_score = Label(window.right_top_frame,text="成绩信息")
window.label_score.place(x = 350 , y = 60)
window_input_score = Entry(window.right_top_frame,width=16,textvariable=score).place(x = 447, y = 58 )
# score = window_input_score.get()

# window.button_append = Button(window.right_top_frame,width=10,text='ADD').place(x = 250, y = 95 )


# 6.添加 TreeView 控件
window.tree = Treeview(window.right_pane,show="headings",columns=("sid","sname","cid","score"),height=18)
window.tree.column("sid",width=100,anchor="center")
window.tree.column("sname",width=100,anchor="center")
window.tree.column("cid",width=80,anchor="center")
window.tree.column("score",width=80,anchor="center")

window.tree.heading("sid",text="学生编号")
window.tree.heading("sname",text="学生姓名")
window.tree.heading("cid",text="课程名称")
window.tree.heading("score",text="成绩信息")

window.tree.place(rely= 0.26, relwidth= 0.96 )
# .place(rely=0.3, relwidth=0.97)  .place(x=10,y=80)


# 至此，GUI界面设置完成

# 接下来需要对各个按钮进行逻辑实现

# 1.sql_query 是负责连接数据库并且执行一些简单操作的函数
def sql_query(sql):
    # query and return the result tuple

    conn = pymysql.connect(host='localhost', port=3306, user='root', password='et1879314', database='grade',
                           charset='utf8')
    cur = conn.cursor()

    cur.execute(sql)
    content = cur.fetchall()
    cur.close()
    conn.close()
    return content

# 2.tree_clear 这是用来清空TreeView控件里面的已存在的内容的函数
def tree_clear(*args):
    temp_list= window.tree.get_children()
    for i in temp_list:
            window.tree.delete(i)   # 先清空，再插入



# 3.load_tree 这是用来在TreeView控件中展示内容的函数
def load_tree(list):
    for item in list:
            window.tree.insert("",1,text="line",values=item)


# 4."查询" 按钮实现
def Show_All(*args):
    # 1.每一次展现 TreeView 内容之前，都要清空之前的内容
    tree_clear()

    # 2.获取查询结果，类型为元组
    sql = "SELECT Grade.StudentID,Grade.StudentName,Grade.CourseName,Grade.Grade " \
          "From Grade,Student Where Student.StudentID=Grade.StudentID;"
    query_result = sql_query(sql)

    # 加载数据到 TreeView 控件 ， 如果 load_treeview 方法不可用，则可以尝试 inset 方法
    #window.tree.load_treeview(query_result)

    # 3.加载数据 insert 方法
    load_tree(query_result)


# "查询"按钮
#window.button_show = Button(window,text=" 查询 ",width=10,command=Show_All)
#window.button_show.place(x = 40, y = 200)
window.button_show.bind("<Button-1>",Show_All)


# 5."第一"按钮实现
def Best_Stu(*args):
    tree_clear()

    sql = """Select StudentID,StudentName,CourseName,Grade
            from
            (
                Select StudentID,StudentName,CourseName,Grade
                ,row_number() over(PARTITION by Grade.CourseName order by Grade.Grade desc) as r
                from Grade
            ) as NEW2
            where r=1
        """

    query_result = sql_query(sql)
    load_tree(query_result)

# "第一"按钮
window.button_best.bind('<Button-1>',Best_Stu)

# 6.sql_insert_del 是用来增删数据库中的数据的函数
def sql_insert_del(sql,arg_list):
    conn = pymysql.connect(host='localhost', port=3306, user='root', password='et1879314', database='grade',
                           charset='utf8')
    cur = conn.cursor()

    try:
        cur.execute(sql,arg_list)
        conn.commit()
        Show_All()

    except:
        conn.rollback()

    cur.close()
    conn.close()

# "删除" 按钮实现
def Delete_One(*args):

    # 连接数据库
    conn = pymysql.connect(host='localhost', port=3306, user='root', password='et1879314', database='grade',charset='utf8')
    tree_clear()
    #sql="delete from Student where Student.StudentID='1909853T-J200-0090';"
    sql = """Set @ID=
    (Select ave1.ID
    from
    (
	    select AVER.Average,AVER.StudentName,AVER.StudentID as ID
	    FROM
	    (
		    SELECT AVG(Grade.Grade) AS Average,Student.StudentName,Student.StudentID,
		    row_number()over(order by avg(Grade.Grade) asc) as r
		    FROM Student
		    JOIN Grade
	    	ON Student.StudentName=Grade.StudentName
		    GROUP BY Student.StudentID
	    ) AS AVER
	    WHERE r=1;
    )as ave1)

    DELETE from Student where Student.StudentID=@ID;
    """

    query_result = sql_query(sql)
    Show_All()


window.button_delete.bind('<Button-1>',Delete_One)





# "添加" 按钮实现
def Add_Student(*args):

    # 要先判断用户是否把每个空都填了
    if sid.get() == "":
        showerror(title='ERROR', message="学生编号不能为空")
    elif sname.get() == "":
        showerror(title='ERROR', message="学生姓名不能为空")
    elif cid.get() == "":
        showerror(title='ERROR', message="课程名称不能为空")
    elif score.get() == "":
        showerror(title='ERROR', message="成绩信息不能为空")
    else:
        # 1.清空
        tree_clear()

        # 2.拿到源数据
        s_sid = sid.get()
        s_sname = sname.get()
        c_cid = cid.get()
        c_cname = cid.get()
        g_score = score.get()

        # 找出所有学生列表，课程列表
        sql = "select StudentID from Student;"
        sql_query_student = sql_query(sql)

        sql = "select distinct CourseName from Grade;"
        sql_query_course = sql_query(sql)

        tuple_s_sid = tuple((s_sid,))

        tuple_c_cid = tuple((c_cid,))

        # 判断用户的输入属于哪种情况，总共三种情况
        # 学生，课程都不同；学生课程都相同；学生或课程不同
        if tuple_s_sid in sql_query_student:
                if tuple_c_cid in sql_query_course: # 插入的学生信息和课程信息都是现有的，直接showinfo了
                    showerror(title="REPEAT",message="此信息已经存在")

                else: # 学生同，课程不同，grade新增
                    sql = "insert into grade values(%s,%s,%s,%s)"
                    arg_list = [s_sid,s_sname,c_cid,g_score]
                    sql_insert_del(sql,arg_list)
                    showinfo(title="SUCCESS", message="课程%s已经为学生%s添加!" % (c_cid,s_sname))

        else:
                if tuple_c_cid in sql_query_course: # 课程同，学生不同,student和grade新增
                    sql = "insert into student values(%s,%s);"
                    arg_list = [s_sid,s_sname]
                    sql_insert_del(sql,arg_list)

                    sql = "insert into grade values(%s,%s,%s,%s)"
                    arg_list = [s_sid,s_sname,c_cid,g_score]
                    sql_insert_del(sql,arg_list)

                    showinfo(title="SUCCESS", message="学生%s的课程%s信息已添加!" % (s_sname,c_cid))

                else: # 新同学，新课程，双表同增
                    sql_student = "insert into student values(%s,%s);"
                    arg_list = [s_sid, s_sname]
                    sql_insert_del(sql_student, arg_list)

                    sql_grade = "insert into grade values(%s,%s,%s,%s);"
                    arg_list = [s_sid, s_sname,c_cid, g_score]
                    sql_insert_del(sql_grade, arg_list)
                    showinfo(title="SUCCESS", message="学生%s和课程%s已添加!" % (s_sname ,c_cid))

# "添加"按钮
window.button_append = Button(window.right_top_frame,width=10,text='添加',command=Add_Student).place(x = 250, y = 95 )






# 启动UI界面
window.mainloop()