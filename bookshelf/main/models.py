from django.db import models

class Books(models.Model):
    city = models.CharField('City', max_length=50)
    nickname = models.CharField('Nickname', max_length=50)
    title = models.CharField('Title', max_length=50)
    writer = models.CharField('Writer', max_length=50)
    description = models.CharField('Description', max_length=250)
    exchange = models.CharField('Exchange', max_length=250)
    telegram = models.CharField('Telegram', max_length=50)
    x = models.IntegerField('X')
    y = models.IntegerField('Y')

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Книга'
        verbose_name_plural = 'Книга'