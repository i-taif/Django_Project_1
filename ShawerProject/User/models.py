from django.db import models
from django.db import models

class counselor(models.Model):
    username=models.CharField(max_length=50)
    first_name=models.CharField(max_length=50,help_text="the name for counselor")
    last_name=models.CharField(max_length=50,help_text="the name for counselor")
    start_date=models.DateField()
    expertise_field=models.CharField(max_length=50)
    statment=models.TextField(max_length=240)
    USERNAME_FIELD = 'username'
    image= models.ImageField(upload_to="images/")

    def _str_(self) -> str:
        return self.usernamecounselor+ " " +self.first_name+ " " +self.last_name