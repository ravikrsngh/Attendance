from django.db import models
from django.contrib.auth.models import AbstractUser, User
# Create your models here.
class Designation(models.Model):
	"""
	Description: Holds the Designations avbailable
	"""
	name = models.CharField(max_length=20, blank=True, null=True)

	def __str__(self):
		return self.name

class Department(models.Model):
	"""
	Description: Model Description
	"""
	name = models.CharField(max_length=20, blank=True, null=True)

	def __str__(self):
		return self.name

class teacher(models.Model):
    department=models.ForeignKey('Department',on_delete=models.CASCADE,null=True)
    designation=models.ForeignKey('Designation',on_delete=models.CASCADE,null=True)
    phone=models.CharField(max_length=10,blank=True,null=True)
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    def __str__(self):
        return self.user.first_name


class student(models.Model):
	"""docstring for userprofile."""
	user=models.OneToOneField(User,on_delete=models.CASCADE)
	phone=models.CharField(max_length=10,blank=True,null=True)
	sem=models.CharField(max_length=10,blank=True,null=True)
	usn=models.CharField(max_length=20,blank=True,null=True)
	branch=models.ForeignKey('Department',on_delete=models.CASCADE,null=True)
	pic1=models.ImageField(upload_to='student_pic/',blank=True)
	pic2=models.ImageField(upload_to='student_pic/',blank=True)
	pic3=models.ImageField(upload_to='student_pic/',blank=True)
	pic4=models.ImageField(upload_to='student_pic/',blank=True)
	pic5=models.ImageField(upload_to='student_pic/',blank=True)
	pic6=models.ImageField(upload_to='student_pic/',blank=True)
	pic7=models.ImageField(upload_to='student_pic/',blank=True)
	pic8=models.ImageField(upload_to='student_pic/',blank=True)
	pic9=models.ImageField(upload_to='student_pic/',blank=True)
	pic10=models.ImageField(upload_to='student_pic/',blank=True)
	pic11=models.ImageField(upload_to='student_pic/',blank=True)
	pic12=models.ImageField(upload_to='student_pic/',blank=True)
	pic13=models.ImageField(upload_to='student_pic/',blank=True)
	pic14=models.ImageField(upload_to='student_pic/',blank=True)
	pic15=models.ImageField(upload_to='student_pic/',blank=True)
	pic=models.ImageField(upload_to='student_pic/',blank=True)
	accepted=models.BooleanField(default=False)
	def __str__(self):
		return self.user.first_name
