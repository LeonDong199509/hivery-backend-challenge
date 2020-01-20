from djongo import models

class Company(models.Model):
    _id = models.ObjectIdField()
    index = models.IntegerField(unique=True)
    company = models.CharField(max_length=16)
    class Meta:
        db_table = 'companies'

class Person(models.Model):
    GENDER_CHOICES = [
        ('male','male'),
        ('female','female')
    ]
    _id = models.ObjectIdField()
    index = models.IntegerField(unique=True)
    guid = models.CharField(max_length=40)
    has_died = models.BooleanField(default=False)
    balance = models.CharField(max_length=16)
    picture= models.URLField(max_length=200)
    age = models.IntegerField()
    eyeColor = models.CharField(max_length=6)
    name = models.CharField(max_length=16)
    gender = models.CharField(max_length=5,choices=GENDER_CHOICES)
    company_id = models.IntegerField()
    email = models.EmailField()
    phone = models.CharField(max_length=16)
    address = models.CharField(max_length=50)
    about = models.TextField()
    registered = models.DateTimeField()
    tags = models.CharField(max_length=50,default = '[]')
    friends = models.CharField(max_length=500,default = '[]')
    greeting = models.TextField()
    favouriteFood = models.CharField(max_length=500,default = '[]')
    class Meta:
        db_table = 'people'

