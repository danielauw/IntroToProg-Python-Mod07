<h1 align="center">
  Error Handling & Pickling
</h1>

DUW  
May 31, 2022  
Foundations of Programming, Python  
Assignment 07  
GitHUB: https://github.com/danielauw/IntroToProg-Python-Mod07   


## Introduction
In this assignment I will explain step-by-step how I created a script that saves to a binary file and how I defined a few examples of error handling. Assignment 07 is meant to prove understanding of the Python pickling concept and error handling situations. Key sources I used to learn more about pickling and error handling: 
-	Pickle – Python object serialization (Python docs) 
-	Errors and Exceptions (Python docs)
-	edX class Introduction to Programming Using Python  

## Creating the Program
The steps I followed to develop and run the program:  
#### 1.	Created a new script file with the .py extension
#### 2.	Updated the script header including inline comments in the script file 
a.	Updated the change log (who, when, what). 
#### 3.	Added some error handling examples:   
a.	IO Error: file does not exist using the syntax try-except-else:   
      &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- I added code for the program to open and read a file that does not exist.   
      &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- I added the exception for the input/output error and included that the program should print that it could not find the file if it doesn’t find it.   
      &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- I added an ‘else’ statement that the program should read the file if it finds it.   
b.	Zero division error and value error showcasing how to use multiple except statements:   
      &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- Added a while loop so that the program continues running until the user adds the right input   
      &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- Added an input statement asking the user to enter a number other than zero.   
      &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- Converted the user input into a float  
      &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- Added a new variable p that is calculated based on the user’s input.   
      &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- Introduced the Zero division error and told the program to print an error message if the user inputs 0.   
      &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-	Introduced the Value Error if the user provides something else than a number like a text response.   
      &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-	Added an ‘else’ statement to print the value of the number calculated based on user input.   
      &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-	Added a ‘break’ to break the while loop at this point.   
      &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-	Added a ‘finally’ statement to print ‘Done’ when the program ends.   
c.	**Figure 1** shows my code with the error handling examples.   

![Exception Handling Python Code](https://github.com/danielauw/IntroToProg-Python-Mod07/blob/main/docs/Figure1.PNG "Exception Handling Python Code")




#### 4.	Demonstrated the pickling concept by saving to a binary file.   
a.	Imported the pickle  
b.	Defined my variables   
c.	Processed the data by defining my functions to save data to the file and then to read data from the file.   
d.	Added code for the presentation section:   
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-	Added two input statements to collect data from the user  
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-	Stored the input into a list  
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- Stored the list into a binary file by opening the file in writing ‘wb’ mode and using the ‘pickle.dump’ expression. Closed the file.   
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-	Read the file into a new list and displayed the content. Opened the file and used the ‘pickle.load’ expression to read the file. Closed the file.   
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-	Added a print statement to print the data in the file.   
e.	**Figure 2** shows my code with the pickling script.   

![Exception Handling Python Code](https://github.com/danielauw/IntroToProg-Python-Mod07/blob/main/docs/Figure5.PNG "Exception Handling Python Code")

#### 5.	Ran the program through CMD   
a.	Opened CMD and added the path file for “Assignment05”   
b.	**Figure 3** shows the output in CMD   

![Exception Handling Python Code](https://github.com/danielauw/IntroToProg-Python-Mod07/blob/main/docs/Figure3.PNG "Exception Handling Python Code")


#### 6.	Opened the binary file in a text editor  
a.	Located the text file and opened it to verify that it displays the user input  
b.	**Figure 4** shows the output in the text editor   


![Exception Handling Python Code](https://github.com/danielauw/IntroToProg-Python-Mod07/blob/main/docs/Figure4.PNG "Exception Handling Python Code")

## Summary
Creating and running Assignment 07 allowed me to work with error handling types and saving the file into a binary format. 


