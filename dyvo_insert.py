def dyvo_insert(sentence, flag):
    """
    (str, str) -> str
    Inserting word "диво" before every word that starts with flag.

    >>> dyvo_insert('Кит кота по хвилях катав - кит у воді, кіт на киті', 'ки')
    'дивокит кота по хвилях катав - дивокит у воді, кіт на дивокиті'

    >>> dyvo_insert('Кіт у морі - кит у дворі', 'ки')
    'кіт у морі - дивокит у дворі'
    """
    element_index = 0
    sentence = sentence.lower()
    while element_index < len(sentence)-2:
        if sentence[element_index] + sentence[element_index + 1] == flag \
            and (sentence[element_index - 1] == ' ' or element_index == 0):
            length_of_word = 0
            element_index_word = element_index
            while sentence[element_index_word] != " " and element_index_word < len(sentence)-1:
                length_of_word += 1
                element_index_word += 1
            sentence_change_position = sentence[element_index : len(sentence)]
            sentence = sentence.replace(sentence_change_position, \
                'диво' + sentence_change_position)
            element_index += len(flag) + length_of_word + 1
        element_index += 1
    return sentence
            

if __name__ == "__main__":
   import doctest
   print(doctest.testmod())
    