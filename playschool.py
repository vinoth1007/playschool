from tkinter import *
from tkinter import Frame, ttk
import re
import pymysql

def about():
    frame3 = Frame(main_frame, bg='GREY14')
    frame3.place(relx=0, rely=0.05, relheight=1, relwidth=1)

    a = """    About Kidzee Play School .Dream Big & Fly High
    A pioneer in ECCE (Early Childhood Care and Education), we are the largest preschool chain in Asia. With an
    incredible network of more than 1900+ centers in over 750+ cities, we are committed to spearheading child
    development across the nation. Having touched the lives of more than 9,00,000 children in India, Kidzee,
    a decade on, remains focussed on nurturing the ‘unique potential’ in every child A glance at the success
    and achievements of Asia's No. 1 preschool.Awarded National Early Child Play school Chain 2019
    by Franchise India in Feb 2019 Awarded Most Admired Preschool Brand –by White Page International in Dec 2018
    Awarded Innovation In Curriculum In Early Childhood Development by ELETS in Dec 2018
    Awarded Leading brand of the Year – Preschools by WCRC in Apr 2018
    Awarded Preschool Franchisor of the Year (Jury’s Choice 2017) by BW Education Brands in Nov 2017
    Awarded Franchisor of the Year – Preschools by Franchise India Awards 2017 in Nov 2017
    Awarded India’s Most Attractive Brand – Preschool by Trust Research Advisory 2017 in Nov 2017
    K11:57 25-05-2021idzee App awarded for Excellence in Omni-Experience category by IDC Insight Award 2017
    Winner of “Best Content and Delivery Award”, Indian Education Congress in 2011
    Winner of Franchise Plus “Franchisor of the Year” award in 2010
    Winner of Franchising World “Best Franchisor in Education” award in 2009"""

    L1 = Label(frame3, text=a, font=('times new roman bold', 20), bg='GREY14', fg='grey', justify='left')
    L1.place(relx=0, rely=0)

    B1 = Button(frame3, text='BACK', command=frame3.destroy, fg='BLACK', width=10,
                bg='PeachPuff4', bd=10, font=('arial bold', 18))
    B1.place(relx=0.45, rely=0.8)

