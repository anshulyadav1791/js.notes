from django.db import models

class m_ki_c_Admin(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    email = models.EmailField(unique=True)
    enrollment_data = models.DateField(auto_now_add=True)
    # city = models.CharField(max_length=100,d2efault='Unknown')

    def __str__(self):
        return self.name