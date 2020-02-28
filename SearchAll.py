import os
from tkinter import *
from tkinter import filedialog
import tkinter

list_filepath = []#全局变量，文件夹及子文件夹中含有的文件（不含子文件夹）
result_list = []#全局变量，文件夹及子文件夹中含有关键字的文件

def get_filedialog():
    #获取到用户选择的文件夹中及选择的子文件夹中含有的文件（不含子文件夹）
    global list_filepath #全局变量
   
    selectfile_Text.delete(1.0,END)#清除选择文件夹的交互框中的内容
    target_dir = filedialog.askdirectory()#记录用户选择的内容
    selectfile_Text.insert(1.0,target_dir)#把用户选择的内容填到选择文件夹的交互框中

    dir_file = os.walk(target_dir)#获取到用户选择的文件夹中及选择的子文件夹中含有的文件

    list_filepath = [] #清空全局变量

    for x in dir_file:
        #将结果添加到全局变量
        for y in  x[2]:
            filepath = x[0] + "/" + y#文件的路径                               
            list_filepath.append(filepath)#添加到全局变量中

    text_text = "" #清空界面中的左侧结果
    for x in list_filepath:
        #将结果添加到左侧结果里
        text_text = text_text + x + "\n"

    
    targetdir_Text.delete(1.0,END)#清空界面中的左侧结果
    targetdir_Text.insert(1.0,text_text)#获取到用户选择的文件夹中及选择的子文件夹中含有的文件的结果在界面中的左侧中显示

def get_keyword():
    #获取用户输入的关键词句并输入含关键词句的文件路径
    global list_filepath,result_list#全局变量
    
    keyword = keyword_Text.get(1.0,END)#获取在界面中输入的关键词句

    finddir_Text.delete(1.0,END)#清空界面中的右侧结果

    result_list = []#输入含关键词句的文件路径

    for x in list_filepath:
        try:
            #如果能顺利打开说明不是乱码
            f = open(x).read()#从用户选择中的文件选取一个打开
            result = f.find (keyword)#从上述文件中查找关键词
            if result >= 0:
                #找到了
                finddir_Text.insert(1.0,x + "\n")#将这个文件的路径添加的右侧结果界面
                result_list.append(x)#在结果列表里添加这个文件
            else:
                #没找到就算了
                None
        except:
            #乱码，就算了吧
            None

def open_result_list():
    #使用CMD打开含关键词句的文件
    global result_list#含关键词句的文件路径的结果列表，全局变量

    for x in result_list:
        #使用CMD打开这个文件
        os.system(x)

#窗口基础属性
root = Tk()
root.minsize(600,400)#窗口最小大小
root.title("全文档搜索")#窗口名称

#提示    
Label(root,text = "▼该文件夹的文件").place(relx = 0.01,relwidth = 0.48,rely= 0.21,relheight = 0.04)
Label(root,text = "▼这些文件含有关键字").place(relx = 0.51,relwidth = 0.48,rely= 0.21,relheight = 0.04)

#按键
selectfile_botton = Button(root,command = get_filedialog, text = "选择文件夹")
selectfile_botton.place(relx = 0.01,relwidth = 0.14,rely= 0.02,relheight = 0.08)

selectfile_botton = Button(root,command = get_keyword, text = "关键词句")
selectfile_botton.place(relx = 0.01,relwidth = 0.14,rely= 0.12,relheight = 0.08)

selectfile_botton = Button(root,command = open_result_list, text = "打开含有关键字的文件")
selectfile_botton.place(relx = 0.75,relwidth = 0.24,rely= 0.91,relheight = 0.08)

#文本框
selectfile_Text = Text(root)#显示用户选择的文件的地方
selectfile_Text.place(relx = 0.15,relwidth = 0.84,rely= 0.02,relheight = 0.08)

keyword_Text = Text(root)#用户输入关键词的地方
keyword_Text.place(relx = 0.15,relwidth = 0.84,rely= 0.12,relheight = 0.08)

targetdir_Text = Text(root)#用户选择的文件夹中及选择的子文件夹中含有的文件
targetdir_Text.place(relx = 0.01,relwidth = 0.48,rely= 0.26,relheight = 0.64)

finddir_Text = Text(root)#含关键词句的文件路径
finddir_Text.place(relx = 0.51,relwidth = 0.48,rely= 0.26,relheight = 0.64)

root.mainloop()#无LOOP无界面
        
