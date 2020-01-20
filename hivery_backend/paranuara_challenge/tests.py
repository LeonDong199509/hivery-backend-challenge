from paranuara_challenge.models import Company
from paranuara_challenge.serializers import CompanySerializer
from paranuara_challenge.models import Person
from paranuara_challenge.serializers import PersonSerializer
from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework.views import status
import json

class BaseViewTest(APITestCase):
    client = APIClient()

    @staticmethod
    def create_company(index='', company=''):
        Company.objects.create(index=index, company=company)

    @staticmethod
    def create_person(index='',company_id='',friends='',name='',age='',address='',phone='',eyeColor='',has_died='',favouriteFood=''):
        Person.objects.create(
            index=index,
            company_id=company_id,
            friends=friends,
            name=name,
            age=age,
            address=address,
            phone=phone,
            eyeColor=eyeColor,
            has_died=has_died,
            favouriteFood=favouriteFood
        )


    def setUp(self):
        # add test data
        self.create_company(1, "sean")
        self.create_company(2, "konshens")
        self.create_company(3, "brick")
        self.create_company(4, "marley")
        friends1= [
            {'index':1},{'index':2}
        ]
        friends2= [
            {'index':1},{'index':2}
        ]
        friends3= [
            {'index':1},{'index':3}
        ]
        food1=[ "orange","beetroot","banana","strawberry"]
        food2=[ "orange","banana","strawberry"]
        food3=["orange","banana","apple","carrot"]
        self.create_person(1,1,json.dumps(friends1),'peter',28,'no','12121212','brown',False,json.dumps(food1))
        self.create_person(2,1,json.dumps(friends2),'scott',28,'no','12121212','blue',False,json.dumps(food2))
        self.create_person(3,2,json.dumps(friends3),'rose',28,'no','12121212','blue',False,json.dumps(food3))

class GetFavoriteFoodTest(BaseViewTest):
    def test_fet_favorite_food(self):
        """
            This test ensures that favorite food is spilited to fruits and vegs 
            when we request this endpoint
        """
        response = self.client.get(
            reverse("favorite-food",kwargs={"index": 1})      
        )
        person_obj = Person.objects.get(index=1)
        expected = {
            'username' : person_obj.name,
            'age' : person_obj.age,
            'fruits' : [ "orange","banana","strawberry"],
            'vegetables': ["beetroot"]
        }
        self.assertEqual(response.data, expected)
        self.assertEqual(response.status_code, status.HTTP_200_OK)



class GetCommonFriendsTest(BaseViewTest):
    def test_get_friends(self):
        """
            This test ensures we get common brown eye and living friends of 2 people
            when we post indexes of them to the endpoint
        """
        data ={
            'person1':1,
            'person2':2
        }
        person1_obj = Person.objects.get(index=1)
        person2_obj = Person.objects.get(index=2)
        response = self.client.post(
            reverse('common_friends'),
            data = data
        )
        person1_info = {
            'name': person1_obj.name,
            'age': person1_obj.age,
            'address' : person1_obj.address,
            'phone' : person1_obj.phone
        }
        person2_info = {
            'name': person2_obj.name,
            'age': person2_obj.age,
            'address' : person2_obj.address,
            'phone' : person2_obj.phone
        }
        expected = {
            'person1': person1_info,
            'person2': person2_info,
            'common_friends': [1]
        }
        self.assertEqual(response.data, expected)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class GetEmployeesTest(BaseViewTest):
    def test_get_employees(self):
        """
            This test ensures that all employees for a given company
            return when we make a GET request to the that endpoint
        """
        response = self.client.get(
            reverse("employees",kwargs={"index": 1})
        )
        expected = Person.objects.filter(company_id=1)
        serialized = PersonSerializer(expected, many=True)
        self.assertEqual(response.data, serialized.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class GetAllCompaniesTest(BaseViewTest):   
    def test_get_all_companies(self):
        """
            This test ensures that all companiess added in the setUp method
            exist when we make a GET request to the companies/ endpoint
        """
        # hit the API endpoint
        response = self.client.get(
            reverse("companies")
        )
        # fetch the data from db
        expected = Company.objects.all()
        serialized = CompanySerializer(expected, many=True)
        self.assertEqual(response.data, serialized.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)