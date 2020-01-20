# hivery-backend-challenge

# developing enviroment
# main dependecy 
python3.8
django-2.2.9,
djongo-1.3.0 
djangorestframework-3.11.0.
# database 
MongoDB 4.2.2



# the instruction to set up this project
1. clone project
    1. git clone https://github.com/LeonDong199509/hivery-backend-challenge.git
2. go to peoject directory
    1. cd hivery-backend0challenge
3. setting up virtual enviroment
    1. pip3 install virtualenv
    2. virtualenv --python=python3 venv
    3. for windows: venv\Scripts\activate
       for linux: source venv/bin/activate
4. install dependencies
    1. pip install -r requirements.txt
5. start your mongodb service
    for example:  systemctl start mongod
6. make database migration 
    1. cd hivery_backend
    2. python manage.py makemigrations
    3. python manage.py migrate
7. import json file to mongodb 
    (go back to your terminal)
    1. mongoimport --db paranuara --collection companies --type json --file <the companies.json file path> --jsonArray
    2. mongoimport --db paranuara --collection people --type json --file <the people.json file path> --jsonArray

8. start django
    1. python manage.py runserver

Now you can access all apis, see docs at /docs endpoint
In case of any accident, you can access the api via my AWSec2 server at http://leonkani.com:8000/docs/







