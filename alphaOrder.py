#! python3
# A program to print the longest substring of user's word in which the 
# letters occur in alphabetical order.

s = input('Enter a word:')
long = ''
longest = ''
if len(s) == 1:
    longest =s
for i in range(len(s)-1):
    if s[i] < s[i+1]:
        long += s[i]
        longest = long
        if i == len(s) - 2:
            long += s[i+1]
    else:
        long += s[i]
        if len(long)> len(longest):
            longest = long
        long = ''
print('Longest substring in alphabetical order is: %s' %longest)