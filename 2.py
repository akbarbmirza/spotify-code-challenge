# Question 2 -- decodeString(s): 
#   Given an encoded string, return its corresponding decoded string. 
#   The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is repeated exactly k times.
#   Note: k is guaranteed to be a positive integer. 
#   For s = "4[ab]", the output should be decodeString(s) = "abababab" 
#   For s = "2[b3[a]]", the output should be decodeString(s) = "baaabaaa"

# constant used in decodeString
DIGITS = '0123456789'

def decodeString(s):
    # determine if string has an encoded string
    open_bracket = s.find('[')

    # if it does...
    if open_bracket != -1:
        # break string into two parts
        # left, everything before the first '['
        left = s[:open_bracket]
        # encoded, everything within that set of square brackets
        encoded = s[open_bracket + 1:-1]
        # print("open_bracket: %s" % open_bracket)
        # print("left: %s" % left)
        # print("encoded: %s" % encoded)
        
        # process left side, since it may be characters and a number
        output = ""
        # string that'll be parsed to find int k
        k_str = ""

        # separate text from k (if it exists on left side)
        for char in left:
          if char not in DIGITS:
            output += char
          else:
            k_str += char

        # at this point, we can parse k_str into an int
        k = int(k_str)

        # call decodeString() recursively, until nothing left to decode
        return output + (k * decodeString(encoded))
    # otherwise, string is already decoded
    else:
      return s

# Test Cases

print(decodeString("4[ab]")) # => "abababab"
print(decodeString("2[b3[a]]")) # => "baaabaaa"
print(decodeString("1[abc3[xyz]]")) # => "abcxyzxyzxyz"