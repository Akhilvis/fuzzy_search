from django.shortcuts import render
from django.http.response import JsonResponse
import re     # regex module from standard library.
import csv

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

    dict_list = tsv_file_reader()
    auto_list = fuzzyfinder(word, dict_list)[:10]
    print (auto_list)


    return JsonResponse({'success': True, 'autocomplete': auto_list})


def fuzzyfinder(user_input, collection):
    suggestions = []
    pattern = '.*?'.join(user_input)  # Converts 'djm' to 'd.*?j.*?m'
    regex = re.compile(pattern)  # Compiles a regex.
    for item in collection:
        match = regex.search(item)  # Checks if the current item matches the regex.
        if match:
            suggestions.append((len(match.group()), match.start(), item))
    return [x for _, _, x in sorted(suggestions)]

def tsv_file_reader():
    dict_list = []
    with open("fuzzyapp/word_search.tsv") as tsvfile:
        tsvreader = csv.reader(tsvfile, delimiter="\t")
        for line in tsvreader:
            dict_list.append(line[0])

    return dict_list