# --------------------------------------------#
#Title: Error Handling
#ChangeLog: (Who, When, What)
#DUW, 5/31/2022, Created script
# --------------------------------------------#

# IO Error - file does not exist
try:
    File=open('MyDatabase.txt', 'r')
except IOError:
    print ("Could not find the file")
else:
    data=File.read()
    print(data)
    File.close()

# ZeroDivisionError, ValueError
while True:
    user_response=input('Please enter a number other than zero:')
    try:
        y=float(user_response)
        p=10/y
    except (ZeroDivisionError):
        print ('Cannot be divided by 0!')
    except (ValueError):
        print ('Input needs to be a number!')
    else:
        print ('The value of p is', p)
        break
    finally:
        print ('Done')

# --------------------------------------------#
#Title: Pickling
#ChangeLog: (Who, When, What)
#DUW, 5/31/2022, Created script
# --------------------------------------------#
import pickle
# Data -------------------------------------------- #
file_name= 'MyTasks.dat'
to_do_list = []

# Processing -------------------------------------- #
def save_data_to_file(file_name, list_of_data):
    file_name=open('MyTasks.dat', 'w')
    for row in to_do_list:
        file_name.write(str(row('Priority'))+str(row('Task')))
    file_name.close()

def read_data_from_file(file_name):
    file_name=open('MyTasks.dat', 'r')
    for row in to_do_list:
        file_name.read(str(row('Priority'))+str(row('Task')))
    file_name.close()

# Presentation ------------------------------------ #
# Getting user input, then store it in a list object
Priority=int(input('Priority:'))
Task=str(input ('Task:'))
to_do_list=[Priority, Task]
# Storing the list object into a binary file
file_name=open('MyTasks.dat', 'wb')
pickle.dump(to_do_list, file_name)
file_name.close()

# Reading the data from the file into a new list object and display the contents
file_name=open('MyTasks.dat', 'rb')
file_name_data=pickle.load(file_name)
file_name.close()

print(file_name_data)