# Longest Substring Without Repeating Characters
# def longest_substring(string):
#     c = ""
#     l = []
#     for i in string:
#         # c.append(i) 
#         if c!=i:
#             l.append(i) 
#         elif c ==i:
#             c==i
#     return c
# Given 



        # c =i 
        # if c!=i:
        #     l[0].append(i)
        # elif c==i:
        #     c=i
        
# given a string s, return the longest 
# palindromic
 
# substring
#  in s.
# def palindromic(a):
#     c = ""
#     for i in a:
#         c+=i


        
#         # if c!=i:
#         #     # c ==i 

#         #     c += i
#         # elif c ==i:
#         #         c+=i

                
        
#     return c
            




# a = "caaa"

# result =palindromic(a)
# print(result)
# def longest_substring_without_repeating(s):
#     longest = 0
#     substring = ""

#     for char in s:
#         if char in substring:
#             substring = substring[substring.index(char) + 1:]
#         substring += char
#         longest = max(longest, len(substring))
    
#     return longest,substring

# # Example usage
# s = "abcabcbb"
# print(longest_substring_without_repeating(s))
        




# string = "abcabcbc"
# result=longest_substring(string)
# print(result)


# def longest_substring_without_repeating(s):
#     longest = 0
#     start = 0

#     for end in range(len(s)):
#         for i in range(start, end):
#             if s[i] == s[end]:
#                 start = i + 1
#                 break
#         longest = max(longest, end - start + 1)
    
#     return longest

# # Example usage
# s = "abcabcbb"
# print(longest_substring_without_repeating(s))

# Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

# Symbol       Value
# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M             1000

# def roman(dct,target):
#     for x in target:
        
        



# dct={"I":1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
# target = 'III'

# print(roman(dct,target))
    
# def roman_to_int(roman):
#     roman_values = {
#         'I': 1, 'V': 5, 'X': 10, 'L': 50,
#         'C': 100, 'D': 500, 'M': 1000
#     }
#     total = 0
#     prev_value = 0

#     for char in reversed(roman):  # Process from right to left
#         value = roman_values[char]
#         if value < prev_value:
#             total -= value  # Subtract if smaller value precedes a larger value
#         else:
#             total += value  # Otherwise, add the value
#         prev_value = value

#     return total

# # Example usage
# roman_numeral = "MCMXCIV"  # Example: 1994
# print(roman_to_int(roman_numeral))  # Output: 1994


# Write a function to find the longest common prefix string amongst an array of strings.

# If there is no common prefix, return an empty string "".

# def longest_common_function_prefix(lst):
#     y = []
#     xx=''
#     for x in lst:
#         # print(x)
#         for i in range(len(x)):
#             # print(i)
#             for j in range(i+1,len(x)):

#                 if x[i]==x[j]:
#                     y.append(x[i])
#                     break
#                 # continue
#     return y 
            
# lst = ['helo','heo',"heluuu"]
# print(longest_common_function_prefix(lst))


# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.

# def  containing_char(char):
#     if char=="()":
#         return True
#     else:
#         return False
    



# char = "[()]}"
# print(containing_char(char))

# Find the Index of the First Occurrence in a String
# def Occurrence(main, find ):
#     if find in main:
#         return 0
#     else:
#         return -1
# main = "govind"
# find =  "gov"
    
print(Occurrence(main , find))
def Occurrence(main, find ):
    if find in main:
        return 0
    else:
        return -1
main = "govind"
find =  "gov"
    
print(Occurrence(main , find))