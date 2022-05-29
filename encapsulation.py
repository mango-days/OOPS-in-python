# encapsulation

class Human :
    def __init__ ( general , name , age , gender ) :
        general.name = name
        general.gender = gender
        general.age = age
    
    def showGeneral ( general ) :
        print ( general.name , general.gender , general.age )
        
        

class Humanity ( Human ) :
    def __init__ ( feelingsOf , name , age , gender ) :
        feelingsOf.self = Human ( name , age , gender )
        feelingsOf.self.gender = "F"
        feelingsOf.age = 28
        feelingsOf.love = True
        feelingsOf.happiness = True
        feelingsOf.content = True
        feelingsOf.wholeness = True
    
    def personalityTraits ( feelingsOf ) :
        print ( "Hi! I am" , feelingsOf.self.name ,"!" )
        print ( "I am a", feelingsOf.self.gender , "in the body of a man." , "I am :")
        if feelingsOf.love == True : print ("full of love")
        if feelingsOf.happiness == True : print ( "happy with my life" )
        if feelingsOf.content == True : print ( "content" )
        if feelingsOf.wholeness == True : print ( "whole" )
        print ( "and no one can take that away from me." )
        print ( "#smile ! ! !" )
        print (" ")
        print ( "I am", feelingsOf.self.age, "years old but I dont feel a day over" , feelingsOf.age , "!!!" )
        
Person = Humanity ( "Micheal" , 54 , "M" )
Person.personalityTraits ()
