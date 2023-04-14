
def sum(*numbers):
    answer=0
    for number in numbers:
     answer +=number
     
    return answer

# write a function that accepts any number of intergers
# and return the result of multiply all of them
def mult(*numbers):
    answer=1
    for number in numbers:
        answer*=number
        
    return answer
    
def student_attribute(**kwargs):
    for key,value in kwargs.items():
        print(f"{key}:{value}")    
        
def my_country(country="Burundi"):
          print(f"Hello from {country}")
          
          
        #   Assignment
   
 #No 1    
# A function named concatenate_args that takes any number 
# of string arguments in positional arguments format 
# and concatenates them into a single string
def concatenate_args(*strings):
    result=(" ")
    for string in strings:
     result+=string
    
    return result

# A function named concatenate_kwargs that takes any number of string arguments 
# in keyword arguments  format and concatenates them into a single string
def concatenate_kwargs(**words):
    answer=(" ")
    for key,value in words.items():
        answer+=(f"{key,value}")
    return answer
   