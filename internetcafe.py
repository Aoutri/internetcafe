from tkinter import *
from tkinter.ttk import Combobox
import pandas as pd
from tkcalendar import Calendar

fee = 20 #ค่าบริการ
co = 5 #ต้นทุน

try: #find xls from path
    path = 'C:\Python\python project\internetcafe/internetcafe.csv'
    frame = pd.DataFrame(pd.read_csv(path))
except: #create xls
    empty = {'username': [], 'check in date':[], 'check in':[], 'check out date':[] , 'check out':[], 'fee':[], 'cost':[], 'profit':[]}
    frame = pd.DataFrame(empty)
    frame.to_csv('C:\Python\python project\internetcafe/internetcafe.csv')

def submitted():
    timeInf = float(time[time_in.current()]) #เก็บค่าเวลาเข้า
    timeOutf = float(time[time_out.current()]) #เก็บค่าเวลาออก
    timeIn = int(timeInf)
    timeOut = int(timeOutf) #con to int
    calIn = cal_in.get_date() #get datein
    calOut = cal_out.get_date() #get dateout
    global frame #ประกาศตัวแปร
    try:
        monthIn = int(calIn[0:2])
    except:
        monthIn = int(calIn[0:1])
    try:
        monthOut = int(calOut[0:2])
    except:
        monthOut = int(calOut[0:1])
    if monthIn < 10:
        try:
            dayIn = int(calIn[2:4])
        except:
            dayIn = int(calIn[2:3])
    else:
        try:
            dayIn = int(calIn[3:5])
        except:
            dayIn = int(calIn[3:4])
    if monthOut < 10:
        try:
            dayOut = int(calOut[2:4])
        except:
            dayOut = int(calOut[2:3])
    else:
        try:
            dayOut = int(calOut[3:5])
        except:
            dayOut = int(calOut[3:4])

    if len(calIn) == 6:
        yearIn = int(calIn[4:6])
    elif len(calIn) == 7:
        yearIn = int(calIn[5:7])
    elif len(calIn) == 8:
        yearIn = int(calIn[6:8])
    if len(calOut) == 6:
        yearOut = int(calOut[4:6])
    elif len(calOut) == 7:
        yearOut = int(calOut[5:7])
    elif len(calOut) == 8:
        yearOut = int(calOut[6:8])


    realDay = dayOut - dayIn
    realMonth = abs(monthOut - monthIn)
    realYear = abs(yearOut - yearIn)
    if yearOut ==  yearIn and monthOut < monthIn:
        submit_text = Label(window, text='error!!! wrong time input', fg='red', font=('Helvetica', 12))
        submit_text.place(x=220, y=380)
        submit_text.after(3000, submit_text.destroy)
        print('error!!! wrong time input')
    elif yearOut == yearIn and monthOut == monthIn and dayOut < dayIn:
        submit_text = Label(window, text='error!!! wrong time input', fg='red', font=('Helvetica', 12))
        submit_text.place(x=220, y=380)
        submit_text.after(3000, submit_text.destroy)
        print('error!!! wrong time input')
    elif yearOut == yearIn and monthOut == monthIn and dayOut == dayIn and timeOut < timeIn:
        submit_text = Label(window, text='error!!! wrong time input', fg='red', font=('Helvetica', 12))
        submit_text.place(x=220, y=380)
        submit_text.after(3000, submit_text.destroy)
        print('error!!! wrong time input')
    else:
        if timeOut > timeIn: 
            if len(frame) != 0:
                frame = frame.drop(len(frame)-1)
            time_play = timeOut - timeIn
            bill = time_play * fee
            cost = time_play * co
            profit = bill - cost
            new_mark = {'username': [username.get()], 'check in date':[calIn], 'check in':[timeIn], 'check out date':[calOut], 'check out':[timeOut], 'fee':[bill], 'cost':[cost], 'profit':[profit]} #xls
            mark_df = pd.DataFrame(new_mark)
            frame = pd.concat([frame,mark_df], ignore_index=True)
            sum_profit = {'profit':[frame['profit'].sum()]}
            sum_profit = pd.DataFrame(sum_profit)
            frame = pd.concat([frame,sum_profit], ignore_index=True)
            frame.to_csv('C:\Python\python project\internetcafe/internetcafe.csv', index=False) #save

            submit_text = Label(window, text='Submitted', fg='red', font=('Helvetica', 12))
            submit_text.place(x=220, y=380)
            submit_text.after(3000, submit_text.destroy)

        elif yearIn != yearOut:
            if len(frame) != 0:
                frame = frame.drop(len(frame)-1)
            time_play = ((realYear - 1) * 365 * 24) + (((12 - monthIn) + (monthOut - 1)) * 31 * 24) + (((31 - dayIn) + (dayOut - 1)) * 24) + ((24 - timeIn) + timeOut)
            bill = time_play * fee
            cost = time_play * co
            profit = bill - cost
            new_mark = {'username': [username.get()], 'check in date':[calIn], 'check in':[timeIn], 'check out date':[calOut], 'check out':[timeOut], 'fee':[bill], 'cost':[cost], 'profit':[profit]} #xls
            mark_df = pd.DataFrame(new_mark)
            frame = pd.concat([frame,mark_df], ignore_index=True)
            sum_profit = {'profit':[frame['profit'].sum()]}
            sum_profit = pd.DataFrame(sum_profit)
            frame = pd.concat([frame,sum_profit], ignore_index=True)
            frame.to_csv('C:\Python\python project\internetcafe/internetcafe.csv', index=False) #save

            submit_text = Label(window, text='Submitted', fg='red', font=('Helvetica', 12))
            submit_text.place(x=220, y=380)
            submit_text.after(3000, submit_text.destroy)

        elif monthIn != monthOut:
            if len(frame) != 0:
                frame = frame.drop(len(frame)-1)
            time_play = ((realMonth - 1) * 31 * 24) + (((31 - dayIn) + (dayOut - 1)) * 24) + ((24 - timeIn) + timeOut)
            bill = time_play * fee
            cost = time_play * co
            profit = bill - cost
            new_mark = {'username': [username.get()], 'check in date':[calIn], 'check in':[timeIn], 'check out date':[calOut], 'check out':[timeOut], 'fee':[bill], 'cost':[cost], 'profit':[profit]} #xls
            mark_df = pd.DataFrame(new_mark)
            frame = pd.concat([frame,mark_df], ignore_index=True)
            sum_profit = {'profit':[frame['profit'].sum()]}
            sum_profit = pd.DataFrame(sum_profit)
            frame = pd.concat([frame,sum_profit], ignore_index=True)
            frame.to_csv('C:\Python\python project\internetcafe/internetcafe.csv', index=False) #save

            submit_text = Label(window, text='Submitted', fg='red', font=('Helvetica', 12))
            submit_text.place(x=220, y=380)
            submit_text.after(3000, submit_text.destroy)
            
        elif dayIn != dayOut: #diff day
            if len(frame) != 0:
                frame = frame.drop(len(frame)-1)
            time_play = ((24 - timeIn) + timeOut) + ((realDay - 1) * 24)
            bill = time_play * fee
            cost = time_play * co
            profit = bill - cost
            new_mark = {'username': [username.get()], 'check in date':[calIn], 'check in':[timeIn], 'check out date':[calOut], 'check out':[timeOut], 'fee':[bill], 'cost':[cost], 'profit':[profit]}
            mark_df = pd.DataFrame(new_mark)
            frame = pd.concat([frame,mark_df], ignore_index=True)
            sum_profit = {'profit':[frame['profit'].sum()]}
            sum_profit = pd.DataFrame(sum_profit)
            frame = pd.concat([frame,sum_profit], ignore_index=True)
            frame.to_csv('C:\Python\python project\internetcafe/internetcafe.csv', index=False)

            submit_text = Label(window, text='Submitted', fg='red', font=('Helvetica', 12))
            submit_text.place(x=220, y=380)
            submit_text.after(3000, submit_text.destroy)

        else: #Err
            submit_text = Label(window, text='error!!! wrong time input', fg='red', font=('Helvetica', 12))
            submit_text.place(x=220, y=380)
            submit_text.after(3000, submit_text.destroy)
            print('error!!! wrong time input')

