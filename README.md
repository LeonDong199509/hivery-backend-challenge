# hivery-backend-challenge

# my developing enviroment
python3.8
django-2.2.9,
djongo-1.3.0 
djangorestframework-3.11.0.
MongoDB 4.2.2



# the instruction to set up this project
1. clone project
    1. git clone https://github.com/LeonDong199509/hivery-backend-challenge.git
2. go to peoject directory
    1. cd hivery-backend-challenge
3. setting up virtual enviroment
    1. pip3 install virtualenv
    2. virtualenv --python=python3 venv
    3. for windows: venv\Scripts\activate
       for linux: source venv/bin/activate
4. install dependencies
    1. pip install -r requirements.txt
5. start your mongodb service
    for example on linux:  systemctl start mongod
                on windows: net start MongoDB
6. make database migration 
    If your database is authenticated,you need to add your database username and password in /hivery_backend/settings.py.
    1. cd hivery_backend
    2. python manage.py makemigrations
    3. python manage.py migrate
7. import json files to mongodb 
    (go back to your terminal)
    If your database is non-authenticated:
    1. mongoimport --db paranuara --collection companies --type json --file <the companies.json file path> --jsonArray
    2. mongoimport --db paranuara --collection people --type json --file <the people.json file path> --jsonArray
    If your database is authenticated:
    1. mongoimport --db paranuara --collection companies --type json --file <the companies.json file path> --jsonArray --authenticationDatabase admin --username "yourAdminname" --password "yourpassword"
    2. mongoimport --db paranuara --collection people --type json --file <the people.json file path> --jsonArray --authenticationDatabase admin --username "yourAdminname" --password "yourpassword"
8. start django
    1. python manage.py runserver

Now you can access all APIs, see docs at http://127.0.0.1:8000/docs endpoint.
In case of any accident, you can access the api via my AWSec2 server at http://leonkani.com:8000/docs/







