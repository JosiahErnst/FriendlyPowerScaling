from django import forms 


# Information here found in the Django Forms documentation

class CreateProfile(forms.Form):
    FirstName = forms.CharField(label="First Name", max_length=15)
    LastName = forms.CharField(label="Last Name", max_length=15)
    Description = forms.TextInput()
    Strength = forms.IntegerField(label="Strength")
    Charisma = forms.IntegerField(label="Charisma")
    Intelligence = forms.IntegerField(label="Intelligence")
    Wisdom = forms.IntegerField(label="Wisdom")
    Dexterity = forms.IntegerField(label="Dexterity")
    Grit = forms.IntegerField(label="Grit")
    Overall = forms.IntegerField(label="Overall")
    
class search(forms.Form):
    search = forms.CharField(label='', max_length=50, required=False, min_length=1)