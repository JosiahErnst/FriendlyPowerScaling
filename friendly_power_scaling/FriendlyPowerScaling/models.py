from django.db import models

# Create your models here.

class User(models.Model):
    Username = models.CharField(max_length=15)
    Password = models.CharField(max_length=30)
    FirstName = models.CharField(max_length=15)
    LastName = models.CharField(max_length=15)
    Description = models.TextField(max_length=400)
    Strength = models.IntegerField()
    Charisma = models.IntegerField()
    Intelligence = models.IntegerField()
    Wisdom = models.IntegerField()
    Dexterity = models.IntegerField()
    Grit = models.IntegerField()
    Overall = models.IntegerField()
    

class Profile(models.Model):
    id = models.BigAutoField(primary_key=True, unique=True)
    FirstName = models.CharField(max_length=15)
    LastName = models.CharField(max_length=15)
    Description = models.TextField(max_length=400)
    Strength = models.IntegerField()
    Charisma = models.IntegerField()
    Intelligence = models.IntegerField()
    Wisdom = models.IntegerField()
    Dexterity = models.IntegerField()
    Grit = models.IntegerField()
    Overall = models.IntegerField()
    
class Scoreboard(models.Model):
    player1 = models.ForeignKey(Profile, unique=True, related_name="+", on_delete=models.DO_NOTHING)
    player2 = models.ForeignKey(Profile, unique=True, related_name="+", on_delete=models.DO_NOTHING)
    player3 = models.ForeignKey(Profile, unique=True, related_name="+", on_delete=models.DO_NOTHING)
    player4 = models.ForeignKey(Profile, unique=True, related_name="+", on_delete=models.DO_NOTHING)
    player5 = models.ForeignKey(Profile, unique=True, related_name="+", on_delete=models.DO_NOTHING)
    player6 = models.ForeignKey(Profile, unique=True, related_name="+", on_delete=models.DO_NOTHING)
    player7 = models.ForeignKey(Profile, unique=True, related_name="+", on_delete=models.DO_NOTHING)
    player8 = models.ForeignKey(Profile, unique=True, related_name="+", on_delete=models.DO_NOTHING)
    player9 = models.ForeignKey(Profile, unique=True, related_name="+", on_delete=models.DO_NOTHING)
    player10 = models.ForeignKey(Profile, unique=True, related_name="+", on_delete=models.DO_NOTHING)
    
    
class Battle(models.Model):
    player1 = models.ForeignKey(Profile, unique=True, related_name="+", on_delete=models.DO_NOTHING)
    player2 = models.ForeignKey(Profile, unique=True, related_name="+", on_delete=models.DO_NOTHING)
    WIN_CON_OPTIONS = {
        "S" : "Strength",
        "C" : "Charisma",
        "I" : "Intelligence",
        "W" : "Wisdom",
        "D" : "Dexterity",
        "G" : "Grit",
    }
    winCondition = models.CharField(max_length=1, choices=WIN_CON_OPTIONS)
    
    
    

    