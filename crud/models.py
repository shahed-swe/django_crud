from django.db import models

# Create your models here.

gender = (
    ('ml','Male'),
    ('fm', 'Female'),
)

class Information(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    father_name = models.CharField(max_length=50)
    mother_name = models.CharField(max_length=50)
    age = models.CharField(max_length=3)
    gender = models.CharField(max_length=6, choices=gender,default=None)
    email = models.CharField(max_length=50)
    password_first = models.CharField(max_length=128)

    def get_absolute_url(self):
        return f"/{self.id}"
    
    def get_edit_url(self):
        return f"{self.get_absolute_url()}/edit"

    def get_delete_url(self):
        return f"{self.get_absolute_url()}/delete"    

    class Meta:
        db_table = 'information'
