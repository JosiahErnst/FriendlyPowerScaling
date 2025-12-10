from django.shortcuts import render
from .myForms import CreateProfile, search

# Create your views here.

def home(request):
    searchIn = search(request.POST)
    if request.method == "POST":
        if searchIn.is_valid() and (searchIn != None) and (searchIn != ""):
            return render(request, 'searchResults.html', {"searchForm": searchIn})
    
    return render(request, 'home.html', {"searchForm": searchIn})

def profile(request):
    searchIn = search(request.POST)
    if request.method == "POST":
        if searchIn.is_valid() and (searchIn != None) and (searchIn != ""):
            return render(request, 'searchResults.html', {"searchForm": searchIn})
        
    return render(request, 'profile.html', {"searchForm": searchIn})

def battle(request):
    searchIn = search(request.POST)
    if request.method == "POST":
        if searchIn.is_valid() and (searchIn != None) and (searchIn != ""):
            return render(request, 'searchResults.html', {"searchForm": searchIn})
        
    return render(request, 'battle.html', {"searchForm": searchIn})

def createProfile(request):
    searchIn = search(request.POST)
    if request.method == "POST":
        if searchIn.is_valid() and (searchIn != None) and (searchIn != ""):
            return render(request, 'searchResults.html', {"searchForm": searchIn})
        
    newProfileForm = CreateProfile(request.POST)
    if newProfileForm.is_valid():
        return render(request, 'createProfile.html', {"form": newProfileForm})
    
    return render(request, 'createProfile.html', {"form": newProfileForm, "searchForm": searchIn})

def searchResults(request):
    searchIn = search(request.POST)
    if searchIn.is_valid():
        return render(request, 'searchResults.html', {"searchForm": searchIn})
    return render(request, 'searchResults.html', {"searchForm": searchIn})