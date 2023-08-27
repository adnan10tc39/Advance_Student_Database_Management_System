from tkinter import *
from tkcalendar import *
import time
import datetime
from tkinter import ttk,messagebox
import random
import pymysql

class studentRecords:
    def __init__(self,root):
        self.root=root
        self.root.title('Students Record System')
        self.root.geometry('1350x800+0+0')
        notebook =ttk.Notebook(self.root)
        self.TabControll1=ttk.Frame(notebook)
        self.TabControll2 = ttk.Frame(notebook)
        self.TabControll3 = ttk.Frame(notebook)
        notebook.add(self.TabControll1,text='School System')
        notebook.add(self.TabControll2, text='Student Details')
        notebook.grid()

        #===================================variables======================

        self.StudentID=StringVar()
        self.Firstname=StringVar()
        self.Surname=StringVar()
        self.Address=StringVar()
        self.PostCode=StringVar()
        self.Gender=StringVar()
        self.DOB=StringVar()
        self.Mobile = StringVar()
        self.Email = StringVar()

        self.ParentGuidance = StringVar()
        self.pgFirstname = StringVar()
        self.pgSurname = StringVar()
        self.pgAddress = StringVar()
        self.pgWorkPhone = StringVar()
        self.pgMobile = StringVar()
        self.pgEmail = StringVar()

        self.Course = StringVar()
        self.CourseCode = StringVar()
        self.Faculty = StringVar()
        self.Dean = StringVar()
        self.Head_of_School = StringVar()
        self.ProgramLeader = StringVar()
        self.CourseTutor = StringVar()
        self.Building = StringVar()
        self.HomeStudent = StringVar()
        self.Oversea = StringVar()
        self.Accommodation = StringVar()
        self.ExchangeProg = StringVar()
        self.Scholarship = StringVar()

        self.BA = StringVar()
        self.BSc = StringVar()
        self.MA = StringVar()
        self.MSc = StringVar()
        self.PhD = StringVar()

        self.DataScience = StringVar()
        self.EventDrivenPro = StringVar()
        self.ObjectOriented = StringVar()
        self.Spreadsheet = StringVar()
        self.SystemAnalysis = StringVar()
        self.InformTechnology = StringVar()
        self.DigitalGraphics = StringVar()

        self.English = StringVar()
        self.Games = StringVar()
        self.Animation = StringVar()
        self.Database = StringVar()
        self.Maths = StringVar()
        self.AddMaths = StringVar()
        self.Physics = StringVar()
        self.Media = StringVar()
        self.GraphicD = StringVar()

        self.ScoreMaths = StringVar()
        self.ScoreEnglish = StringVar()
        self.ScoreBiology= StringVar()
        self.ScoreComputing = StringVar()
        self.Gender = StringVar()
        self.ExamNo = StringVar()
        self.ScoreChemistry = StringVar()
        self.ScorePhysics = StringVar()
        self.ScoreAddMaths = StringVar()
        self.ScoreBusiness = StringVar()
        self.TotalScore = StringVar()
        self.Average = StringVar()
        self.Ranking = StringVar()
        self.TaxPeriod = StringVar()
        self.iDate = StringVar()

        self.Module1 = StringVar()
        self.Module2 = StringVar()
        self.Module3 = StringVar()
        self.Module4 = StringVar()
        self.Module5 = StringVar()
        self.Module6 = StringVar()
        self.Module7 = StringVar()
        self.Module8 = StringVar()
        self.Ranking = StringVar()
        self.ToatalScore = StringVar()
        self.ResultDate = StringVar()

        self.Subject1 = StringVar()
        self.Subject2 = StringVar()
        self.Subject3 = StringVar()
        self.Subject4 = StringVar()
        self.Subject5 = StringVar()
        self.Subject6 = StringVar()
        self.Subject7 = StringVar()
        self.Subject8 = StringVar()

    #============================================== Frames================================
        MainFrame=Frame(self.TabControll1,bd=10,width=1320,height=700,relief=RIDGE)
        MainFrame.grid(padx=5,pady=5)

        Tab2Frame = Frame(self.TabControll2, bd=10, width=1320, height=700, relief=RIDGE)
        Tab2Frame.grid(padx=5, pady=5)

        TopFrame3 = Frame(MainFrame, bd=10, width=1320, height=500, relief=RIDGE)
        TopFrame3.grid(padx=5, pady=5)

        RightFrame1 = Frame(TopFrame3, bd=5, width=300, height=400,padx=1,bg='cadet blue', relief=RIDGE)
        RightFrame1.pack(side=RIGHT,pady=2)

        InnerRightFrame = Frame(RightFrame1, bd=5, width=290, height=310, padx=1,relief=RIDGE)
        InnerRightFrame.pack(side=TOP, pady=1)

        CalendarFrame = Frame(InnerRightFrame, bd=5, width=290, height=310, padx=1, relief=RIDGE)
        CalendarFrame.pack(side=TOP, pady=1)

        UnitsFrame = Frame(InnerRightFrame, bd=5, width=290, height=310, padx=1, relief=RIDGE)
        UnitsFrame.pack(side=TOP, pady=1)

        ResultFrame = Frame(InnerRightFrame, bd=5, width=300, height=50, padx=1, relief=RIDGE)
        ResultFrame.pack(side=TOP, pady=1)

        ResultFrameLeft = Frame(ResultFrame, bd=0, width=120, height=50, padx=1, relief=RIDGE)
        ResultFrameLeft.grid(row=0,column=0,pady=1)

        # ResultFrameRight = Frame(ResultFrame, bd=0, width=190, height=50, padx=1, relief=RIDGE)
        # ResultFrameRight.grid(row=0, column=0)

        UnitNo=Frame(UnitsFrame, bd=0, width=50, height=290, padx=1, relief=RIDGE)
        UnitNo.grid(row=0, column=0,pady=2)
        UnitSubject = Frame(UnitsFrame, bd=0, width=200, height=290, padx=1,pady=2, relief=RIDGE)
        UnitSubject.grid(row=0, column=1, pady=2)
        UnitScore=Frame(UnitsFrame, bd=0, width=50, height=290, padx=1,pady=1, relief=RIDGE)
        UnitScore.grid(row=0, column=2, pady=1)
        #============================================================================================
        LeftFrame = Frame(TopFrame3, bd=5, width=1315, height=400, padx=1, bg='cadetblue', relief=RIDGE)
        LeftFrame.pack(side=RIGHT, pady=0)
        CourseFrame = Frame(LeftFrame, bd=5, width=550, height=180, padx=2, relief=RIDGE)
        CourseFrame.pack(side=TOP, pady=1)

        LeftFrame2 = Frame(LeftFrame, bd=5, width=550, height=180, padx=1, bg='cadetblue', relief=RIDGE)
        LeftFrame2.pack(side=TOP)
        StudentStatusFrame = Frame(LeftFrame2, bd=5, width=275, height=170, padx=1, relief=RIDGE)
        StudentStatusFrame.pack(side=LEFT)
        DegreeFrame = Frame(LeftFrame2, bd=5, width=275, height=170, padx=1, relief=RIDGE)
        DegreeFrame.pack(side=RIGHT)

        ButtonFrame = Frame(LeftFrame, bd=5, width=290, height=50, padx=2, relief=RIDGE)
        ButtonFrame.pack(side=LEFT,pady=2)

        RightFrame2= Frame(TopFrame3, bd=5, width=290, height=400, padx=2,bg='cadetblue', relief=RIDGE)
        RightFrame2.pack(side=LEFT,pady=3)
        StudentFrame = Frame(RightFrame2, bd=5, width=275, height=50, padx=2, relief=RIDGE)
        StudentFrame.pack(side=TOP, pady=2)
        ParentFrame = Frame(RightFrame2, bd=5, width=275, height=50, padx=2, relief=RIDGE)
        ParentFrame.pack(side=TOP)

        TopFrame11 = Frame(Tab2Frame, bd=10, width=1310, height=60, relief=RIDGE)
        TopFrame11.grid(row=0,column=0)
        TopFrame12 = Frame(Tab2Frame, bd=10, width=1310, height=100, relief=RIDGE)
        TopFrame12.grid(row=1, column=0)

        TopFrame12a = Frame(TopFrame12, bd=10, width=1310, height=100, relief=RIDGE)
        TopFrame12a.grid(row=1, column=1)
        TopFrame12b = Frame(TopFrame12, bd=10, width=320, height=100, relief=RIDGE)
        TopFrame12b.grid(row=1, column=0)
        #=================================================================================================

        self.lblStudentID = Label(StudentFrame,font=('arial', 12, 'bold'), text='Student ID',bd=5, anchor='w',justify=LEFT)
        self.lblStudentID.grid(row=0, column=0, sticky='w',padx=2,pady=2)
        self.txtStudentID = Entry(StudentFrame, font=('arial', 12, 'bold'),bd=2,width=25,justify='left',textvariable=self.StudentID)
        self.txtStudentID.grid(row=0, column=1)

        self.lblFirstname = Label(StudentFrame, font=('arial', 12, 'bold'), text='First Name', bd=5, anchor='w',
                                  justify=LEFT)
        self.lblFirstname.grid(row=1, column=0, sticky='w', padx=2)
        self.txtFirstname = Entry(StudentFrame, font=('arial', 12, 'bold'), bd=2, width=25, justify='left',
                                  textvariable=self.Firstname)
        self.txtFirstname.grid(row=1, column=1)

        self.lblSurname = Label(StudentFrame, font=('arial', 12, 'bold'), text='Surname', bd=5, anchor='w',
                                  justify=LEFT)
        self.lblSurname.grid(row=2, column=0, sticky='w', padx=3, pady=3)
        self.txtSurname = Entry(StudentFrame, font=('arial', 12, 'bold'), bd=2, width=25, justify=LEFT,
                                  textvariable=self.Surname)
        self.txtSurname.grid(row=2, column=1)

        self.lblAddress = Label(StudentFrame, font=('arial', 12, 'bold'), text='Address', bd=5, anchor='w')
        self.lblAddress.grid(row=3, column=0, sticky='w', padx=3, pady=3)
        self.txtAddress = Entry(StudentFrame, font=('arial', 12, 'bold'), bd=2, width=25, justify=LEFT,
                                  textvariable=self.Address)
        self.txtAddress.grid(row=3, column=1)

        self.lblPostCode = Label(StudentFrame, font=('arial', 12, 'bold'), text='Post Code', bd=5, anchor='w')
        self.lblPostCode.grid(row=4, column=0, sticky='w', padx=3, pady=3)
        self.txtPostCode = Entry(StudentFrame, font=('arial', 12, 'bold'), bd=2, width=25, justify=LEFT,
                                  textvariable=self.PostCode)
        self.txtPostCode.grid(row=4, column=1)

        self.lblGender = Label(StudentFrame, font=('arial', 12, 'bold'), text='Gender', bd=5)
        self.lblGender.grid(row=5, column=0, sticky='w', padx=3)
        self.cboGender =ttk.Combobox(StudentFrame, font=('arial', 12, 'bold'), width=23, justify=LEFT,
                                 textvariable=self.Gender,state='readonly')
        self.cboGender['value']=('','Female','Male')
        self.cboGender.current(0)
        self.cboGender.grid(row=5, column=1)

        self.lblDOB = Label(StudentFrame, font=('arial', 12, 'bold'), text='DOB', bd=5, anchor='w')
        self.lblDOB.grid(row=6, column=0, sticky='w', padx=3, pady=3)
        self.txtDOB = Entry(StudentFrame, font=('arial', 12, 'bold'), bd=2, width=25, justify=LEFT,
                                 textvariable=self.DOB)
        self.txtDOB.grid(row=6, column=1)

        self.lblMobile = Label(StudentFrame, font=('arial', 12, 'bold'), text='Mobile', bd=5, anchor='w')
        self.lblMobile.grid(row=7, column=0, sticky='w', padx=3, pady=3)
        self.txtMobile = Entry(StudentFrame, font=('arial', 12, 'bold'), bd=2, width=25, justify=LEFT,
                                 textvariable=self.Mobile)
        self.txtMobile.grid(row=7, column=1)

        self.lblEmail = Label(StudentFrame, font=('arial', 12, 'bold'), text='Email', bd=5, anchor='w')
        self.lblEmail.grid(row=8, column=0, sticky='w', padx=3, pady=3)
        self.txtEmail = Entry(StudentFrame, font=('arial', 12, 'bold'), bd=2, width=25, justify=LEFT,
                                 textvariable=self.Email)
        self.txtEmail.grid(row=8, column=1)
        #====================================================================================================

        self.lblParentGuidence = Label(ParentFrame, font=('arial', 12, 'bold'), text='Parent or Guidance', bd=5)
        self.lblParentGuidence.grid(row=0, column=0, sticky='w', padx=3)
        self.cboParentGuidence = ttk.Combobox(ParentFrame, font=('arial', 12, 'bold'), width=15,
                                      textvariable=self.ParentGuidance, state='readonly')
        self.cboParentGuidence['value'] = ('', 'Mother', 'Father','Brother', 'Sister','Guidance')
        self.cboParentGuidence.current(0)
        self.cboParentGuidence.grid(row=0, column=1)

        self.lblpgFirstname = Label(ParentFrame, font=('arial', 12, 'bold'), text='First Name', bd=5, anchor='w',
                                  justify=LEFT)
        self.lblpgFirstname.grid(row=1, column=0, sticky='w', padx=2)
        self.txtpgFirstname = Entry(ParentFrame, font=('arial', 12, 'bold'), bd=2, width=17, justify='left',
                                  textvariable=self.pgFirstname)
        self.txtpgFirstname.grid(row=1, column=1)

        self.lblpgSurname = Label(ParentFrame, font=('arial', 12, 'bold'), text='Surname', bd=5, anchor='w',
                                justify=LEFT)
        self.lblpgSurname.grid(row=2, column=0, sticky='w', padx=3, pady=3)
        self.txtpgSurname = Entry(ParentFrame, font=('arial', 12, 'bold'), bd=2, width=17, justify=LEFT,
                                textvariable=self.pgSurname)
        self.txtpgSurname.grid(row=2, column=1)

        self.lblpgAddress = Label(ParentFrame, font=('arial', 12, 'bold'), text='Address', bd=5, anchor='w')
        self.lblpgAddress.grid(row=3, column=0, sticky='w', padx=3, pady=3)
        self.txtpgAddress = Entry(ParentFrame, font=('arial', 12, 'bold'), bd=2, width=17, justify=LEFT,
                                textvariable=self.pgAddress)
        self.txtpgAddress.grid(row=3, column=1)

        self.lblpgWorkPhone = Label(ParentFrame, font=('arial', 12, 'bold'), text='Work Phone No', bd=5, anchor='w')
        self.lblpgWorkPhone.grid(row=4, column=0, sticky='w', padx=3, pady=3)
        self.txtpgWorkPhone = Entry(ParentFrame, font=('arial', 12, 'bold'), bd=2, width=17, justify=LEFT,
                                 textvariable=self.pgWorkPhone)
        self.txtpgWorkPhone.grid(row=4, column=1)

        self.lblpgMobile = Label(ParentFrame, font=('arial', 12, 'bold'), text='Mobile', bd=5, anchor='w')
        self.lblpgMobile.grid(row=5, column=0, sticky='w', padx=3, pady=3)
        self.txtpgMobile = Entry(ParentFrame, font=('arial', 12, 'bold'), bd=2, width=17, justify=LEFT,
                                textvariable=self.pgMobile)
        self.txtpgMobile.grid(row=5, column=1)

        self.lblpgEmail = Label(ParentFrame, font=('arial', 12, 'bold'), text='Email', bd=5, anchor='w')
        self.lblpgEmail.grid(row=6, column=0, sticky='w', padx=3, pady=3)
        self.lblpgEmail = Entry(ParentFrame, font=('arial', 12, 'bold'), bd=2, width=17,textvariable=self.pgEmail)
        self.lblpgEmail.grid(row=6, column=1)

        #==============================================Course Frame=============================================
        self.Course.set('Course Selector')
        self.lblCourse=Label(CourseFrame, font=('arial', 12, 'bold'), text='Course', bd=5, anchor='w')
        self.lblCourse.grid(row=0, column=0,sticky=W)

        self.cboCourse = ttk.Combobox(CourseFrame, font=('arial', 12, 'bold'), width=50,textvariable=self.Course, state='readonly')
        self.cboCourse['value'] = ('','Bsc Serious Game','BSc Computer Science','BA Animation','BSc Information System',
                                   'BSc Computing','BSc Computer Game','BSc Computer Animation')
        self.cboCourse.current(0)
        self.cboCourse.grid(row=0, column=1)
        self.cboCourse.bind('<<ComboboxSelected>>',self.CourseData)

        self.lblCourseCode = Label(CourseFrame, font=('arial', 12, 'bold'), text='Course Code', bd=5, anchor='w')
        self.lblCourseCode.grid(row=1, column=0, sticky='w', padx=3)
        self.txtCourseCode = Entry(CourseFrame, font=('arial', 12, 'bold'), bd=2, width=52, textvariable=self.CourseCode)
        self.txtCourseCode.grid(row=1, column=1)

        self.lblFacultyName = Label(CourseFrame, font=('arial', 12, 'bold'), text='Faculty Name', bd=5, anchor='w')
        self.lblFacultyName.grid(row=2, column=0, sticky='w', padx=3)
        self.txtFacultyName = Entry(CourseFrame, font=('arial', 12, 'bold'), bd=2, width=52,
                                   textvariable=self.Faculty)
        self.txtFacultyName.grid(row=2, column=1)

        self.lblFacultyDean = Label(CourseFrame, font=('arial', 12, 'bold'), text='Dean Of Faculty', bd=5, anchor='w')
        self.lblFacultyDean.grid(row=3, column=0, sticky='w', padx=3)
        self.txtFacultyDean = Entry(CourseFrame, font=('arial', 12, 'bold'), bd=2, width=52,
                                   textvariable=self.Dean)
        self.txtFacultyDean.grid(row=3, column=1)

        self.lblSchoolHead = Label(CourseFrame, font=('arial', 12, 'bold'), text='Head Of School', bd=5, anchor='w')
        self.lblSchoolHead.grid(row=4, column=0, sticky='w', padx=3)
        self.txtSchoolHead = Entry(CourseFrame, font=('arial', 12, 'bold'), bd=2, width=52,
                                   textvariable=self.Head_of_School)
        self.txtSchoolHead.grid(row=4, column=1)

        self.lblProgramLeader = Label(CourseFrame, font=('arial', 12, 'bold'), text='Program Leader', bd=5, anchor='w')
        self.lblProgramLeader.grid(row=5, column=0, sticky='w', padx=3)
        self.txtProgramLeader = Entry(CourseFrame, font=('arial', 12, 'bold'), bd=2, width=52,
                                   textvariable=self.ProgramLeader)
        self.txtProgramLeader.grid(row=5, column=1)

        self.lblCourseTutor = Label(CourseFrame, font=('arial', 12, 'bold'), text='Course Tutor', bd=5, anchor='w')
        self.lblCourseTutor.grid(row=6, column=0, sticky='w', padx=3)
        self.txtCourseTutor = Entry(CourseFrame, font=('arial', 12, 'bold'), bd=2, width=52,
                                   textvariable=self.CourseTutor)
        self.txtCourseTutor.grid(row=6, column=1)

        self.lblBuilding = Label(CourseFrame, font=('arial', 12, 'bold'), text='Building', bd=5, anchor='w')
        self.lblBuilding.grid(row=7, column=0, sticky='w', padx=3)
        self.txtBuilding = Entry(CourseFrame, font=('arial', 12, 'bold'), bd=2, width=52,
                                   textvariable=self.Building)
        self.txtBuilding.grid(row=7, column=1)

        # ==============================================Course Status Frame=========================================
        self.lblHomeStudent = Label(StudentStatusFrame, font=('arial', 12, 'bold'), text='Home Student', bd=5, anchor='w')
        self.lblHomeStudent.grid(row=0, column=0, sticky=W)
        self.cboHomeStudent = ttk.Combobox(StudentStatusFrame, font=('arial', 12, 'bold'),width=14, textvariable=self.HomeStudent,state='readonly')
        self.cboHomeStudent['value'] = ('No','Yes')
        self.cboHomeStudent.current(0)
        self.cboHomeStudent.grid(row=0, column=1,pady=7)

        self.lblOversea = Label(StudentStatusFrame, font=('arial', 12, 'bold'), text='Oversea Student', bd=5,
                                    anchor='w')
        self.lblOversea.grid(row=1, column=0, sticky=W)
        self.cboOversea = ttk.Combobox(StudentStatusFrame, font=('arial', 12, 'bold'), width=14,
                                           textvariable=self.Oversea, state='readonly')
        self.cboOversea['value'] = ('No', 'Yes')
        self.cboOversea.current(0)
        self.cboOversea.grid(row=1, column=1, pady=7)

        self.lblAccommodation = Label(StudentStatusFrame, font=('arial', 12, 'bold'), text='Accommodation', bd=5,
                                    anchor='w')
        self.lblAccommodation.grid(row=2, column=0, sticky=W)
        self.cboAccommodation = ttk.Combobox(StudentStatusFrame, font=('arial', 12, 'bold'), width=14,
                                           textvariable=self.Accommodation, state='readonly')
        self.cboAccommodation['value'] = ('No', 'Yes')
        self.cboAccommodation.current(0)
        self.cboAccommodation.grid(row=2, column=1, pady=7)

        self.lblExchangeProg = Label(StudentStatusFrame, font=('arial', 12, 'bold'), text='Exchange Prog', bd=5,
                                    anchor='w')
        self.lblExchangeProg.grid(row=3, column=0, sticky=W)
        self.cboExchangeProg = ttk.Combobox(StudentStatusFrame, font=('arial', 12, 'bold'), width=14,
                                           textvariable=self.ExchangeProg, state='readonly')
        self.cboExchangeProg['value'] = ('No', 'Yes')
        self.cboExchangeProg.current(0)
        self.cboExchangeProg.grid(row=3, column=1, pady=7)

        self.lblScholarship = Label(StudentStatusFrame, font=('arial', 12, 'bold'), text='ScholarSsip', bd=5,
                                    anchor='w')
        self.lblScholarship.grid(row=4, column=0, sticky=W)
        self.cboScholarship = ttk.Combobox(StudentStatusFrame, font=('arial', 12, 'bold'), width=14,
                                           textvariable=self.Scholarship, state='readonly')
        self.cboScholarship['value'] = ('No', 'Yes')
        self.cboScholarship.current(0)
        self.cboScholarship.grid(row=4, column=1, pady=7)

        #============================================== Degree Frame======================================

        self.lblBA = Label(DegreeFrame, font=('arial', 12, 'bold'), text='Bachelor of Art', bd=9)
        self.lblBA.grid(row=0, column=0, sticky=W)
        self.SpBA = Spinbox(DegreeFrame,from_=0,to=20, font=('arial', 12, 'bold'), width=9,textvariable=self.BA)
        self.SpBA.grid(row=0, column=1, pady=5)

        self.lblBSc = Label(DegreeFrame, font=('arial', 12, 'bold'), text='Bachelor of Science',bd=9)
        self.lblBSc.grid(row=1, column=0, sticky=W)
        self.SpBSc = Spinbox(DegreeFrame, from_=0, to=20, font=('arial', 12, 'bold'), width=9,textvariable=self.BSc)
        self.SpBSc.grid(row=1, column=1, pady=5)

        self.lblMA = Label(DegreeFrame, font=('arial', 12, 'bold'), text='Master of Art', bd=9)
        self.lblMA.grid(row=2, column=0, sticky=W)
        self.SpMA = Spinbox(DegreeFrame, from_=0, to=20, font=('arial', 12, 'bold'), width=9, textvariable=self.MA)
        self.SpMA.grid(row=2, column=1, pady=5)

        self.lblMSc = Label(DegreeFrame, font=('arial', 12, 'bold'), text='Master of Science', bd=9)
        self.lblMSc.grid(row=3, column=0, sticky=W)
        self.SpMSc = Spinbox(DegreeFrame, from_=0, to=20, font=('arial', 12, 'bold'), width=9, textvariable=self.MSc)
        self.SpMSc.grid(row=3, column=1, pady=5)

        self.lblPhD = Label(DegreeFrame, font=('arial', 12, 'bold'), text='Doctor of Philosopy', bd=9)
        self.lblPhD.grid(row=4, column=0, sticky=W)
        self.SpPhD = Spinbox(DegreeFrame, from_=0, to=20, font=('arial', 12, 'bold'), width=9, textvariable=self.PhD)
        self.SpPhD.grid(row=4, column=1, pady=5)

        #============================calender Frame=====================================================
        def getSelectDate():
            nowDate=cal.get_date()
            self.ResultDate.set(nowDate)
            self.AddModulescore()

        cal =Calendar(CalendarFrame,selectmode="day",patren='dd-mm-yyyy',font=('arial', 9, 'bold'),padx=100)
        cal.grid(row=0,column=0)

        #========================================unit No frame===========================================
        self.lblNo = Label(UnitNo, font=('arial', 12, 'bold'), text='No',padx=2,pady=2)
        self.lblNo.grid(row=0, column=0, sticky=W)

        self.lbl1 = Label(UnitNo, font=('arial', 12, 'bold'), text='1',padx=2,pady=2)
        self.lbl1.grid(row=1, column=0, sticky=W)

        self.lbl2 = Label(UnitNo, font=('arial', 12, 'bold'), text='2',padx=2,pady=2)
        self.lbl2.grid(row=2, column=0, sticky=W)

        self.lbl3 = Label(UnitNo, font=('arial', 12, 'bold'), text='3', padx=2,pady=2)
        self.lbl3.grid(row=3, column=0, sticky=W)

        self.lbl4 = Label(UnitNo, font=('arial', 12, 'bold'), text='4',padx=2,pady=2)
        self.lbl4.grid(row=4, column=0, sticky=W)

        self.lbl5 = Label(UnitNo, font=('arial', 12, 'bold'), text='5',padx=2,pady=2)
        self.lbl5.grid(row=5, column=0, sticky=W)

        self.lbl6 = Label(UnitNo, font=('arial', 12, 'bold'), text='6',padx=2,pady=2)
        self.lbl6.grid(row=6, column=0, sticky=W)

        self.lbl7 = Label(UnitNo, font=('arial', 12, 'bold'), text='7',padx=2,pady=2)
        self.lbl7.grid(row=7, column=0, sticky=W)

        self.lbl8 = Label(UnitNo, font=('arial', 12, 'bold'), text='8',padx=2,pady=2)
        self.lbl8.grid(row=8, column=0, sticky=W)

        #===============================unit Subject====================================
        self.lblSelectUnit=Label(UnitSubject,font=('arial', 12, 'bold'), text='Select the Subject')
        self.lblSelectUnit.grid(row=0, column=0, sticky=W)

        self.cboSubject1 = ttk.Combobox(UnitSubject, font=('arial', 10, 'bold'), width=18,
                                           textvariable=self.Subject1, state='readonly')
        self.cboSubject1['value'] = ('', 'Event Driven Prog')
        self.cboSubject1.current(0)
        self.cboSubject1.grid(row=1, column=0,padx=2,pady=3)
        self.cboSubject1.bind('<<ComboboxSelected>>',self.setSubject)

        self.cboSubject2 = ttk.Combobox(UnitSubject, font=('arial', 10, 'bold'), width=18,
                                        textvariable=self.Subject2, state='readonly')
        self.cboSubject2['value'] = ('', 'Object Oriented','Spreadsheet')
        self.cboSubject2.current(0)
        self.cboSubject2.grid(row=2, column=0, padx=2, pady=3)
        self.cboSubject2.bind('<<ComboboxSelected>>', self.setSubject)

        self.cboSubject3 = ttk.Combobox(UnitSubject, font=('arial', 10, 'bold'), width=18,
                                        textvariable=self.Subject3, state='readonly')
        self.cboSubject3['value'] = ('', 'System Analysis', 'Inform Technology')
        self.cboSubject3.current(0)
        self.cboSubject3.grid(row=3, column=0, padx=2, pady=3)
        self.cboSubject3.bind('<<ComboboxSelected>>', self.setSubject)

        self.cboSubject4 = ttk.Combobox(UnitSubject, font=('arial', 10, 'bold'), width=18,
                                        textvariable=self.Subject4, state='readonly')
        self.cboSubject4['value'] = ('', 'Digital Graphics', 'English')
        self.cboSubject4.current(0)
        self.cboSubject4.grid(row=4, column=0, padx=2, pady=3)
        self.cboSubject4.bind('<<ComboboxSelected>>', self.setSubject)

        self.cboSubject5 = ttk.Combobox(UnitSubject, font=('arial', 10, 'bold'), width=18,
                                        textvariable=self.Subject5, state='readonly')
        self.cboSubject5['value'] = ('', 'Games', 'Animation')
        self.cboSubject5.current(0)
        self.cboSubject5.grid(row=5, column=0, padx=2, pady=3)
        self.cboSubject5.bind('<<ComboboxSelected>>', self.setSubject)

        self.cboSubject6 = ttk.Combobox(UnitSubject, font=('arial', 10, 'bold'), width=18,
                                        textvariable=self.Subject6, state='readonly')
        self.cboSubject6['value'] = ('', 'Database', 'Maths')
        self.cboSubject6.current(0)
        self.cboSubject6.grid(row=6, column=0, padx=2, pady=3)
        self.cboSubject6.bind('<<ComboboxSelected>>', self.setSubject)

        self.cboSubject7 = ttk.Combobox(UnitSubject, font=('arial', 10, 'bold'), width=18,
                                        textvariable=self.Subject7, state='readonly')
        self.cboSubject7['value'] = ('', 'AddMaths', 'Physics')
        self.cboSubject7.current(0)
        self.cboSubject7.grid(row=7, column=0, padx=2, pady=3)
        self.cboSubject7.bind('<<ComboboxSelected>>', self.setSubject)

        self.cboSubject8 = ttk.Combobox(UnitSubject, font=('arial', 10, 'bold'), width=18,
                                        textvariable=self.Subject8, state='readonly')
        self.cboSubject8['value'] = ('', 'Data Science')
        self.cboSubject8.current(0)
        self.cboSubject8.grid(row=8, column=0, padx=2, pady=3)
        self.cboSubject8.bind('<<ComboboxSelected>>', self.setSubject)


        #==========================================UnitScore=================================
        self.lblSUnit = Label(UnitScore , font=('arial', 12, 'bold'), text='Score')
        self.lblSUnit.grid(row=0, column=0, sticky=W)

        self.txt1 = Entry(UnitScore, font=('arial', 12, 'bold'),  width=5,textvariable=self.Module1,state=DISABLED)
        self.txt1.grid(row=1, column=0, padx=2, pady=2)

        self.txt2 = Entry(UnitScore, font=('arial', 12, 'bold'), width=5, textvariable=self.Module2,
                          state=DISABLED)
        self.txt2.grid(row=2, column=0, padx=2, pady=2)

        self.txt3 = Entry(UnitScore, font=('arial', 12, 'bold'),  width=5, textvariable=self.Module3,
                          state=DISABLED)
        self.txt3.grid(row=3, column=0, padx=2, pady=2)

        self.txt4 = Entry(UnitScore, font=('arial', 12, 'bold'), width=5, textvariable=self.Module4,
                          state=DISABLED)
        self.txt4.grid(row=4, column=0, padx=2, pady=2)

        self.txt5 = Entry(UnitScore, font=('arial', 12, 'bold'),  width=5, textvariable=self.Module5,
                          state=DISABLED)
        self.txt5.grid(row=5, column=0, padx=2, pady=2)

        self.txt6 = Entry(UnitScore, font=('arial', 12, 'bold'), width=5, textvariable=self.Module6,
                          state=DISABLED)
        self.txt6.grid(row=6, column=0, padx=2, pady=2)

        self.txt7 = Entry(UnitScore, font=('arial', 12, 'bold'), width=5, textvariable=self.Module7,
                          state=DISABLED)
        self.txt7.grid(row=7, column=0, padx=2, pady=2)

        self.txt8 = Entry(UnitScore, font=('arial', 12, 'bold'), width=5, textvariable=self.Module8,
                          state=DISABLED)
        self.txt8.grid(row=8, column=0, padx=2, pady=2)

        #====================================================================================================
        self.lblTotalScore = Label(ResultFrameLeft, font=('arial', 13, 'bold'), text='Total Score')
        self.lblTotalScore.grid(row=0, column=0, sticky='w')
        self.txtTotalScore = Entry(ResultFrameLeft, font=('arial', 13, 'bold'),width=16,textvariable=self.TotalScore)
        self.txtTotalScore.grid(row=0, column=1)

        self.lblRanking = Label(ResultFrameLeft, font=('arial', 13, 'bold'), text='Ranking')
        self.lblRanking.grid(row=1, column=0, sticky='w')
        self.txtRanking = Entry(ResultFrameLeft, font=('arial', 13, 'bold'), width=16, textvariable=self.Ranking)
        self.txtRanking.grid(row=1, column=1)

        self.lblDate = Label(ResultFrameLeft, font=('arial', 13, 'bold'), text='Date')
        self.lblDate.grid(row=2, column=0, sticky='w')
        self.txtDate = Entry(ResultFrameLeft, font=('arial', 13, 'bold'), width=16, textvariable=self.ResultDate)
        self.txtDate.grid(row=2, column=1)

        #=============================================2nd Tab title=========================================
        self.lblTitle = Label(TopFrame11, font=('arial', 40, 'bold'), text='Student Details Management System', bd=5,justify=CENTER)
        self.lblTitle.grid(padx=168)
        # =============================================2nd Tab=========================================

        self.lblDataScience = Label(TopFrame12b, font=('arial', 12, 'bold'), text='Data Science', bd=7,
                                    anchor='e')
        self.lblDataScience.grid(row=0, column=0, sticky=W)
        self.cboDataScience = ttk.Combobox(TopFrame12b, font=('arial', 12, 'bold'), width=19,
                                           textvariable=self.DataScience, state='readonly')
        self.cboDataScience['value'] = ('No','Core Unit', 'Yes','Complete')
        self.cboDataScience.current(0)
        self.cboDataScience.grid(row=0, column=1)

        self.lblEventDrivenPro = Label(TopFrame12b, font=('arial', 12, 'bold'), text='Event Driven Prog', bd=7,
                                    anchor='e')
        self.lblEventDrivenPro.grid(row=1, column=0, sticky=W)
        self.cboEventDrivenPro = ttk.Combobox(TopFrame12b, font=('arial', 12, 'bold'), width=19,
                                           textvariable=self.EventDrivenPro, state='readonly')
        self.cboEventDrivenPro['value'] = ('No', 'Core Unit', 'Yes', 'Complete')
        self.cboEventDrivenPro.current(0)
        self.cboEventDrivenPro.grid(row=1, column=1)

        self.lblObjectOriented = Label(TopFrame12b, font=('arial', 12, 'bold'), text='object Oriented', bd=7,
                                    anchor='e')
        self.lblObjectOriented.grid(row=2, column=0, sticky=W)
        self.cboObjectOriented = ttk.Combobox(TopFrame12b, font=('arial', 12, 'bold'), width=19,
                                           textvariable=self.ObjectOriented, state='readonly')
        self.cboObjectOriented['value'] = ('No', 'Core Unit', 'Yes', 'Complete')
        self.cboObjectOriented.current(0)
        self.cboObjectOriented.grid(row=2, column=1)

        self.lblSpreadsheet = Label(TopFrame12b, font=('arial', 12, 'bold'), text='Spreadsheet', bd=7,
                                    anchor='e')
        self.lblSpreadsheet.grid(row=3, column=0, sticky=W)
        self.cboSpreadsheet = ttk.Combobox(TopFrame12b, font=('arial', 12, 'bold'), width=19,
                                           textvariable=self.Spreadsheet, state='readonly')
        self.cboSpreadsheet['value'] = ('No', 'Core Unit', 'Yes', 'Complete')
        self.cboSpreadsheet.current(0)
        self.cboSpreadsheet.grid(row=3, column=1)

        self.lblSystemAnalysis = Label(TopFrame12b, font=('arial', 12, 'bold'), text='System Analysis', bd=7,
                                    anchor='e')
        self.lblSystemAnalysis.grid(row=4, column=0, sticky=W)
        self.cboSystemAnalysis = ttk.Combobox(TopFrame12b, font=('arial', 12, 'bold'), width=19,
                                           textvariable=self.SystemAnalysis, state='readonly')
        self.cboSystemAnalysis['value'] = ('No', 'Core Unit', 'Yes', 'Complete')
        self.cboSystemAnalysis.current(0)
        self.cboSystemAnalysis.grid(row=4, column=1)

        self.lblInformTechnology = Label(TopFrame12b, font=('arial', 12, 'bold'), text='Inform Technology', bd=7,
                                    anchor='e')
        self.lblInformTechnology.grid(row=5, column=0, sticky=W)
        self.cboInformTechnology = ttk.Combobox(TopFrame12b, font=('arial', 12, 'bold'), width=19,
                                           textvariable=self.InformTechnology, state='readonly')
        self.cboInformTechnology['value'] = ('No', 'Core Unit', 'Yes', 'Complete')
        self.cboInformTechnology.current(0)
        self.cboInformTechnology.grid(row=5, column=1)

        self.lblDigitalGraphics = Label(TopFrame12b, font=('arial', 12, 'bold'), text='Digital Graphics', bd=7,
                                    anchor='e')
        self.lblDigitalGraphics.grid(row=6, column=0, sticky=W)
        self.cboDigitalGraphics = ttk.Combobox(TopFrame12b, font=('arial', 12, 'bold'), width=19,
                                           textvariable=self.DigitalGraphics, state='readonly')
        self.cboDigitalGraphics['value'] = ('No', 'Core Unit', 'Yes', 'Complete')
        self.cboDigitalGraphics.current(0)
        self.cboDigitalGraphics.grid(row=6, column=1)

        self.lblEnglish = Label(TopFrame12b, font=('arial', 12, 'bold'), text='English', bd=7,
                                    anchor='e')
        self.lblEnglish.grid(row=7, column=0, sticky=W)
        self.cboEnglish = ttk.Combobox(TopFrame12b, font=('arial', 12, 'bold'), width=19,
                                           textvariable=self.English, state='readonly')
        self.cboEnglish['value'] = ('No', 'Core Unit', 'Yes', 'Complete')
        self.cboEnglish.current(0)
        self.cboEnglish.grid(row=7, column=1)

        self.lblGames = Label(TopFrame12b, font=('arial', 12, 'bold'), text='Games', bd=7,
                                    anchor='e')
        self.lblGames.grid(row=8, column=0, sticky=W)
        self.cboGames = ttk.Combobox(TopFrame12b, font=('arial', 12, 'bold'), width=19,
                                           textvariable=self.Games, state='readonly')
        self.cboGames['value'] = ('No', 'Core Unit', 'Yes', 'Complete')
        self.cboGames.current(0)
        self.cboGames.grid(row=8, column=1)

        self.lblAnimation = Label(TopFrame12b, font=('arial', 12, 'bold'), text='Animation', bd=7,
                                    anchor='e')
        self.lblAnimation.grid(row=9, column=0, sticky=W)
        self.cboAnimation = ttk.Combobox(TopFrame12b, font=('arial', 12, 'bold'), width=19,
                                           textvariable=self.Animation, state='readonly')
        self.cboAnimation['value'] = ('No', 'Core Unit', 'Yes', 'Complete')
        self.cboAnimation.current(0)
        self.cboAnimation.grid(row=9, column=1)

        self.lblDatabase = Label(TopFrame12b, font=('arial', 12, 'bold'), text='Database', bd=7,
                                    anchor='e')
        self.lblDatabase.grid(row=10, column=0, sticky=W)
        self.cboDatabase = ttk.Combobox(TopFrame12b, font=('arial', 12, 'bold'), width=19,
                                           textvariable=self.Database, state='readonly')
        self.cboDatabase['value'] = ('No', 'Core Unit', 'Yes', 'Complete')
        self.cboDatabase.current(0)
        self.cboDatabase.grid(row=10, column=1)

        self.lblMaths = Label(TopFrame12b, font=('arial', 12, 'bold'), text='Maths', bd=7,
                                    anchor='e')
        self.lblMaths.grid(row=11, column=0, sticky=W)
        self.cboMaths = ttk.Combobox(TopFrame12b, font=('arial', 12, 'bold'), width=19,
                                           textvariable=self.Maths, state='readonly')
        self.cboMaths['value'] = ('No', 'Core Unit', 'Yes', 'Complete')
        self.cboMaths.current(0)
        self.cboMaths.grid(row=11, column=1)

        self.lblAddMaths = Label(TopFrame12b, font=('arial', 12, 'bold'), text='AddMaths', bd=7,
                                    anchor='e')
        self.lblAddMaths.grid(row=12, column=0, sticky=W)
        self.cboAddMaths = ttk.Combobox(TopFrame12b, font=('arial', 12, 'bold'), width=19,
                                           textvariable=self.AddMaths, state='readonly')
        self.cboAddMaths['value'] = ('No', 'Core Unit', 'Yes', 'Complete')
        self.cboAddMaths.current(0)
        self.cboAddMaths.grid(row=12, column=1)

        self.lblPhysics = Label(TopFrame12b, font=('arial', 12, 'bold'), text='Physics', bd=7,
                                    anchor='e')
        self.lblPhysics.grid(row=13, column=0, sticky=W)
        self.cboPhysics = ttk.Combobox(TopFrame12b, font=('arial', 12, 'bold'), width=19,
                                           textvariable=self.Physics, state='readonly')
        self.cboPhysics['value'] = ('No', 'Core Unit', 'Yes', 'Complete')
        self.cboPhysics.current(0)
        self.cboPhysics.grid(row=13, column=1)
        #======================================================================================================

        scroll_x = Scrollbar(TopFrame12a, orient=HORIZONTAL)
        scroll_y = Scrollbar(TopFrame12a, orient=VERTICAL)
        self.Student_Record = ttk.Treeview(TopFrame12a,height=22, columns=('studentid', 'firstname', 'surname', 'address',
        'postcode','gender','dob','mobile','email','parent'),xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.Student_Record.xview)
        scroll_y.config(command=self.Student_Record.yview)

        self.Student_Record.heading('studentid', text='Student ID')
        self.Student_Record.column('studentid', width=70)

        self.Student_Record.heading('firstname', text='Firstname')
        self.Student_Record.column('firstname', width=90)

        self.Student_Record.heading('surname', text='Surname')
        self.Student_Record.column('surname', width=90)

        self.Student_Record.heading('address', text='Address')
        self.Student_Record.column('address', width=200)

        self.Student_Record.heading('postcode', text='Post Code')
        self.Student_Record.column('postcode', width=70)

        self.Student_Record.heading('gender', text='Gender')
        self.Student_Record.column('gender', width=70)

        self.Student_Record.heading('dob', text='DOB')
        self.Student_Record.column('dob', width=70)

        self.Student_Record.heading('mobile', text='Mobile')
        self.Student_Record.column('mobile', width=70)

        self.Student_Record.heading('email', text='Email')
        self.Student_Record.column('email', width=90)

        self.Student_Record.heading('parent', text='Parent/Guid')
        self.Student_Record.column('parent', width=70)

        self.Student_Record['show'] = 'headings'
        self.Student_Record.pack(fill=BOTH, expand=1)

        self.Student_Record.bind("<ButtonRelease-1>",self.get_cursor)
        self.Display()


        #=====================================button Frame========================================
        self.btnAddNewStudent=Button(ButtonFrame,text='AddNew',padx=11,bd=4,font=('arial',16,'bold'),bg='cadetblue',
                                     width=5,command=self.AddData).grid(row=0,column=0,padx=1)
        self.btnUpdate = Button(ButtonFrame, text='Update', padx=11, bd=4, font=('arial', 16, 'bold'),
                                       bg='cadetblue',width=5,command=self.Update).grid(row=0, column=1, padx=1)
        self.btnDelete = Button(ButtonFrame, text='Delete', padx=11, bd=4, font=('arial', 16, 'bold'),
                                       bg='cadetblue',width=5,command=self.Deletedb).grid(row=0, column=2, padx=1)
        self.btnReset = Button(ButtonFrame, text='Reset', padx=11, bd=4, font=('arial', 16, 'bold'),
                                       bg='cadetblue',width=5,command=self.reset).grid(row=0, column=3, padx=1)
        self.btnResult = Button(ButtonFrame, text='Result', padx=11, bd=4, font=('arial', 16, 'bold'),
                                       bg='cadetblue',width=5,command=getSelectDate ).grid(row=0, column=4, padx=1)
        self.btnExit = Button(ButtonFrame, text='Exit', padx=11, bd=4, font=('arial', 16, 'bold'),
                                       bg='cadetblue',width=5,command=self.iExit).grid(row=0, column=5, padx=1)

        #===================================Function===================================================
    def iExit(self):
        iexit=messagebox.askyesno('Student Management System','Confirm if you want to exit')
        if iexit >0:
            root.destroy()
            return

    def reset(self):
        self.StudentID.set('')
        self.Firstname.set('')
        self.Surname.set('')
        self.Address.set('')
        self.PostCode.set('')
        self.Gender.set('')
        self.DOB.set('')
        self.Mobile.set('')
        self.Email.set('')

        self.ParentGuidance.set('')
        self.pgFirstname.set('')
        self.pgSurname.set('')
        self.pgAddress.set('')
        self.pgWorkPhone.set('')
        self.pgMobile.set('')
        self.pgEmail.set('')

        self.Course.set('Course Selector')
        self.CourseCode.set('')
        self.Faculty.set('')
        self.Dean.set('')
        self.Head_of_School.set('')
        self.ProgramLeader.set('')
        self.CourseTutor.set('')
        self.Building.set('')

        self.HomeStudent.set('No')
        self.Oversea.set('No')
        self.Accommodation.set('No')
        self.ExchangeProg.set('No')
        self.Scholarship.set('No')

        self.BA.set('0')
        self.BSc.set('0')
        self.MA.set('0')
        self.MSc.set('0')
        self.PhD.set('0')

        self.DataScience.set('')
        self.EventDrivenPro.set('')
        self.ObjectOriented.set('')
        self.Spreadsheet.set('')
        self.SystemAnalysis.set('')
        self.InformTechnology.set('')
        self.DigitalGraphics.set('')

        self.English.set('')
        self.Games.set('')
        self.Animation.set('')
        self.Database.set('')
        self.Maths.set('')
        self.AddMaths.set('')
        self.Physics.set('')
        self.Media.set('')
        self.GraphicD.set('')


        self.Module1.set('')
        self.Module2.set('')
        self.Module3.set('')
        self.Module4.set('')
        self.Module5.set('')
        self.Module6.set('')
        self.Module7.set('')
        self.Module8.set('')
        self.Ranking.set('')
        self.ToatalScore.set('')
        self.ResultDate.set('')

        self.Subject1.set('')
        self.Subject2.set('')
        self.Subject3.set('')
        self.Subject4.set('')
        self.Subject5.set('')
        self.Subject6.set('')
        self.Subject7.set('')
        self.Subject8.set('')

    def setSubject(self,event):
        if self.Subject1.get()=='Event Driven Prog':
            self.txt1.config(state=NORMAL)
            self.txt1.focus_set()
            self.EventDrivenPro.set('Core Unit')
        elif self.Subject1.get() == '':
            self.txt1.config(state=DISABLED)
            self.Module1.set('')
            self.EventDrivenPro.set('No')

        if self.Subject2.get()=='Object Oriented' :
            self.txt2.config(state=NORMAL)
            self.txt2.focus_set()
            self.ObjectOriented.set('Completed')
            self.Spreadsheet.set('No')
        if self.Subject2.get()=='Spreadsheet' :
            self.txt2.config(state=NORMAL)
            self.txt2.focus_set()
            self.Spreadsheet.set('Core Unit')
            self.ObjectOriented.set('No')
        elif self.Subject2.get() == '':
            self.txt2.config(state=DISABLED)
            self.Module2.set('')
            self.ObjectOriented.set('No')
            self.Spreadsheet.set('No')

        if self.Subject3.get()=='System Analysis' :
            self.txt3.config(state=NORMAL)
            self.txt3.focus_set()
            self.SystemAnalysis.set('Core Unit')
            self.InformTechnology.set('No')
        if self.Subject3.get()=='Inform Technology' :
            self.txt3.config(state=NORMAL)
            self.txt3.focus_set()
            self.InformTechnology.set('Core Unit')
            self.SystemAnalysis.set('No')
        elif self.Subject3.get() == '':
            self.txt3.config(state=DISABLED)
            self.Module3.set('')
            self.SystemAnalysis.set('No')
            self.InformTechnology.set('No')

        if self.Subject4.get()=='Digital Graphics' :
            self.txt4.config(state=NORMAL)
            self.txt4.focus_set()
            self.DigitalGraphics.set('Complete')
            self.English.set('No')
        if self.Subject4.get()=='English':
            self.txt4.config(state=NORMAL)
            self.txt4.focus_set()
            self.English.set('Core Unit')
            self.DigitalGraphics.set('No')
        elif self.Subject4.get() == '':
            self.txt4.config(state=DISABLED)
            self.Module4.set('')
            self.DigitalGraphics.set('No')
            self.English.set('No')

        if self.Subject5.get()=='Games' :
            self.txt5.config(state=NORMAL)
            self.txt5.focus_set()
            self.Games.set('Complete')
            self.Animation.set('No')
        if self.Subject5.get()=='Animation':
            self.txt5.config(state=NORMAL)
            self.txt5.focus_set()
            self.Animation.set('Complete')
            self.Games.set('No')
        elif self.Subject5.get() == '':
            self.txt5.config(state=DISABLED)
            self.Module5.set('')
            self.Animation.set('No')
            self.Games.set('No')

        if self.Subject6.get()=='Database' :
            self.txt6.config(state=NORMAL)
            self.txt6.focus_set()
            self.Database.set('Complete')
            self.Maths.set('No')
        if self.Subject6.get()=='Maths':
            self.txt6.config(state=NORMAL)
            self.txt6.focus_set()
            self.Maths.set('Core Unit')
            self.Database.set('No')
        elif self.Subject6.get() == '':
            self.txt6.config(state=DISABLED)
            self.Module6.set('')
            self.Database.set('No')
            self.Maths.set('No')

        if self.Subject7.get()=='AddMaths' :
            self.txt7.config(state=NORMAL)
            self.txt7.focus_set()
            self.AddMaths.set('Complete')
            self.Physics.set('No')
        if self.Subject7.get()=='Physics':
            self.txt7.config(state=NORMAL)
            self.txt7.focus_set()
            self.Physics.set('Core Unit')
            self.AddMaths.set('No')
        elif self.Subject7.get() == '':
            self.txt7.config(state=DISABLED)
            self.Module7.set('')
            self.Physics.set('No')
            self.AddMaths.set('No')

        if self.Subject8.get()=='Data Science' :
            self.txt8.config(state=NORMAL)
            self.txt8.focus_set()
            self.DataScience.set('Core Unit')
        elif self.Subject8.get() == '':
            self.txt8.config(state=DISABLED)
            self.Module8.set('')
            self.DataScience.set('No')

    def CourseData(self,event):
        if self.Course.get()=='Bsc Serious Game':
            self.CourseCode.set("BSC234A")
            self.Faculty.set('The School of Computer Science')
            self.Dean.set("Dr Ashiq Hussain")
            self.Head_of_School.set("Jan Muhammad Kerio")
            self.ProgramLeader.set('prof.Asjad')
            self.CourseTutor.set('Dr Shafique')
            self.Building.set('Engineering Building')

        if self.Course.get()=='BSc Computer Science':
            self.CourseCode.set("BSC235B")
            self.Faculty.set('The School of Computer Science')
            self.Dean.set("Dr Ashfaq")
            self.Head_of_School.set("Dr Amjad")
            self.ProgramLeader.set('prof.Asjad')
            self.CourseTutor.set('Dr Nouman')
            self.Building.set('Science Building')

        if self.Course.get()=='BA Animation':
            self.CourseCode.set("BSC4566B")
            self.Faculty.set('The School of Computer Science')
            self.Dean.set("Dr Ali")
            self.Head_of_School.set("Dr Amjad")
            self.ProgramLeader.set('prof. Abid')
            self.CourseTutor.set('Dr Nouman')
            self.Building.set('Computer Science')

        if self.Course.get() == 'BSc Information System':
            self.CourseCode.set("BSC46B")
            self.Faculty.set('The School of Computer Science')
            self.Dean.set("Dr Sami")
            self.Head_of_School.set("Dr Hassan")
            self.ProgramLeader.set('prof. Usman')
            self.CourseTutor.set('Dr Shafqat')
            self.Building.set('Computer Science')

        if self.Course.get() == 'BSc Computing':
            self.CourseCode.set("BSC45986B")
            self.Faculty.set('The School of Computer Science')
            self.Dean.set("Dr Sarfraz")
            self.Head_of_School.set("Dr Arslan")
            self.ProgramLeader.set('prof. Waseem')
            self.CourseTutor.set('Dr Shafqat')
            self.Building.set('Computer Science')

        if self.Course.get() == 'BSc Computer Game':
            self.CourseCode.set("BSC4591B")
            self.Faculty.set('The School of Computer Science')
            self.Dean.set("Dr Nouman")
            self.Head_of_School.set("Dr Sarfraz")
            self.ProgramLeader.set('prof. Nawaz')
            self.CourseTutor.set('Dr Asif')
            self.Building.set('Computer Science')

        if self.Course.get() == 'BSc Computer Animation':
            self.CourseCode.set("BSC4821A")
            self.Faculty.set('The School of Computer Science')
            self.Dean.set("Dr Anjum")
            self.Head_of_School.set("Dr Khadim")
            self.ProgramLeader.set('prof. Nawaz')
            self.CourseTutor.set('Dr Ali')
            self.Building.set('Computer Science')

    def AddModulescore(self):

        if self.Module1.get()=="":
            self.Module1.set("0")
        if self.Module2.get()=="":
            self.Module2.set("0")
        if self.Module3.get()=="":
            self.Module3.set("0")
        if self.Module4.get()=="":
            self.Module4.set("0")
        if self.Module5.get()=="":
            self.Module5.set("0")
        if self.Module6.get()=="":
            self.Module6.set("0")
        if self.Module7.get()=="":
            self.Module7.set("0")
        if self.Module8.get()=="":
            self.Module8.set("0")

        Unit1 = float(self.Module1.get())
        Unit2 = float(self.Module2.get())
        Unit3 = float(self.Module3.get())
        Unit4 = float(self.Module4.get())
        Unit5 = float(self.Module5.get())
        Unit6 = float(self.Module6.get())
        Unit7 = float(self.Module7.get())
        Unit8 = float(self.Module8.get())

        UnitTotal = ( Unit1 + Unit2 + Unit3 + Unit4 + Unit5 + Unit6 + Unit7 + Unit8 )
        self.TotalScore.set(int(UnitTotal))

        if UnitTotal >= 700:
            self.Ranking.set('1St Class')
        elif UnitTotal >= 600:
            self.Ranking.set('2.i Upper')
        elif UnitTotal >= 500:
            self.Ranking.set('2.ii Lower')
        elif UnitTotal >= 400:
            self.Ranking.set('3rd Class')
        elif UnitTotal >= 300:
            self.Ranking.set('CoHE')
        elif UnitTotal <= 300:
            self.Ranking.set('Fail')

    def AddData(self):
        if self.StudentID.get() == "" or self.Firstname.get() == "" or self.Surname.get() == "":
            messagebox.showerror("Error", "Enter Correct Member Details")
        else:
            con = pymysql.connect(host="localhost", user="root", password='123@abc',port=3306, database='studentranking')
            cur = con.cursor()
            cur.execute("insert into studentranking values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
            (
                self.StudentID.get(),
                self.Firstname.get(),
                self.Surname.get(),
                self.Address.get(),
                self.PostCode.get(),
                self.Gender.get(),
                self.DOB.get(),
                self.Mobile.get(),
                self.Email.get(),

                self.ParentGuidance.get(),
                self.pgFirstname.get(),
                self.pgSurname.get(),
                self.pgAddress.get(),
                self.pgWorkPhone.get(),
                self.pgMobile.get(),
                self.pgEmail.get(),
                self.Course.get(),
                self.CourseCode.get(),
                self.Faculty.get(),
                self.Dean.get(),
                self.Head_of_School.get(),
                self.ProgramLeader.get(),
                self.CourseTutor.get(),
                self.Building.get(),

                self.HomeStudent.get(),
                self.Oversea.get(),
                self.Accommodation.get(),
                self.ExchangeProg.get(),
                self.Scholarship.get(),

                self.BA.get(),
                self.BSc.get(),
                self.MA.get(),
                self.MSc.get(),
                self.PhD.get(),

                self.DataScience.get(),
                self.EventDrivenPro.get(),
                self.ObjectOriented.get(),
                self.Spreadsheet.get(),
                self.SystemAnalysis.get(),
                self.InformTechnology.get(),
                self.DigitalGraphics.get(),
                self.English.get(),
                self.Games.get(),
                self.Animation.get(),
                self.Database.get(),
                self.Maths.get(),
                self.AddMaths.get(),
                self.Physics.get(),

                self.Module1.get(),
                self.Module2.get(),
                self.Module3.get(),
                self.Module4.get(),
                self.Module5.get(),
                self.Module6.get(),
                self.Module7.get(),
                self.Module8.get(),

                self.TotalScore.get(),
                self.Ranking.get(),
                self.ResultDate.get(),
            ))
            con.commit()
            con.close()
            messagebox.showinfo("Successful", "Record Entered Successfully")
            self.Display()
            self.reset()

    def Update(self):
        if self.StudentID.get() == "" or self.Firstname.get() == "" or self.Surname.get() == "":
            messagebox.showerror("Error", "Enter Correct Member Details")
        else:
            con = pymysql.connect(host="localhost", user="root", password='123@abc',port=3306, database='studentranking')
            cur = con.cursor()
            cur.execute("update studentranking set firstname=%s,surname=%s,address=%s,postcode=%s,gender=%s,dob=%s,mobile=%s,email=%s,parent=%s,pfirstname=%s,psurname=%s,paddress=%s,pphone=%s,pmobile=%s,pemail=%s,course=%s,coursecode=%s,faculty=%s,deanoffac=%s,hos=%s,proleader=%s,coursetutor=%s,building=%s,homestd=%s,overseastd=%s,accommodation=%s,exchange=%s,scholarship=%s,ba=%s,bsc=%s,ma=%s,msc=%s,phd=%s,datasci=%s,eventdriprog=%s,objectori=%s,spreadsheet=%s,sysanalysis=%s,infotech=%s,digitalgrap=%s,english=%s,games=%s,animation=%s,datab=%s,maths=%s,addmaths=%s,physics=%s,module1=%s,module2=%s,module3=%s,module4=%s,module5=%s,module6=%s,module7=%s,module8=%s,totalscore=%s,ranking=%s,dateofrank=%s where studentid=%s",(self.Firstname.get(),self.Surname.get(),self.Address.get(),self.PostCode.get(),self.Gender.get(),self.DOB.get(),self.Mobile.get(),self.Email.get(),self.ParentGuidance.get(),self.pgFirstname.get(),self.pgSurname.get(),self.pgAddress.get(),self.pgWorkPhone.get(),self.pgMobile.get(),self.pgEmail.get(),self.Course.get(),self.CourseCode.get(),self.Faculty.get(),self.Dean.get(),self.Head_of_School.get(),self.ProgramLeader.get(),self.CourseCode.get(),self.Building.get(),self.HomeStudent.get(),self.Oversea.get(),self.Accommodation.get(),self.ExchangeProg.get(),self.Scholarship.get(),self.BA.get(),self.BSc.get(),self.MA.get(),self.MSc.get(),self.PhD.get(),self.DataScience.get(), self.EventDrivenPro.get(), self.ObjectOriented.get(), self.Spreadsheet.get(),self.SystemAnalysis.get(),self.InformTechnology.get(),self.DigitalGraphics.get(),self.English.get(),self.Games.get(),self.Animation.get(),self.Database.get(),self.Maths.get(),self.AddMaths.get(),self.Physics.get(),self.Module1.get(),self.Module2.get(),self.Module3.get(),self.Module4.get(),self.Module5.get(),self.Module6.get(),self.Module7.get(),self.Module8.get(),self.TotalScore.get(),self.Ranking.get(),self.ResultDate.get(),self.StudentID.get()))
            con.commit()
            con.close()
            messagebox.showinfo("Successful", "Record Updated Successfully")
            self.Display()
            self.reset()

    def Deletedb(self):

        con = pymysql.connect(host="localhost", user="root", password='123@abc',port=3306, database='studentranking')
        cur = con.cursor()
        cur.execute("delete from studentranking where studentid =%s",self.StudentID.get())
        con.commit()
        con.close()
        messagebox.showinfo("Successful", "Record Deleted Successfully")
        self.Display()
        self.reset()

    def Display(self):
        con = pymysql.connect(host="localhost", user="root", password="123@abc",port=3306, database="studentranking")
        cur = con.cursor()
        cur.execute("select * from studentranking")
        rows = cur.fetchall()
        if len(rows) != 0:
            self.Student_Record.delete(*self.Student_Record.get_children())
            for row in rows:
                self.Student_Record.insert('', END, values=row)
            con.commit()
        con.close()

    def get_cursor(self,event):
        cursor_row = self.Student_Record.focus()
        contants = self.Student_Record.item(cursor_row)
        row = contants['values']

        self.StudentID.set(row[0]),
        self.Firstname.set(row[1]),
        self.Surname.set(row[2]),
        self.Address.set(row[3]),
        self.PostCode.set(row[4]),
        self.Gender.set(row[5]),
        self.DOB.set(row[6]),
        self.Mobile.set(row[7]),
        self.Email.set(row[8]),

        self.ParentGuidance.set(row[9]),
        self.pgFirstname.set(row[10]),
        self.pgSurname.set(row[11]),
        self.pgAddress.set(row[12]),
        self.pgWorkPhone.set(row[13]),
        self.pgMobile.set(row[14]),
        self.pgEmail.set(row[15]),
        self.Course.set(row[16]),
        self.CourseCode.set(row[17]),
        self.Faculty.set(row[18]),
        self.Dean.set(row[19]),
        self.Head_of_School.set(row[20]),
        self.ProgramLeader.set(row[21]),
        self.CourseTutor.set(row[22]),
        self.Building.set(row[23]),

        self.HomeStudent.set(row[24]),
        self.Oversea.set(row[25]),
        self.Accommodation.set(row[26]),
        self.ExchangeProg.set(row[27]),
        self.Scholarship.set(row[28]),

        self.BA.set(row[29]),
        self.BSc.set(row[30]),
        self.MA.set(row[31]),
        self.MSc.set(row[32]),
        self.PhD.set(row[33]),

        self.DataScience.set(row[34]),
        self.EventDrivenPro.set(row[35]),
        self.ObjectOriented.set(row[36]),
        self.Spreadsheet.set(row[37]),
        self.SystemAnalysis.set(row[38]),
        self.InformTechnology.set(row[39]),
        self.DigitalGraphics.set(row[40]),
        self.English.set(row[41]),
        self.Games.set(row[42]),
        self.Animation.set(row[43]),
        self.Database.set(row[44]),
        self.Maths.set(row[45]),
        self.AddMaths.set(row[46]),
        self.Physics.set(row[47]),

        self.Module1.set(row[48]),
        self.Module2.set(row[49]),
        self.Module3.set(row[50]),
        self.Module4.set(row[51]),
        self.Module5.set(row[52]),
        self.Module6.set(row[53]),
        self.Module7.set(row[54]),
        self.Module8.set(row[55]),

        self.TotalScore.set(row[56]),
        self.Ranking.set(row[57]),
        self.ResultDate.set(row[58])

if __name__ == '__main__':
    root=Tk()
    application=studentRecords(root)
    root.mainloop()