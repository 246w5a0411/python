#Nested if: A if within a if is called nested if
"""
syntax: ifcondition:
            outer if statements
            if condition:
                inner if statements
            else:
                inner else statements
        else:
            outer else statements
"""
#write a program for weather indication and advices
is_snowing=True
temp=int(input("enter a temperature"))
if is_snowing>10:
    print("please carry umbrella")     
    if is_snowing==-10:
       print("please carry umbrella and jacket")
    else:
        print("enjoy the sunny day")
else:
    print("the condition is false")
