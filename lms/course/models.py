from django.db import models

import uuid



# Create your models here.

category_choices =[
    ('IT & Software' , 'IT & Software'),
    ('Finance' , 'Finance'),
    ('Marketing' , 'Marketing')
]

class BaseClass(models.Model):

    uuid = models.SlugField(unique=True,default=uuid.uuid4)

    active_status = models.BooleanField(default=True)

    created_at = models.DateTimeField( auto_now_add= True)

    updated_at = models.DateTimeField( auto_now=True)

    class Meta:

        abstract = True





class CategoryChoices(models.TextChoices):

    IT_SOFTWARE = 'IT & Software', 'IT & Software'

    FINANCE = 'Finance', 'Finance'

    MARKETING = 'Marketing','Marketing'


class LevelChoices(models.TextChoices):

    BEGINER='Begimner','Beginner'

    INTERMEDIATE='Intermediate','Intermediate'

    ADVANCE='Advance','Advance'

class Typechoice(models.TextChoices):

    FREE = 'Free', 'Free'

    PREMIUM = 'Premium', 'Premium'


class Course(BaseClass):

    title = models.CharField(max_length=50)

    description = models.TextField()

    image = models.ImageField(upload_to='course-images/')

    instructor = models.ForeignKey('instructors.Instructors',on_delete=models.CASCADE)
                                    #appname    . modelname

    category = models.CharField(max_length=50,choices=CategoryChoices.choices)

    level = models.CharField(max_length=25,choices=LevelChoices.choices)

    type = models.CharField(max_length=20,choices=Typechoice.choices)

    fee = models.DecimalField(max_digits=8,decimal_places=2)

    offer_fee = models.DecimalField(max_digits=8,decimal_places=2,null=True,blank=True)


    def __str__(self):
         return f'{self.title}-{self.instructor}'




    class Meta:

        verbose_name = 'Courses'

        verbose_name_plural = 'Courses'

        ordering = ['-id']