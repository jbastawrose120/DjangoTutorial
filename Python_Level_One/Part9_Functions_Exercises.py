#####################################
#### PART 9: FUNCTION EXERCISES #####
#####################################


# Complete the tasks below by writing functions! Keep in mind, these can be
# really tough, its all about breaking the problem down into smaller, logical
# steps. If you get stuck, don't feel bad about having to peek to the solutions!

#####################
## -- PROBLEM 1 -- ##
#####################

# Given a list of integers, return True if the sequence of numbers 1, 2, 3
# appears in the list somewhere.

# For example:

# arrayCheck([1, 1, 2, 3, 1]) → True
# arrayCheck([1, 1, 2, 4, 1]) → False
# arrayCheck([1, 1, 2, 1, 2, 3]) → True
print("PROBLEM 1__________________________________________")
def arrayCheck(nums):
    # CODE GOES HERE
    listToCheck = [1,2,3]
    for i in range(0, len(nums)+1):
        if i + 3 <= len(nums):
            if listToCheck == nums[i:i+3]:
                return True

    return False


arr1 = [1,1,2,3,1]
arr2 = [1,2,2,3,1,3,3]
arr3 = [1,1,2,1,2,3]

print(arrayCheck(arr1))
print(arrayCheck(arr2))
print(arrayCheck(arr3))

#####################
## -- PROBLEM 2 -- ##
#####################

# Given a string, return a new string made of every other character starting
# with the first, so "Hello" yields "Hlo".

# For example:

# stringBits('Hello') → 'Hlo'
# stringBits('Hi') → 'H'
# stringBits('Heeololeo') → 'Hello'

print('\n\n\nPROBLEM 2__________________________________________')
def stringBits(str):
  # CODE GOES HERE
  return str[::2]

print(stringBits('Hello'))
print(stringBits('Hi'))
print(stringBits('Heeololeo'))


#####################
## -- PROBLEM 3 -- ##
#####################

# Given two strings, return True if either of the strings appears at the very end
# of the other string, ignoring upper/lower case differences (in other words, the
# computation should not be "case sensitive").
#
# Note: s.lower() returns the lowercase version of a string.
#
# Examples:
#
# end_other('Hiabc', 'abc') → True
# end_other('AbC', 'HiaBc') → True
# end_other('abc', 'abXabc') → True

print('\n\n\nPROBLEM 3__________________________________________')
def end_other(a, b):
  # CODE GOES HERE
  if a.upper().find(b.upper()) > 0:
      return True
  elif b.upper().find(a.upper()) > 0:
      return True
  else:
      return False

print(end_other('Hiabc', 'abc'))
print(end_other('AbC', 'HiaBc'))
print(end_other('abc', 'abXabc'))

#####################
## -- PROBLEM 4 -- ##
#####################

# Given a string, return a string where for every char in the original,
# there are two chars.

# doubleChar('The') → 'TThhee'
# doubleChar('AAbb') → 'AAAAbbbb'
# doubleChar('Hi-There') → 'HHii--TThheerree'
print('\n\n\nPROBLEM 4__________________________________________')

def doubleChar(str):
  # CODE GOES HERE
  strAsList = list(str)
  result = []
  for i in range(0,len(strAsList)):
      result.append(strAsList[i])
      result.append(strAsList[i])
  return ''.join(result)

print(doubleChar('The'))
print(doubleChar('AAbb'))
print(doubleChar('Hi-There'))

#####################
## -- PROBLEM 5 -- ##
#####################
print('\n\n\nPROBLEM 5__________________________________________')
# Read this problem statement carefully!

# Given 3 int values, a b c, return their sum. However, if any of the values is a
# teen -- in the range 13-19 inclusive -- then that value counts as 0, except 15
# and 16 do not count as a teens. Write a separate helper "def fix_teen(n):"that
# takes in an int value and returns that value fixed for the teen rule.
#
# In this way, you avoid repeating the teen code 3 times (i.e. "decomposition").
# Define the helper below and at the same indent level as the main no_teen_sum().
# Again, you will have two functions for this problem!
#
# Examples:
#
# no_teen_sum(1, 2, 3) → 6
# no_teen_sum(2, 13, 1) → 3
# no_teen_sum(2, 1, 14) → 3

def no_teen_sum(a, b, c):
  # CODE GOES HERE
  if fix_teen(a):
      a = 0
  if fix_teen(b):
      b = 0
  if fix_teen(c):
      c = 0

  return a + b + c


def fix_teen(n):
  # CODE GOES HERE
  if n == 13 or n == 14 or (n > 16 and n < 20):
      return True
  else:
      return False


print(no_teen_sum(1, 2, 3))
print(no_teen_sum(2, 13, 1))
print(no_teen_sum(2, 1, 14))
#####################
## -- PROBLEM 6 -- ##
#####################
print('\n\n\nPROBLEM 6__________________________________________')
# Return the number of even integers in the given array.
#
# Examples:
#
# count_evens([2, 1, 2, 3, 4]) → 3
# count_evens([2, 2, 0]) → 3
# count_evens([1, 3, 5]) → 0

def count_evens(nums):
  # CODE GOES HERE
  result = 0
  for num in nums:
      if num % 2 == 0:
          result += 1
  return result


print(count_evens([2, 1, 2, 3, 4]))
print(count_evens([2, 2, 0]))
print(count_evens([1, 3, 5]))
