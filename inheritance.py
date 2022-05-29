# inheritance

class Human :
    def __init__ ( general , name , age , gender ) :
        general.name = name
        general.gender = gender
        general.age = age
    
    def showGeneral ( general ) :
        print ( general.name , general.gender , general.age )
    
class Student ( Human ):
    def __init__ ( records , name , age , gender , standard , rollNo ) :
        records.student = Human ( name , age , gender )
        records.standard = standard 
        records.rollNo = rollNo
    
    def showRecords ( records ) :
        print ( records.student.showGeneral() , records.standard , records.rollNo )
    
Obj = Student ( "Jasmine Kaur" , "F" , 23 , 15 , 22409 )
Obj.showRecords()
