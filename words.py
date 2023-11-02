def print_upper_words(words, must_start_with):
    """     Prints only the words from the list 
    that start with one of the letters in the set, 
    but converted to all caps

    words : list
        a list of words to be filtered
    must_start_with : set
        a set of letters to filter the list by
    return : list
        a list of all caps words that begin with the given letters
    """
    result = ""
    for each in words:
        if each[0] in must_start_with:
            result += (" " + each.upper())
    print (result)


print_upper_words