def submit():

    frame4 = Frame(main_frame, bg='GREY14')
    frame4.place(relx=0.4, rely=0.06, relheight=0.78, relwidth=0.556)

    L11 = Label(frame4, text='FORM SUBMITTED SUCCESSFULLY', font=('times new roman bold', 20),
               bg='GREY14', fg='grey')
    L11.place(relx=0.2, rely=0)

    if not re.search("[a-z]", E1.get()) and len(E1.get()) == 12 and not re.search("[A-Z]", E1.get()):

        L1 = Label(frame4, text='AADHAR NUMBER  : ' + E1.get(), font=('times new roman bold', 15),
                   bg='GREY14', fg='grey')
        L1.place(relx=0, rely=0.1)

        if not re.search("[0-9]", E2.get()) and not re.search("[_@$]", E2.get()) and re.search("[a-z]", E2.get()) \
                or re.search("[A-Z]", E2.get()):
            L1 = Label(frame4, text='STUDENT NAME : ' + E2.get(), font=('times new roman bold', 15),
                       bg='GREY14', fg='grey')
            L1.place(relx=0, rely=0.2)

            if not re.search("[a-z]", E3.get()) and not re.search("[A-Z]", E3.get()):
                L1 = Label(frame4, text=f'STUDENT DOB  : ' + E3.get(), font=('times new roman bold', 15),
                           bg='GREY14', fg='grey')
                L1.place(relx=0, rely=0.3)

                if not re.search("[0-9]", E4.get()) and not re.search("[_@$]",
                                                                      E4.get()) and E4.get() == 'male' or E4.get() == 'female' or \
                        E4.get() == 'MALE' or E4.get() == 'FEMALE':
                    L1 = Label(frame4, text='GENDER  : ' + E4.get(), font=('times new roman bold', 15),
                               bg='GREY14', fg='grey')
                    L1.place(relx=0, rely=0.4)

                    if not re.search("[0-9]", E5.get()) and not re.search("[_@$]", E5.get()) and re.search("[a-z]",
                                                                                                           E5.get()) \
                            or re.search("[A-Z]", E5.get()):
                        L1 = Label(frame4, text='FATHER NAME  : ' + E5.get(), font=('times new roman bold', 15),
                                   bg='GREY14', fg='grey')
                        L1.place(relx=0, rely=0.5)

                        if not re.search("[0-9]", E6.get()) and not re.search("[_@$]", E6.get()) and re.search("[a-z]",
                                                                                                               E6.get()) \
                                or re.search("[A-Z]", E6.get()):
                            L1 = Label(frame4, text='MOTHER NAME  : ' + E6.get(), font=('times new roman bold', 15),
                                       bg='GREY14', fg='grey')
                            L1.place(relx=0, rely=0.6)

                            if not re.search("[0-9]", E7.get()) and not re.search("[_@$]", E7.get()) and re.search(
                                    "[a-z]", E7.get()) \
                                    or re.search("[A-Z]", E7.get()):
                                L1 = Label(frame4, text='GUARDIAN NAME  : ' + E7.get(),
                                           font=('times new roman bold', 15),
                                           bg='GREY14', fg='grey')
                                L1.place(relx=0, rely=0.7)

                                if not re.search("[a-z]", E8.get()) and len(E8.get()) == 10 and not re.search("[A-Z]",
                                                                                                              E8.get()):
                                    L1 = Label(frame4, text='PHONE NO  : ' + E8.get(),
                                               font=('times new roman bold', 15),
                                               bg='GREY14', fg='grey')
                                    L1.place(relx=0, rely=0.8)

                                    if re.search("[a-z]", E9.get()) and len(E9.get()) < 20 and re.search("[_@$]",
                                                                                                         E9.get()):
                                        L1 = Label(frame4, text='MAIL ID  : ' + E9.get(),
                                                   font=('times new roman bold', 15),
                                                   bg='GREY14', fg='grey')
                                        L1.place(relx=0, rely=0.9)

                                        c = pymysql.connect(
                                            user="root",
                                            password="",
                                            host="localhost",
                                            database="kid")

                                        cursor = c.cursor()

                                        try:
                                            cursor.execute(
                                                "INSERT INTO form VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)",
                                                (str(E1.get()), str(E2.get()), str(E3.get()), str(E4.get()),
                                                 str(E5.get()), str(E6.get()),
                                                 str(E7.get()), str(E8.get()), str(E9.get())))
                                            c.commit()
                                            print('Form Updated Successfully')


                                        except:
                                            print('Unable To Update')

                                    else:

                                        frame5 = Frame(main_frame, bg='GREY14')
                                        frame5.place(relx=0.4, rely=0.06, relheight=0.78, relwidth=0.556)

                                        L1 = Label(frame5, text='PLEASE ENTER VALID E-MAIL',
                                                   font=('times new roman bold', 20),
                                                   bg='GREY14', fg='grey')
                                        L1.place(relx=0.15, rely=0.2)

                                else:

                                    frame5 = Frame(main_frame, bg='GREY14')
                                    frame5.place(relx=0.4, rely=0.06, relheight=0.78, relwidth=0.556)

                                    L1 = Label(frame5, text='PLEASE ENTER CORRECT PHONE NO',
                                               font=('times new roman bold', 20),
                                               bg='GREY14', fg='grey')
                                    L1.place(relx=0.15, rely=0.2)

                            else:

                                frame5 = Frame(main_frame, bg='GREY14')
                                frame5.place(relx=0.4, rely=0.06, relheight=0.78, relwidth=0.556)

                                L1 = Label(frame5, text='PLEASE ENTER VALID GUARDIAN NAME',
                                           font=('times new roman bold', 20),
                                           bg='GREY14', fg='grey')
                                L1.place(relx=0.15, rely=0.2)

                        else:

                            frame5 = Frame(main_frame, bg='GREY14')
                            frame5.place(relx=0.4, rely=0.06, relheight=0.78, relwidth=0.556)

                            L1 = Label(frame5, text='PLEASE ENTER VALID MOTHER NAME', font=('times new roman bold', 20),
                                       bg='GREY14', fg='grey')
                            L1.place(relx=0.15, rely=0.2)

                    else:

                        frame5 = Frame(main_frame, bg='GREY14')
                        frame5.place(relx=0.4, rely=0.06, relheight=0.78, relwidth=0.556)

                        L1 = Label(frame5, text='PLEASE ENTER VALID FATHER NAME', font=('times new roman bold', 20),
                                   bg='GREY14', fg='grey')
                        L1.place(relx=0.15, rely=0.2)

                else:

                    frame5 = Frame(main_frame, bg='GREY14')
                    frame5.place(relx=0.4, rely=0.06, relheight=0.78, relwidth=0.556)

                    L1 = Label(frame5, text='PLEASE ENTER CORRECT GENDER', font=('times new roman bold', 20),
                               bg='GREY14', fg='grey')
                    L1.place(relx=0.15, rely=0.2)

            else:

                frame5 = Frame(main_frame, bg='GREY14')
                frame5.place(relx=0.4, rely=0.06, relheight=0.78, relwidth=0.556)

                L1 = Label(frame5, text='PLEASE ENTER CORRECT DOB', font=('times new roman bold', 20),
                           bg='GREY14', fg='grey')
                L1.place(relx=0.15, rely=0.2)

        else:

            frame5 = Frame(main_frame, bg='GREY14')
            frame5.place(relx=0.4, rely=0.06, relheight=0.78, relwidth=0.556)

            L1 = Label(frame5, text='PLEASE ENTER VALID STUDENT NAME', font=('times new roman bold', 20),
                       bg='GREY14', fg='grey')
            L1.place(relx=0.15, rely=0.2)



    else:

        frame5 = Frame(main_frame, bg='GREY14')
        frame5.place(relx=0.4, rely=0.06, relheight=0.78, relwidth=0.556)

        L1 = Label(frame5, text='PLEASE ENTER CORRECT AADHAR NUMBER', font=('times new roman bold', 20),
                   bg='GREY14', fg='grey')
        L1.place(relx=0.1, rely=0.2)


