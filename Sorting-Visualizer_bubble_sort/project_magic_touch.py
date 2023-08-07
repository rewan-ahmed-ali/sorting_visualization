import tkinter as tk
import datetime
import random
#Making a window using the Tkinter
win = tk.Tk()
win.title('Magic Touch Team')
win.geometry('600x450') #حجم شاشه العرض اثبته برقم اللي محتجاه  # عرض 600 
win.config(background="pink")
#Making a Canvas within the window to display contents 
# # canvas -->  win شاشه جديده  داخل شاشه  الاصليه
canvas = tk.Canvas(win, width='300', height='400')
#,background='white' ممكن تتحط بدل من ( line 15)
canvas.grid(row=0,column=0, rowspan = 40, columnspan=8)
#حط العناصر وكأنها نظام جدولي grid
canvas.config(background="#FDE4E3")
#Function to swap two bars that will be animated
# Team Members Names
def names():
    frame = tk.Frame(win, background="pink",bg="pink",border=1)
    frame.grid(row=2,column=10)
    label = tk.Label(frame, text="Team Members",background="pink",font="arial" )
    txt = tk.Text(frame, height= 12  , width= 30 ,background="pink" )
    name = "\n Omnya Mohamed Negm \n Rewan Ahmed Abdelghfar \n Maryam Jamal Dawood \n Sara Abd El-Kader Mohamed \n Alaa Atef \n Aya Sabry El Sorady \n Yasmeena Ehab \n Ahmed Samy \n Ramez mousa"
    label.pack()
    txt.pack()
    txt.insert(tk.END,name)
names()
#complexity code
def complexity():
    label_1 = tk.Label(win, text="  Time Complexity=> O(n²)",background="pink",font="arial" )
    label_1.grid(column=10,row=10)
complexity()
#swap 
def swap(pos_0, pos_1):
    bar1, _, bar12, _ = canvas.coords(pos_0)
    bar21, _, bar22, _ = canvas.coords(pos_1)
    canvas.move(pos_0, bar21-bar1, 0)
    canvas.move(pos_1, bar12-bar22, 0)
#main function
def build():
    global barList
    global List
    canvas.delete('all')
    barstart = 6
    barend = 10 #شكل عمود
    barList = []
    List = []
    #Creating a rectangle
    for bar in range(0,30): #عدد bar
        randomY = random.randint(1, 380) # y تغيير  حجم عمود بالنسبة ل محور
        bar = canvas.create_rectangle(barstart, randomY, barend,380 , fill='red') #1 شكل معكوس لو رقم ب
        barList.append(bar)
        barstart += 10
        barend += 10
    #Getting length of the bar and appending into length list
    for bar in barList:
        bar = canvas.coords(bar)
        length = bar[3] - bar[1]
        List.append(length)
    #Maximum is colored  orange
    #Minimum is colored  gray
    for i in range(len(List)-1):
        if List[i] == min(List):
            canvas.itemconfig(barList[i], fill='gray')
        elif List[i] == max(List):
            canvas.itemconfig(barList[i], fill='orange')
#Bubble Sort algorithm # [4,3,7,1,2,5]
# نقارن من يسار ونبدل الاكبر مكان الاصغر
check=True
def _bubble_sort():
    global check
    global barList #بتوريني برتب ازاى
    global List #الاصلية
    n=len(List)
    for i in range(n - 1):
        for j in range(n - i - 1): #بنطرح كاونتر اللي قبل كده عشان اتعمله سواب خلاص
            if(List[j] > List[j + 1]):
                (List[j] , List[j + 1]) =( List[j + 1] , List[j])
                barList[j], barList[j + 1] = barList[j + 1] , barList[j]
                swap(barList[j + 1] , barList[j])
                yield #طريقه الترتيب       
                 #  لو شيلتها هيترتب علطول 
                #لو موجوده بيوريني برتب ازاى
    check=False
#algorithm Fuctions
def bubble_sort():  #فانكشن بتحط بتحط الفانكش الاصليه في متغير عشان نستخدمه   
    global worker
    worker = _bubble_sort()
    animate()    
#Animation Function
def animate():      
    global worker
    if worker is not None:
        try:
            next(worker)
            win.after(50, animate)     #سرعة الترتيب 
        except StopIteration:            
            worker = None
        finally:
            win.after_cancel(animate) 

counting= [0 , 0]
#time
def counter():
    global counting
    if start_btn['text'] != 'Bubble Sort algorithm' and check==True :
        counting[0] += 1
        
        if counting[0] == 100:
            counting[1] +=1
            counting[0]= 0
            counting_lb.config(text=f'{datetime.timedelta(seconds=counting[1])}:00')
        else:
            counting_lb.config(text=f'{datetime.timedelta(seconds=counting[1])}:{counting[0]}')
    
    win.after(10,counter)

def counting_command(command):
    if command == 'init':
        start_btn.config(text=' Running')
        counter(),bubble_sort()
    
counting_lb=tk.Label(win,text='0:00:00:00')
counting_lb.grid(column=1,row=1)
#Buttons
start_btn=tk.Button(win,text='Bubble Sort algorithm' , command=lambda:counting_command('init') )
start_btn.grid(column=3,row=1)

bubble = tk.Button(win, text='Fast..?', command=bubble_sort)
bubble.grid(column=6,row=1)


build()
win.mainloop()

# Library used: tkinter
# canvas wedget to creat the window
# Grid system for displaying the data
# Swap function to switch between bars
# /Worker is the intelligent who will go through the bars /
# Bubble sort function to sort the bar length 
# Animation function to desplay the movement of the bar on screen
# Bubble sort button to vie the operation on click