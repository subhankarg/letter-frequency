letter-frequency
================

Calculates the frequency of letters for Indic scripts. Currently supports only Bengali and Devanagari scripts. Supports Latin scripts too.

Set SEMIVOWELS_MODE = True to enable including semivowels with consonants
You can add support for other Indic scripts by adding the corresponding DEPENDENTS and JOINERS.

Requirements: Python 3

Usage:
letter_frequency.py "folder name"

folder should contain files in Unicode format

Eg. Letter count for Assamese corpus published in the following paper
http://doi.acm.org/10.1145/2432553.2432566
