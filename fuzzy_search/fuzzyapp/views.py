from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'autocomplete.html')

def fuzzy_search(request, *args, **kwargs):
    print ('fuzzy_search......................',request.GET.get('word', -1))
    word = request.GET.get('word', '')
