from django.db import models

# Create your models here.
class myfiles(models.Model):
    file = models.FileField(upload_to="")
    user = models.CharField(max_length=100)

    def __str__(self):
        return self.file.name

    def delete(self, *args, **kwargs):
        self.file.delete()
        super().delete(*args, **kwargs)  # Call the "real" save() method.