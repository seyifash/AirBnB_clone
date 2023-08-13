# ﻿AIRBNB CLONE - The Console 
Description of the command interpreter
The console is the first part of the AirBnB clone project. It is the first step towards building your first full web application: the AirBnB clone

### DESCRIPTION OF THE COMMAND INTEPRETER 
- Create a new object (ex: a new User or a new Place)
- Retrieve an object from a file, a database etc…
- Do operations on objects (count, compute stats, etc…)
- Update attributes of an object
- Destroy an object  

### HOW TO USE IT
- Clone this repository: git clone "https://github.com/Osei365/AirBnB_clone.git"
- Access AirBnb directory: cd AirBnB_clone
- Run hbnb(interactively): ./console and enter command
- Run hbnb(non-interactively): echo "<command>" | ./console.py

### File Descriptions  
console.py - the console contains the entry point of the command interpreter. List of commands this console current supports:

- EOF - exits console
- quit - exits console
- <emptyline> - overwrites default emptyline method and does nothing
- create - Creates a new instance ofBaseModel, saves it (to the JSON file) and prints the id
- destroy - Deletes an instance based on the class name and id (save the change into the JSON file).
- show - Prints the string representation of an instance based on the class name and id.
- all - Prints all string representation of all instances based or not on the class name.
- update - Updates an instance based on the class name and id by adding or updating attribute (save the change into the JSON file).
