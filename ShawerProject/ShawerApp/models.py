from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class counselor(models.Model):
    first_name=models.CharField(max_length=50,help_text="the name for counselor")
    last_name=models.CharField(max_length=50,help_text="the last for counselor")
    counselor=models.ForeignKey(User,on_delete=models.CASCADE)
    start_date=models.DateField()
    expertise_field=models.CharField(max_length=50)
    statment=models.TextField(max_length=240)
    image= models.ImageField(upload_to="images/")

    def __str__(self) -> str:
        return self.first_name+" "+ self.last_name

class comment(models.Model):
    name=models.CharField(max_length=50, verbose_name="الاسم")
    email=models.EmailField()
    body=models.TextField(verbose_name="التعليق")
    comment_date=models.DateTimeField(auto_now_add=True)
    active=models.BooleanField(default=False)
    profile=models.ForeignKey(counselor,on_delete=models.CASCADE,related_name='comments')

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self) -> str:
        return 'علق {} على {} '.format(self.name, self.profile)
