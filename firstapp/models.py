from django.db import models

class Book(models.Model):

    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    price = models.IntegerField()
    publisher = models.CharField(max_length=20)
    ebook = models.BooleanField(default=True)

    class Meta:
        db_table = 'Books'

        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'

    def __str__(self):
        return "Title : {} Author : {} Price : {}".format(self.title, self.author, self.price)