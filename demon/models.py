from django.db import models

class DemonCheker(models.Model):
    subject = models.CharField(verbose_name='Демон', max_length=100)
    state = models.BooleanField(verbose_name='Состояние', default=False)

    def __str__(self):
        return f"{self.subject}"
