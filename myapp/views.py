from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def result(request):
    text = request.GET['fulltext']
    words = text.split()
    word_dictionary = {}

    for wd in words:
        if wd in word_dictionary:
            word_dictionary[wd]+=1
        else:
            word_dictionary[wd]=1

    return render(request, 'result.html', {'full' : text, 'words_num' : len(words), 'dictionary' : word_dictionary.items()})