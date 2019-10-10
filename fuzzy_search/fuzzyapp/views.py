from django.shortcuts import render
from django.http.response import JsonResponse
import re     # regex module from standard library.


# Create your views here.

def home(request):
    return render(request, 'autocomplete.html')


def fuzzy_search(request, *args, **kwargs):
    print ('fuzzy_search......................', request.GET.get('word', -1))
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


def fuzzyfinder(user_input, collection):
    suggestions = []
    pattern = '.*?'.join(user_input)  # Converts 'djm' to 'd.*?j.*?m'
    regex = re.compile(pattern)  # Compiles a regex.
    for item in collection:
        match = regex.search(item)  # Checks if the current item matches the regex.
        if match:
            suggestions.append((len(match.group()), match.start(), item))
    return [x for _, _, x in sorted(suggestions)]
