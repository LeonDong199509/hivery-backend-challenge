from django.shortcuts import render
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from paranuara_challenge.models import Company
from paranuara_challenge.serializers import CompanySerializer
from paranuara_challenge.models import Person
from paranuara_challenge.serializers import PersonSerializer
from paranuara_challenge.serializers import CommonFriendSeializer
from paranuara_challenge.utils.utils import split_fruit_veg,find_common,clean_friends,find_friends

class CompanyList(generics.ListAPIView):
    '''
        Get all companies
    '''
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

class CompanyDetail(generics.RetrieveAPIView):
    '''
        Get the company from the index
        index -- the index of the company you wanna search
    '''
    lookup_field = 'index'
    queryset = Company.objects.all()
    serializer_class = CompanySerializer


class PersonList(generics.ListAPIView):
    '''
        Get all employees for the company, when the index of company is given
        index -- the index of the company you want to search
    '''
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
    def get_queryset(self):
        if 'index' in self.kwargs:
            return Person.objects.filter(company_id=self.kwargs['index'])
        else:
            return Person.objects.all()

class CommonFriendView(generics.GenericAPIView):
    serializer_class = CommonFriendSeializer
    def post(self,request):
        '''
            Get common friends of 2 people
            person1 -- the index of the first person
            person2 -- the index of the second person
        '''
        serializer = CommonFriendSeializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        person1 = serializer.validated_data.get('person1')
        person2 = serializer.validated_data.get('person2')
        try:
            person1_obj = Person.objects.get(index=person1)
        except:
            return Response({'error': "person1 not exist"}, status=status.HTTP_404_NOT_FOUND)
        try:
            person2_obj = Person.objects.get(index=person2)
        except:
            return Response({'error': "person2 not exist"}, status=status.HTTP_404_NOT_FOUND)
        common_friend = find_common(clean_friends(person1_obj.friends),clean_friends(person2_obj.friends))
        conditioned_friend = find_friends(common_friend) 
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
        data = {
            'person1': person1_info,
            'person2': person2_info,
            'common_friends': conditioned_friend
        }
        return Response(data, status=status.HTTP_200_OK)
    

class FruitVegView(APIView):
    def get(self,request,index):
        """  
            Get person's favorite fruits and vegetables
            index -- the index of the person you want to search
        """ 
        try:
            person_obj = Person.objects.get(index=int(index))
        except:
            return Response({'error': "person not exist"}, status=status.HTTP_404_NOT_FOUND)
        fruits,vegs = split_fruit_veg(person_obj.favouriteFood)
        data= {
            'username' : person_obj.name,
            'age' : person_obj.age,
            'fruits' : fruits,
            'vegetables': vegs
        }
        return Response(data, status=status.HTTP_200_OK)

