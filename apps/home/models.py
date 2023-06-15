from django.db import models
from django.contrib.auth.models import AbstractUser


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

class StrategyCard(models.Model):
    title = models.CharField(max_length=200, default='empty title')
    strategyType = models.CharField(max_length=200, default='empty strategyType')
    signalType = models.CharField(max_length=200, default='empty signal type')
    cover = models.CharField(max_length=200, default='empty cover')
    footnote = models.CharField(max_length=200, default='empty footnote')
    explanation = models.CharField(max_length=2000, default='empty explanation')
    # is_fulfilled = models.BooleanField(default=False)
    def __str__(self):
        return self.title

class StrategyDeck(models.Model):
    title = models.CharField(max_length=200)
    strategies = models.ManyToManyField(StrategyCard, related_name='deck_strategies', blank=True)
    def __str__(self):
        return self.title


class Series(models.Model):
    # investor = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    # adopted_deck = models.ForeignKey(StrategyDeck, on_delete=models.PROTECT, null=True)
    title = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    strategies = models.ManyToManyField(StrategyCard, related_name='strategy_series', blank=True)
    def __str__(self):
        return self.title


class Transaction(models.Model):
    # transaction_series = models.ForeignKey(Series, on_delete=models.SET_NULL, null=True)
    fulfilled_strategies = models.ManyToManyField(StrategyCard, related_name='fulfilled_series', blank=True)
    annotation = models.CharField(max_length=200)
    class Meta:
        pass
        # ordering = ['-updated', '-created', 'like_count', 'message_count']
    def __str__(self):
        return self.annotation