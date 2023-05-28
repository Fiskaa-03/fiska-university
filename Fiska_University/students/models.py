from django.db import models

# Create your models here.
class Major_Data(models.Model):
    major_name = models.CharField(max_length=50)

    def __str__(self):
        return self.major_name


class Status_Data(models.Model):
    status = models.CharField(max_length=50)

    def __str__(self):
        return self.status


class Students_Data(models.Model):
    id = models.IntegerField(unique=True, editable=False)
    NIM = models.CharField(max_length=20, primary_key=True)
    name = models.CharField(max_length=100)
    major = models.ForeignKey(Major_Data, on_delete=models.RESTRICT)
    email = models.EmailField(max_length=200)
    contact = models.CharField(max_length=20)
    status = models.ForeignKey(Status_Data, on_delete=models.RESTRICT)

    def save(self, *args, **kwargs):
        self.object_list = Students_Data.objects.order_by('id')

        if len(self.object_list) == 0:  # if there are no objects
            self.id = 1
        else:
            self.id = self.object_list.last().id + 1

        super(Students_Data, self).save()

    # def save(self, *args, **kwargs):
    #     students = Students_Data.objects.all()

    #     if students.exists() and self._state.adding:
    #         last_student = students.latest('id')
    #         self.order = int(last_student.id) + 1
    #     super().save(*args, **kwargs)