window = Tk()
window.title('REG')
window.geometry('1300x550')

main_frame = Frame(window, bg='DodgerBlue4')
main_frame.pack(fill='both', expand=True)

frame1 = Frame(main_frame, bg='DodgerBlue4')
frame1.place(relx=0, rely=0, relheight=1, relwidth=1)

L1 = Label(frame1, text=' WELCOME TO PLAY SCHOOL', fg='YELLOW2', bg='DodgerBlue4',font=('times new roman bold', 20))
L1.place(relx=0.35, rely=0)

L2 = Label(frame1, text='AADHAR NO',fg='white', bg='DodgerBlue4', font=('times new roman bold', 16))
L2.place(relx=0.05, rely=0.08)

E1 = Entry(frame1, fg='black', bg='white', width=15, font=('arial', 18), bd=10, textvariable='')
E1.place(relx=0.2, rely=0.065)

L2 = Label(frame1, text='STUDENT NAME', fg='white', bg='DodgerBlue4',
           font=('times new roman bold', 15))
L2.place(relx=0.05, rely=0.18)

E2 = Entry(frame1, fg='black', bg='white', width=15, font=('arial', 18), bd=10)
E2.place(relx=0.2, rely=0.165)

L3 = Label(frame1, text='STUDENT DOB', fg='white', bg='DodgerBlue4',font=('times new roman bold', 16))
L3.place(relx=0.05, rely=0.28)

E3 = Entry(frame1, fg='black', bg='white', width=15, font=('arial', 18), bd=10)
E3.place(relx=0.2, rely=0.265)
text = 'DD-MM-YYYY'
E3.insert(0, text)

L4 = Label(frame1, text='GENDER', font=('TIMES NEW ROMAN BOLD', 16),
           fg='white', bg='DodgerBlue4')
L4.place(relx=0.05, rely=0.38)

E4 = Entry(frame1, fg='black', bg='white', width=15, font=('arial', 18), bd=10)
E4.place(relx=0.2, rely=0.365)

L6 = Label(frame1, text='FATHER NAME', fg='white', bg='DodgerBlue4',font=('times new roman bold', 16))
L6.place(relx=0.05, rely=0.48)

E5 = Entry(frame1, fg='black', bg='white', width=18, font=('arial', 15), bd=10)
E5.place(relx=0.2, rely=0.465)

L7 = Label(frame1, text='MOTHER NAME', fg='white', bg='DodgerBlue4',font=('times new roman bold', 16))
L7.place(relx=0.05, rely=0.58)

E6 = Entry(frame1, fg='black', bg='white', width=18, font=('arial', 15), bd=10)
E6.place(relx=0.2, rely=0.565)

L8 = Label(frame1, text='GUARDIAN NAME', fg='white', bg='DodgerBlue4',font=('times new roman bold', 16))
L8.place(relx=0.05, rely=0.68)

E7 = Entry(frame1, fg='black', bg='white', width=18, font=('arial', 15), bd=10)
E7.place(relx=0.2, rely=0.665)

L9 = Label(frame1, text='PHONE NO', fg='white', bg='DodgerBlue4',font=('times new roman bold', 16))
L9.place(relx=0.05, rely=0.78)

E8 = Entry(frame1, fg='black', bg='white', width=18, font=('arial', 15), bd=10)
E8.place(relx=0.2, rely=0.765)

L10 = Label(frame1, text='MAIL ID', fg='white', bg='DodgerBlue4',font=('times new roman bold', 16))
L10.place(relx=0.05, rely=0.88)

E9 = Entry(frame1, fg='black', bg='white', width=18, font=('arial', 15), bd=10)
E9.place(relx=0.2, rely=0.865)

B1 = Button(frame1, text='SUBMIT', fg='BLACK', bg='PeachPuff4',
            width=10, font=('arial bold', 15), bd=10, command=submit)
B1.place(relx=0.4, rely=0.9)

B1 = Button(frame1, text='ABOUT US', fg='BLACK', bg='PeachPuff4', width=10,
font=('arial bold', 15), bd=10, command=about)
B1.place(relx=0.6, rely=0.9)

B1 = Button(frame1, text='EXIT', command=window.destroy, fg='BLACK', width=10,
bg='PeachPuff4', bd=10, font=('arial bold', 15))
B1.place(relx=0.85, rely=0.9)

frame2 = Frame(main_frame, bg='GREY14')
frame2.place(relx=0.4, rely=0.06, relheight=0.78, relwidth=0.556)

mainloop()
