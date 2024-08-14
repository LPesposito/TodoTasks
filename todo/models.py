from datetime import date
from django.db import models


class Todo(models.Model):
    title = models.CharField(max_length=120, null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True, null=False, blank=False)
    deadline = models.DateField(null=False, blank=False)
    finished_at = models.DateField(null=True)

    class Meta:
        ordering = ["deadline"]

    def mask_as_complete(self):
        if not self.finished_at:
            self.finished_at = date.today()
            self.save()
