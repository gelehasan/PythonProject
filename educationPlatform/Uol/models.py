from django.db import models

 
# Create your models here.

class User(models.Model):
    id= models.AutoField(primary_key=True) 
    userName= models.CharField(max_length=256, null=False,unique=True, blank=False)
    email=  models.CharField(max_length=256, null=False, blank=False)
    role =  models.CharField(max_length=256, null=False, blank=False)
    joinDate = models.DateField(auto_now_add=True) 

    def __str__(self):
        return self.userName

class Course(models.Model):
     id = models.CharField(primary_key=True, max_length=256) 
     modelName= models.CharField(max_length=256, null=False, blank=False)
     writtenExam= models.CharField(max_length=256, null=False, blank=False)
     category = models.CharField(max_length=256, null=False, blank=False)
     instructor = models.ForeignKey(User, on_delete=models.DO_NOTHING)
     publishDate = models.DateField(auto_now_add=True)

     def __str__(self):
        return self.modelName
        
        



     
class Enrollment(models.Model):
    id = models.AutoField(primary_key=True) 
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    course= models.ForeignKey(Course,on_delete=models.CASCADE)
    enrollmentDate = models.DateField(auto_now_add=True)
    progress = models.IntegerField(null=False, blank=False)
    status = models.CharField(max_length=256, null=False, blank=False)

    def __str__(self):
        return f"{self.user.userName} enrolled in {self.course.modelName}"

class CourseReview (models.Model):
    id = models.AutoField(primary_key=True) 
    user= models.ForeignKey(User,on_delete=models.CASCADE)
    course =  models.ForeignKey(Course,on_delete=models.CASCADE)
    rating = models.IntegerField(null=False, blank=False)
    comment = models.TextField(null=False, blank=False)
    ReviewDate= models.DateField(auto_now_add=True)

    def __str__(self):
        return f"Review by {self.user.userName} for {self.course.title} with rating {self.rating}"