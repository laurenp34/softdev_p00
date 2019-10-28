# Storytelling by noobpedia

**Roster/Roles**
- Raymond Lee
	- Viewing stories
		- Only show latest update and author when adding to a story
		- Disable ability to edit if a user has already written to a story
  - Adding to a story
		- Word limit
		- Log the fact that a user edited this
		- Add story to user's landing page
  - If time allows: a searching mechanism using edit distance that compares the search value with every existing title and orders them from least to greatest distance.

- Kevin Li
	- Implementing routes
		- Getting and processing form data
		- Login/registration process
		- Link pages to one another via hyperlinks and whatnot
		- Flashing necessary messages
	- Parse data from SQLite database in a usable for the app.py file
	- Handling sessions and the logic invovled for the landing page after login


- Emory Walsh -- Project Manager
	- Designing the database
		- Create each table
		-	Creating modules that add to
  	- Accessing information from each database table

## Instructions for running this project

**Dependencies**

You must install the Python module called "flask". If you don't, install it in a Terminal with:
```bash
pip3 install flask
```
Note that on certain systems (like the school computers), the pip3 command may be restricted. To get around this, create a virtual environment with:
```bash
python3 -m venv <name_of_venv>
```
*Note that if your system only has Python 3 installed, just remove the 3 from the above command.*

To activate the virtual environment, cd into the directory you created the environment in, and run the "activate" file. Now, you should be able to pip3 install and run Python files that utilize modules installed via pip3. To deactivate the environment, run the "deactivate" file.  

**Run the program**

After procuring the ability to run flask module commands, all you need to do to run the program is to type into a Terminal: 
```bash
python3 app.py
```
*Again, remove the 3 after the "python" if necessary.*
