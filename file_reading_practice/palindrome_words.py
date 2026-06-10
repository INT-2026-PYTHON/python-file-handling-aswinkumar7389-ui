"""
## 4. Find All Palindrome Words  *(Medium)*

=================================================
PALINDROME WORDS
=================================================

Problem Statement:
Read the text file `sowpods.txt` and PRINT
every PALINDROME word (a word that reads the
same forwards and backwards).

Write a helper FUNCTION called `is_palindrome`
that takes a single word and returns True if
it is a palindrome, else False. Pass every
word in the file to this function ONE AT A
TIME.

-------------------------------------------------
Input Example (sowpods.txt sample):
level
radar
hello
noon
civic
python
deified
racecar
banana

Output Example:
level
radar
noon
civic
deified
racecar
Total palindromes: 6

-------------------------------------------------
Explanation:
- "level"    reversed -> "level"   -> palindrome
- "radar"    reversed -> "radar"   -> palindrome
- "hello"    reversed -> "olleh"   -> not
- "noon"     reversed -> "noon"    -> palindrome
- "civic"    reversed -> "civic"   -> palindrome
- "python"   reversed -> "nohtyp"  -> not
- "deified"  reversed -> "deified" -> palindrome
- "racecar"  reversed -> "racecar" -> palindrome
- "banana"   reversed -> "ananab"  -> not
=================================================

"""
# Helper function to check palindrome
def is_palindrome(word):
    # A word is palindrome if it equals its reverse
    return word == word[::-1]

# Open the file
with open("C:/Users/aswin/OneDrive/Documents/GitHub/python-file-handling-aswinkumar7389-ui/file_reading_practice/sowpods.txt", "r") as f:
    words = [line.strip().lower() for line in f]

count = 0  # keep track of total palindromes

# Check each word one at a time
for word in words:
    if is_palindrome(word):   # call the helper function
        print(word)           # print the palindrome
        count += 1            # increase counter

print("Total palindromes:", count)
