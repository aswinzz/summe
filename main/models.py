from django.db import models
import random
class PDF(models.Model):
    pdfFile = models.FileField(upload_to='documents/',default='dummy.txt')
    def save(self, *args, **kwargs):
        randomNum = random.randint(10000,90000)
        new_name = str(randomNum) + ".pdf"
        self.pdfFile.name = new_name
        super(PDF, self).save(*args, **kwargs)

class Doc(models.Model):
    docFile = models.FileField(upload_to='documents/',default='dummy.txt')
    def save(self, *args, **kwargs):
        randomNum = random.randint(10000,90000)
        new_name = str(randomNum) + ".docx"
        self.docFile.name = new_name
        super(Doc, self).save(*args, **kwargs)
