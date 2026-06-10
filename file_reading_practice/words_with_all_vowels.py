"""
## 3. Words Containing All Five Vowels  *(Medium)*

=================================================
WORDS WITH ALL VOWELS
=================================================

Problem Statement:
Read the text file `sowpods.txt` and PRINT
every word that contains ALL FIVE vowels
('a', 'e', 'i', 'o', 'u') at least once.
The order of the vowels does NOT matter, and
the check should be case-insensitive.


-------------------------------------------------
Input Example (sowpods.txt sample):
education
sequoia
facetious
hello
audio
unequivocal

Output Example:
education
sequoia
facetious
unequivocal
Total words with all vowels: 4

-------------------------------------------------
Explanation:
- "education" contains a, e, i, o, u -> yes
- "sequoia"   contains a, e, i, o, u -> yes
- "facetious" contains a, e, i, o, u -> yes
- "hello"     missing a, i, o, u     -> no
- "audio"     missing e               -> no
- "unequivocal" contains a,e,i,o,u   -> yes
=================================================

"""
# Find words with all five vowels (a, e, i, o, u) without issubset

# Open the file
with open("file_reading_practice/sowpods.txt", "r") as f:
    words = [line.strip().lower() for line in f]

count = 0  # counter for words that qualify

# Check each word manually
for word in words:
    if ("a" in word and
        "e" in word and
        "i" in word and
        "o" in word and
        "u" in word):
        print(word)
        count += 1

print("Total words with all vowels:", count)