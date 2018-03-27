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
        print('entered __str__')
        if self.visited_date is None:
            print(str(self.visited_date))
            print(' no date ')
            return '%s visited? %s %s ' % (self.name, self.visited, self.review_text)
        else:
            print(' has a date ')
            struct_time = time.strptime(self.visited_date, "%d %b %y")
            print(struct_time)
            return '%s visited? %s %s %s' % (self.name, self.visited, struct_time, self.review_text)

