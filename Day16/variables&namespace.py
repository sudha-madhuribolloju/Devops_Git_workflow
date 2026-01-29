#Variable Scopes & Namespace (Local and Global)
#global variable
total_marks =200
def report_total():
    global total_marks
    total_marks = total_marks+50
    print(f'total_marks: {total_marks}')
report_total()
#Local variable
def update_total():
    total_marks=100
    print(f'total_marks: {total_marks}')
update_total()
#global
y=10
print(y)
#local
def total():
    y=20
    print(y)
total()
print(y)
