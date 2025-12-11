from django.shortcuts import render
from .myForms import CreateProfile, search
from .models import Profile

# Create your views here.

def home(request):
    searchIn = search(request.POST)
    if request.method == "POST":
        if searchIn.is_valid() and (searchIn != None) and (searchIn != ""):
            return render(request, 'searchResults.html', {"searchForm": searchIn})
    
    queryAll = len(Profile.objects.all())
    data = []
    
    i = 1
    while i < queryAll+1:
        data.append(Profile.objects.get(pk=i))
        i += 1
        
    print(data)
    
    return render(request, 'home.html', {"searchForm": searchIn})

def battle(request):
    searchIn = search(request.POST)
    if request.method == "POST":
        if searchIn.is_valid() and (searchIn != None) and (searchIn != ""):
            return render(request, 'searchResults.html', {"searchForm": searchIn})
        
    return render(request, 'battle.html', {"searchForm": searchIn})

def createProfile(request):
    newProfileForm = CreateProfile(request.POST)
    if newProfileForm.is_valid():
        return render(request, 'createProfile.html', {"form": newProfileForm})
    
    searchIn = search(request.POST)
    if request.method == "POST":
        if searchIn.is_valid() and (searchIn != None) and (searchIn != ""):
            return render(request, 'searchResults.html', {"searchForm": searchIn})
        
    print(Profile.objects.all())
    return render(request, 'createProfile.html', {"form": newProfileForm, "searchForm": searchIn})

def searchResults(request):
    searchIn = search(request.GET)
    return render(request, 'searchResults.html', {"searchForm": searchIn})