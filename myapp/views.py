from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def result(request):
    text = request.GET['fulltext']
    words = text.split()
    length = len(words)

    word_dictionary = {}
    for word in words:
        if word in word_dictionary : 
            #increase
            word_dictionary[word] += 1
        else :
            #add to dictionary
            word_dictionary[word] = 1

    return render(request, 'result.html', {'full': text, 'full_len': length, 'dictionary' : word_dictionary.items()})
