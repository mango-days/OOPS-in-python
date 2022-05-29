{\rtf1\ansi\ansicpg1252\cocoartf2636
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\paperw11900\paperh16840\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\pard\tx566\tx1133\tx1700\tx2267\tx2834\tx3401\tx3968\tx4535\tx5102\tx5669\tx6236\tx6803\pardirnatural\partightenfactor0

\f0\fs24 \cf0 # encapsulation\
\
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
        \
class Humanity ( Human ) :\
    def __init__ ( feelingsOf , name , age , gender ) :\
        feelingsOf.self = Human ( name , age , gender )\
        feelingsOf.self.gender = "F"\
        feelingsOf.age = 28\
        feelingsOf.love = True\
        feelingsOf.happiness = True\
        feelingsOf.content = True\
        feelingsOf.wholeness = True\
    \
    def personalityTraits ( feelingsOf ) :\
        print ( "Hi! I am" , feelingsOf.self.name ,"!" )\
        print ( "I am a", feelingsOf.self.gender , "in the body of a man." , "I am :")\
        if feelingsOf.love == True : print ("full of love")\
        if feelingsOf.happiness == True : print ( "happy with my life" )\
        if feelingsOf.content == True : print ( "content" )\
        if feelingsOf.wholeness == True : print ( "whole" )\
        print ( "and no one can take that away from me." )\
        print ( "#smile ! ! !" )\
        print (" ")\
        print ( "I am", feelingsOf.self.age, "years old but I dont feel a day over" , feelingsOf.age , "!!!" )\
        \
Person = Humanity ( "Micheal" , 54 , "M" )\
Person.personalityTraits ()\
}