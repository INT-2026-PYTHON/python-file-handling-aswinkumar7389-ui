"""
## 2. Alphabets That Never Appear Back-to-Back  *(Medium)*

=================================================
ALPHABETS NEVER IN SEQUENCE
=================================================

Problem Statement:
Read the text file `sowpods.txt` and PRINT
every alphabet letter that:
   - APPEARS at least once in the words of
     the file, AND
   - NEVER appears TWICE IN A ROW (back-to-back)
     in ANY word of the file.

Letters that never appear in the file at all
should NOT be in the answer. Letters that
appear back-to-back at least once (like the
'u' in "vacuum") should also be excluded.

-------------------------------------------------
Input Example (sowpods.txt sample):
aardvark
hello
buzz
moon
puppy

Output Example:
Letters that never appear back-to-back:
['b', 'd', 'e', 'h', 'k', 'm', 'n', 'r', 'u', 'v', 'y']

-------------------------------------------------
Explanation:
Letters seen anywhere in the sample:
   aardvark -> a, r, d, v, k
   hello    -> h, e, l, o
   buzz     -> b, u, z
   moon     -> m, o, n
   puppy    -> p, u, y
   seen    = {a, b, d, e, h, k, l, m, n, o,
              p, r, u, v, y, z}

Letters that ever appear back-to-back:
   aa (aardvark), ll (hello), zz (buzz),
   oo (moon),     pp (puppy)
   doubled = {a, l, z, o, p}

Answer = seen - doubled
       = {b, d, e, h, k, m, n, r, u, v, y}
Sorted -> ['b', 'd', 'e', 'h', 'k', 'm', 'n',
           'r', 'u', 'v', 'y']
=================================================

"""
# Open the file and read all words
with open("file_reading_practice/sowpods.txt", "r") as f:

    words = [line.strip().lower() for line in f]

seen = set()      # letters that appear anywhere
doubled = set()   # letters that appear twice in a row

# Go through each word
for word in words:
    for i in range(len(word)):
        seen.add(word[i])  # mark letter as seen
        # check if the same letter repeats
        if i < len(word) - 1 and word[i] == word[i+1]:
            doubled.add(word[i])

# Final answer = letters seen but not doubled
result = sorted(seen - doubled)

print("Letters that never appear back-to-back:")
print(result)