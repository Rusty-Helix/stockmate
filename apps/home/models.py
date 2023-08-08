from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User


# class User(AbstractUser):
#     name = models.CharField(max_length=200, null=True)
#     real_first_name = models.CharField(max_length=200, null=True)
#     real_last_name = models.CharField(max_length=200, null=True)
    
#     email = models.EmailField(unique=True, null=True)
    
#     GENDER_CHOICES = (('M', 'Male'),
#                       ('F', 'Female'),
#                       ('T', 'Transgender'),
#                       ('N', 'Prefer not to tell'),
#                       )
#     gender = models.CharField(choices=GENDER_CHOICES, null=True, max_length=2)
    
#     bio = models.TextField(max_length=300, null=True)

#     # investment_motto = models.TextField(max_length=300, null=True)

#     avatar = models.ImageField(null=True, blank=True, default="default-avatar.svg")

#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = ['username']
class IsBuildingDeck(models.Model):
    id = models.AutoField(primary_key=True)
    is_building_deck = models.BooleanField(default=False)
    def __str__(self):
        return 'singleton boolean'
    
class StrategyCard(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200, default='empty title')
    selected = models.BooleanField(default=False)

    STRATEGY_TYPE_CHOICES = (
        ('candlestick pattern', 'candlestick pattern'),
        ('index value', 'index value'),
        ('index trend', 'index trend'),
        ('strategic stop', 'strategic stop'))
    strategyType = models.CharField(choices=STRATEGY_TYPE_CHOICES, default='free', max_length=200)

    SIGNAL_TYPE_CHOICES = (
        ('buy', 'buy'),
        ('sell', 'sell'),
        ('wait', 'wait'))
    signalType = models.CharField(choices=SIGNAL_TYPE_CHOICES, default='free', max_length=200)


    explanation = models.CharField(max_length=2000, default='empty explanation')
    cover = models.CharField(max_length=200, default='question-mark.jpg')
    footnote = models.CharField(max_length=200, default='empty footnote')

    # is_fulfilled = models.BooleanField(default=False)
    def __str__(self):
        return self.title

class StrategyDeck(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    creator = models.ForeignKey(User, blank=True, null=True, on_delete=models.PROTECT)
    # strategies = models.ManyToManyField(StrategyCard)
    strategies = models.CharField(max_length=2000, default='', null=True, blank=True)
    # is_current = models.BooleanField(default=False)
    def __str__(self):
        return self.title
    
class CurrentDeck(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    creator = models.ForeignKey(User, blank=True, null=True, on_delete=models.PROTECT)
    counter = models.BigIntegerField(default=1)
    strategies = models.CharField(max_length=2000, default='', null=True, blank=True)
    # strategies = models.ManyToManyField(StrategyCard, related_name='deck_strategies', blank=True)
    # strategies = models.ForeignKey(StrategyCard, on_delete=models.SET_NULL, null=True, blank=True)

    is_current = models.BooleanField(default=True)
    def __str__(self):
        return self.title

class Note(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    body = models.CharField(max_length=2000)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    NOTE_TYPE_CHOICES = (
        ('buy', 'buy'),
        ('sell', 'sell'),
        ('transaction series', 'transaction series'),
        ('free', 'free'))

    note_type = models.CharField(choices=NOTE_TYPE_CHOICES, default='free', max_length=200)

    def __str__(self):
        return self.title

class Transaction(models.Model):
    id = models.AutoField(primary_key=True)
    # transaction_series = models.ForeignKey(Series, on_delete=models.SET_NULL, null=True)
    ACTION_CHOICES = (('buy', 'buy'),
                    ('sell', 'sell'))

    actionType = models.CharField(choices=ACTION_CHOICES, max_length=200, default='buy')
    fulfilled_strategies = models.ManyToManyField(StrategyCard, related_name='fulfilled_series', blank=True)
    # annotation = models.CharField(max_length=200)
    note = models.ForeignKey(Note, on_delete=models.SET_NULL, null=True, blank=True)

    updated = models.DateTimeField(auto_now=True, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True, blank=True, null=True)



    class Meta:
        pass
        # ordering = ['-updated', '-created', 'like_count', 'message_count']
    def __str__(self):
        return self.annotation


class TransactionSeries(models.Model):
    id = models.AutoField(primary_key=True)
    verbose_name_plural = 'Transaction Series'
    # investor = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    # adopted_deck = models.ForeignKey(StrategyDeck, on_delete=models.PROTECT, null=True)
    title = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True, editable=False, blank=True, null=True)
    updated = models.DateTimeField(auto_now=True, blank=True, null=True)

    adoptedStrategyCard = models.ManyToManyField(StrategyCard, related_name='strategy_series', blank=True)
    adoptedStrategyDeck = models.ManyToManyField(StrategyDeck, related_name='strategy_series', blank=True)

    # annotation = models.CharField(max_length=200)
    note = models.ForeignKey(Note, on_delete=models.SET_NULL, null=True, blank=True)
    
    updated = models.DateTimeField(auto_now=True, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True, null=True, blank=True)


    def __str__(self):
        return self.title
    