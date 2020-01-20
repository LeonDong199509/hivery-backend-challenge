# Paranuara Challenge
Paranuara is a class-m planet. Those types of planets can support human life, for that reason the president of the Checktoporov decides to send some people to colonise this new planet and
reduce the number of people in their own country. After 10 years, the new president wants to know how the new colony is growing, and wants some information about his citizens. Hence he hired you to build a rest API to provide the desired information.

The government from Paranuara will provide you two json files (located at resource folder) which will provide information about all the citizens in Paranuara (name, age, friends list, fruits and vegetables they like to eat...) and all founded companies on that planet.
Unfortunately, the systems are not that evolved yet, thus you need to clean and organise the data before use.
For example, instead of providing a list of fruits and vegetables their citizens like, they are providing a list of favourite food, and you will need to split that list (please, check below the options for fruits and vegetables).

## New Features
Your API must provides these end points:
- Given a company, the API needs to return all their employees. Provide the appropriate solution if the company does not have any employees.
- Given 2 people, provide their information (Name, Age, Address, phone) and the list of their friends in common which have brown eyes and are still alive.
- Given 1 people, provide a list of fruits and vegetables they like. This endpoint must respect this interface for the output: `{"username": "Ahi", "age": "30", "fruits": ["banana", "apple"], "vegetables": ["beetroot", "lettuce"]}`
api/companies/id/employees
api/commons/
post () 


api/people/id/fruit_veges



## Delivery
To deliver your system, you need to send the link on GitHub. Your solution must provide tasks to install dependencies, build the system and run. Solutions that does not fit this criteria **will not be accepted** as a solution. Assume that we have already installed in our environment Java, Ruby, Node.js, Python, MySQL, MongoDB and Redis; any other technologies required must be installed in the install dependencies task. Moreover well tested and designed systems are one of the main criteria of this assessement 

## Evaluation criteria
- Solutions written in Python would be preferred.
- Installation instructions that work.
- During installation, we may use different companies.json or people.json files.
- The API must work.
- Tests

Feel free to reach to your point of contact for clarification if you have any questions.



Pros:

Using exception handling

Good models

Documented code

Usage of serialisers

Locking transactions per request

 

Cons:

Garbage in repo (___pychache__, venv)

Garbage in the repository (sqllite3 db, __pycache__)

Incorrect use of Django commands during setup

Commented code everywhere

Imports inside function

Mixed data in the same response variables (e.g. index)

No request parameters validation or sanitisation

Single endpoint for multiple purposes, overall very hard to understand the logic of majority of the functions, too many if statements and code branches

All logic inside views, no structure

Big try/except blocks

Building json response manually (no serializers)

Not using proper response codes

Overcomplicated logic

A lot of O(n^2) complexity code paths in the solution

No DB backend, reading files, no data cleanup and modification

No proper logic abstraction

No proper response creation, returning raw text

No structure (single file solution)

No unit tests

No data cleanup, validation and persistence


do i need to write serilizer for inputs and ouputs seperately
do i need to serializer for get ?
all cal in view?or serilizer? the structure of project
