# fuzzy_search
This project is an autocmplete system for searching keywords.Autocomplete suggestion ranking is based on the following criterias.

Constraints

    1. Matches can occur anywhere in the string, not just at the beginning. For example, eryx should match archaeopteryx (among others).
    2. The ranking of results should satisfy the following:
        a. We assume that the user is typing the beginning of the word. Thus, matches at the start of a word should be ranked higher. For example, for the input pract, the result practical should be ranked higher than impractical.
        b. Common words (those with a higher usage count) should rank higher than rare words.
        c. Short words should rank higher than long words. For example, given the input environ, the result environment should rank higher than environmentalism.
            i. As a corollary to the above, an exact match should always be ranked as the first result.

## Algorithm

Inorder to show dictionary word suggestions according to above criteria , different characteristics are calculated using regular expression patterns, string operations etc. 

Regex = '.*?'

This regex pattern will find all words having searched alphabets.

### Word Characteristics

1. Length of the word
2. Position of the occurence of first letter.
3. Viewers count(directly get from dctionary file)

### Finding weighted average of all characteristics

Inorder to find weighted average , making a linear equation with a multipliyng factor.Adjust those mutiplying factors to get the desired result.

    length_factor = .5
    position_factor = 100
    view_count_factor = .0001
    
    rank = (length_factor * Length of the word) + (position_factor * (20 - Position of the occurence of first letter)) +
            (view_count_factor *  Viewers count)

we are assuing maximum word length as 20 and substracting Position of the occurence of first letter from 20, since words starts with given input should get higher rank.


            
            


