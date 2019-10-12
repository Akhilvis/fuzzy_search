from django.shortcuts import render
from django.http.response import JsonResponse
import re  # regex module from standard library.
import csv


# Create your views here.

def home(request):
    return render(request, 'autocomplete.html')


def fuzzy_search(request, *args, **kwargs):
    print ('fuzzy_search......................', request.GET.get('word', -1))
    word = request.GET.get('word', '')

    dict_list = tsv_file_reader()
    auto_list = fuzzyfinder(word, dict_list)[:25]
    print (auto_list)

    return JsonResponse({'success': True, 'autocomplete': auto_list})


def fuzzyfinder(user_input, collection):
    suggestions = []
    pattern = '.*?'.join(user_input)  # Converts 'djm' to 'd.*?j.*?m'
    regex = re.compile(pattern)  # Compiles a regex.
    for item in collection:
        match = regex.search(item[0])  # Checks if the current item matches the regex.
        if match:
            suggestions.append((len(match.group()), match.start(), int(item[1]), item[0]))
    print ('length of suggestions.....', len(suggestions))
    weighted_list = find_weighted_average(suggestions)
    print (888888888888888888888888,weighted_list)
    ranked_suggetions = [x for _, x in sorted(weighted_list, reverse=True)]
    print('########################################################')
    print (ranked_suggetions)
    print('#######################-------#################################')

    return ranked_suggetions


def tsv_file_reader():
    dict_list = []
    with open("fuzzyapp/word_search.tsv") as tsvfile:
        tsvreader = csv.reader(tsvfile, delimiter="\t")
        for line in tsvreader:
            dict_list.append(line)

    return dict_list


def find_weighted_average(suggestions):
    print ('find_weighted_average',suggestions[:5])
    weighted_list = []
    # Linear Equation to find weighted average
    length_factor = .5
    position_factor = 100
    view_count_factor = .0001


    for word_list in suggestions:
        print ('loop.........',word_list)
        rank  = (length_factor*word_list[0]) + (position_factor*(20 - word_list[1])) + (view_count_factor*word_list[2])

        weighted_list.append((rank, word_list[3]))
    print ('@@@@@@@@@@@@@@@@@@@@@@@@@@@@@', weighted_list)
    return weighted_list