window = Tk()

#username
username_title = Label(window, text='Username', fg='black', font=('Helvetica', 16))
username_title.place(x=30, y=20)
username = Entry(window, text='Enter your username')
username.place(x=30, y=60)

#time in
#time out
time = ['00.00', '01.00', '02.00', '03.00', '04.00', '05.00', '06.00', '07.00', '08.00', '09.00', '10.00', '11.00', '12.00', '13.00', '14.00', '15.00', '16.00', '17.00', '18.00', '19.00', '20.00', '21.00', '22.00', '23.00']

time_title = Label(window, text='Log in - Log out', fg='black', font=('Helvetica', 16))
time_title.place(x=30, y=105)

cal_in = Calendar(window, selectmode = 'day', year = 2022, month = 12, day = 13)
cal_in.place(x=30, y=150)

cal_out = Calendar(window, selectmode = 'day', year = 2022, month = 12, day = 13)
cal_out.place(x=300, y=150)

time_in = Combobox(window, values=time)
time_in.place(x=30, y=330)

time_out = Combobox(window, values=time)
time_out.place(x=300, y=330)

submit = Button(window, text='Submit', font=('Helvetica', 14), command=submitted)
submit.place(x=220, y=400)

window.title('Internet Cafe')
window.geometry('555x475')
window.mainloop()