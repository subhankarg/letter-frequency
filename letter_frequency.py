#!/usr/bin/python3
#
#
#  The MIT License (MIT)
#
#  Copyright (c) 2012 Subhankar Ghosh
#
#  Permission is hereby granted, free of charge, to any person obtaining a copy
#  of this software and associated documentation files (the "Software"), to deal
#  in the Software without restriction, including without limitation the rights
#  to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#  copies of the Software, and to permit persons to whom the Software is
#  furnished to do so, subject to the following conditions:
#
#  The above copyright notice and this permission notice shall be included in all
#  copies or substantial portions of the Software.
#
#  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#  IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#  FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#  AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#  LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#  OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
#  SOFTWARE.
#  
#  

"""
Finds the letter frequency of texts in Bengali or
Devanagari Unicode scripts

Python 3 required for proper Unicode support
"""

__version__ = "1.1"

import os
import sys

DEPENDENTS_BENGALI = "ািীুূৃেৈোৌংঃঁ'"
DEPENDENTS_DEVANAGARI = "ािीुूृॄॅॆेैॉॊोौँंः"

DEPENDENTS = DEPENDENTS_BENGALI + DEPENDENTS_DEVANAGARI
JOINERS = u'्্\u200D'
NONJOINERS = u'\u200C'

# Set True to enable including semivowels with consonants
SEMIVOWELS_MODE = False


def text_fix(data):
    """
    Optionally remove or fix any known
    letter errors in the corpus
    """
    # Strip Unicode BOM
    data = data.replace(u'\uFEFF', '')
    # data = data.replace('৷', '।')
    return data


def get_text(files):
    """
    Get text from each file
    """
    with open(files, 'r') as file_name:
        read_data = file_name.read()

    read_data = text_fix(read_data)
    return read_data


def count_freq(word_text, count_dictionary, count_total):
    """
    Counts frequency of each letter
    """
    for words in word_text:
        word_length = len(words)
        i, j = 0, 0
        while i < word_length:
            j += 1
            while j < word_length:
                if SEMIVOWELS_MODE:
                    if words[j] in DEPENDENTS + NONJOINERS:
                        j += 1
                        break
                if words[j] in JOINERS:
                    j += 1
                    continue
                break
            char = words[i:j]
            i = j

            # Check key in dict
            if char in count_dictionary:
                # If it exists, increment
                count_dictionary[char] += 1
            else:
                # If it doesn't, add to dictionary and set to 1
                count_dictionary[char] = 1

            # Keep total count
            count_total += 1

    return count_dictionary, count_total


def main(argv):
    """
    Checks arguments
    """
    if (len(argv) != 2):
        print("Usage: " + os.path.basename(__file__) + " <Folder>")
    else:
        count_dictionary = dict()
        count_total = 0

        for files in os.listdir(argv[1]):
            path_name = os.path.join(argv[1], files)

            word_text = get_text(path_name).split()

            count_dictionary, count_total = count_freq(
            word_text, count_dictionary, count_total)

        count_list = sorted(count_dictionary.items(),
                            key=lambda x: x[1], reverse=True)

        print ('Symbol\t\tFrequency (%)\n-----------------------------')
        for symbols, count in count_list:
            print ('{}\t\t{:g}'.format(symbols, (100*count/count_total)))


if __name__ == '__main__':
    main(sys.argv)
