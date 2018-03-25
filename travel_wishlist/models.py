from django.db import models
import time

# Create your models here.

class Place(models.Model):
    name = models.CharField(max_length=200)
    visited = models.BooleanField(default=False)
    visited_date = models.DateTimeField(
            blank=True, null=True)
    review_text = models.TextField(blank=True, null=True)

    def __str__(self):
        struct_time = time.strptime(self.visited_date, "%d %b %y")
        return '%s visited? %s %s %s' % (self.name, self.visited, struct_time, self.review_text)
