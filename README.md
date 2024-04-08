# comsc330

Our goal is to develop a system that will do some basic grade analysis. 

Intent:
 - find the GPA of a section
 - combined GPA of all sections in a group
 - compare each section GPA against group GPA to determine if there is a signficant difference between   the two.

Requirements: 
- Program needs to be self contained

**Coding Assignments**
- Using Python:

- Read in files - Han 
 - Make class that  takes each section and stores it into a 2D array
 - First row of array will be section information
 - i.e.
		[[section information]
  [last name, first name, student ID, letter grade]
  [last name, first name, student ID, letter grade]
  …
  [last name, first name, student ID, letter grade]]
 - Each successive row will be each students data
 - Each 2D array will be stored in a node in a linked list
- Linked list storage - Liam 
- Group organization - Nate 
 - Create a class to search through each section using the linked list to find GPA information, etc.
- Run organization -Liam
 - Create a class to run several iterations of the group files
 - Compare each groups data against each other
- Math - Maria
 - Create a class to calculate z value and GPA conversion
 - Implement a way to keep track of students with more than one A,A- and more than one D+,D,D-,F
