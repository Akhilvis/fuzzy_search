# fuzzy_search
This project is an autocmplete system for searching keywords.Autocomplete suggestion ranking is based on the following criterias.

Constraints

    1. Matches can occur anywhere in the string, not just at the beginning. For example, eryx should match archaeopteryx (among others).
    2. The ranking of results should satisfy the following:
        a. We assume that the user is typing the beginning of the word. Thus, matches at the start of a word should be ranked higher. For example, for the input pract, the result practical should be ranked higher than impractical.
        b. Common words (those with a higher usage count) should rank higher than rare words.
        c. Short words should rank higher than long words. For example, given the input environ, the result environment should rank higher than environmentalism.
            i. As a corollary to the above, an exact match should always be ranked as the first result.
            
            
