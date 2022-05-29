{\rtf1\ansi\ansicpg1252\cocoartf2636
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\paperw11900\paperh16840\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\pard\tx566\tx1133\tx1700\tx2267\tx2834\tx3401\tx3968\tx4535\tx5102\tx5669\tx6236\tx6803\pardirnatural\partightenfactor0

\f0\fs24 \cf0 # Polymorphism\
class Human :\
    def __init__ ( general , name , age , gender ) :\
        general.name = name\
        general.gender = gender\
        general.age = age\
    \
    def showGeneral ( general ) :\
        print ( general.name , general.gender , general.age )\
\
\
class SchoolStudent ( Human ):\
    def __init__ ( records , name , age , gender , courses ) :\
        records.student = Human ( name , age , gender )\
        records.courses = courses\
\
    def showRecords ( records ) :\
        print ( records.student.showGeneral() , records.courses )\
\
\
class CollegeStudent ( SchoolStudent , Human ):\
    def __init__ ( records , name , age , gender , courses ) :\
        records.student = Human ( name , age , gender )\
        records.courses = courses\
\
    def showRecords ( records ) :\
        print ( records.student.showGeneral() , records.courses )\
    \
    \
class Employee ( CollegeStudent , Human ):\
    def __init__ ( records , name , age , gender , empNo , c_courses , s_courses) :\
        records.general = Human ( name , age , gender )\
        records.empNo = empNo\
        records.c_records = CollegeStudent ( name , age , gender , c_courses )\
        records.c_courses = records.c_records.courses\
        records.s_records = SchoolStudent ( name , age , gender , s_courses )\
        records.s_courses = records.s_records.courses\
        records.courses = [ "Onboarding courses" , records.c_courses , s_courses ]\
    \
    def showRecords ( records ) :\
        records.general.showGeneral()\
        print ( records.empNo , records.courses )\
    \
    def IdentityCheck ( records ) :\
        if records.general.name == records.c_records.student.name and records.general.name == records.s_records.student.name : print ("Identity confirmed")\
        else : print ( "Records do not match !!!!" )\
        \
Obj = Employee ( "Jasmine Kaur" , 23 , "F" , 22409 , "Computer Science" , "Mathematics" )\
Obj.showRecords()\
Obj.IdentityCheck()}