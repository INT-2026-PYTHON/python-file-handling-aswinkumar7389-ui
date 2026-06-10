"""
## 5. Longest Palindrome in the File  *(Hard)*

=================================================
LONGEST PALINDROME
=================================================

Problem Statement:
Read the text file `sowpods.txt` and find the
LONGEST PALINDROME word in the file.

If multiple palindromes share the maximum
length, print ALL of them.

-------------------------------------------------
Input Example (sowpods.txt sample):
level
radar
noon
civic
deified
racecar
rotator
malayalam

Output Example:
Longest palindrome length: 9
malayalam

-------------------------------------------------
Explanation:
Lengths of the palindromes in the sample:
   level    -> 5
   radar    -> 5
   noon     -> 4
   civic    -> 5
   deified  -> 7
   racecar  -> 7
   rotator  -> 7
   malayalam -> 9
The longest is "malayalam" with 9 characters.
=================================================

"""
with open("file_reading_practice/sowpods.txt","r") as f:
    words = [line.strip().lower() for line in f]
palindromes = []

for word in words:
    if word == word[::-1]:
        palindromes.append(word)
# Find the maximum length
max_len = 0
for p in palindromes:
    if len(p) > max_len:
        max_len = len(p)

# Collect all palindromes with that length
longest = []
for p in palindromes:
    if len(p) == max_len:
        longest.append(p)


print("Longest palindrome length:", max_len)
print("Longest palindrome(s):")
for w in longest:
    print(w)
