from django.db import models

# Create your models here.
class Adhaar(models.Model):
    adharr_no=models.IntegerField()
    create_date=models.DateField(auto_now_add=True)
    create_by=models.CharField(max_length=20)

    def __str__(self):
        return str(self.adharr_no)

class Stu(models.Model):
    name=models.CharField(max_length=20)
    email=models.CharField(max_length=20)
    contact=models.IntegerField(max_length=20)
    city=models.CharField(max_length=20)
    # without related name
    # a_no=models.OneToOneField(Adhaar,on_delete=models.CASCADE,related_name='puju')
    a_no=models.OneToOneField(Adhaar,on_delete=models.CASCADE)
    # with related name
    # a_no=models.OneToOneField(Adhaar,on_delete=models.CASCADE,related_name='jatin')
    # adhaar_obj = Adhaar.objects.get(id=1) 
    # Stu.objects.create(name="Rahul", a_no=adhaar_obj)


