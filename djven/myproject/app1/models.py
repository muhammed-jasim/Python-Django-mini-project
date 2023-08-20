from django.db import models

# Create your models here.
class Details(models.Model):
    name = models.CharField(max_length=36,null=True,blank=True);
    course_details = models.TextField(null=True,blank=True); 

    def __str__(self):
        return self.name

class Teachers(models.Model):
    teacher_name = models.CharField(max_length=36,null=True,blank=True);
    name=models.ForeignKey(Details,on_delete=models.CASCADE);
    teacher_image = models.ImageField(upload_to='teacher');

class Contacts(models.Model):
    user_name = models.CharField(max_length=30,null=True,blank=True)
    email_id = models.EmailField()
    phone = models.CharField(max_length=10)
    name = models.ForeignKey(Details,on_delete=models.CASCADE);
 