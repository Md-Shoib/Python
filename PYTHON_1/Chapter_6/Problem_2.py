# WAP to find out wheather a students has passed the exam or failed exam taking user input but total marks > 40 and each subject > 33 
mark_1 = int(input("Enter the marks of Math:"))
mark_2 = int(input("Enter the marks of Computer:"))
mark_3 = int(input("Enter the marks of Science:"))

total_marks = ((mark_1 + mark_2 + mark_3)/300)*100
# Conditional 
if(total_marks>40 and mark_1>=32 and mark_2>=32 and mark_3>=32  ):
    print("He passed the exam", total_marks)
    
else:
    print("You failed in exam")
    
         
        
        
    
    
