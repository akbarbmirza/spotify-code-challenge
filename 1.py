# Question 1 -- sortByStrings(s,t):
#   Sort the letters in the string s by the order they occur in the string t. 
#   You can assume t will not have repetitive characters. 
#   For s = "weather" and t = "therapyw", the output should be sortByString(s, t) = "theeraw".
#   For s = "good" and t = "odg", the output should be sortByString(s, t) = "oodg".

def sortByStrings(s, t):
    # hold a dictionary to hold the # of times a letter appears
    letterCounts = {}
    # collect letters in string s
    for letter in s:
        if letter in letterCounts:
            letterCounts[letter] += 1
        else:
            letterCounts[letter] = 1

    output = ""

    # iterate through letters in t to establish our order
    for letter in t:
        if letter in letterCounts:
            output += letter * letterCounts[letter]
    
    return output

# Test Cases
print(sortByStrings("weather", "therapyw")) # => "theeraw"
print(sortByStrings("good", "odg")) # => "oodg"
print(sortByStrings("helloworld", "wrolhed")) # => "wroolllhed"