from typing import Any
from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length =200)
    pub_Date = models.DateTimeField()
    body = models.TextField()
    image = models.ImageField(upload_to="images/")
    
    def summart(self):
        return self.body[:100]
    



    
