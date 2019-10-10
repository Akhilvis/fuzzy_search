from django.shortcuts import render
from django.http.response import JsonResponse

# Create your views here.

def home(request):
    return render(request, 'autocomplete.html')

def fuzzy_search(request, *args, **kwargs):
    print ('fuzzy_search......................',request.GET.get('word', -1))
    word = request.GET.get('word', '')

    autocomplete = [
      "ActionScript",
      "AppleScript",
      "Asp",
      "BASIC",
      "C",
      "C++",
      "Clojure",
      "COBOL",
      "ColdFusion",
      "Erlang",
      "Fortran",
      "Groovy",
      "Haskell",
      "Java",
      "JavaScript",
      "Lisp",
      "Perl",
      "PHP",
      "Python",
      "Ruby",
      "Scala",
      "Scheme"
    ]

    return JsonResponse({'success': True, 'autocomplete': autocomplete})
