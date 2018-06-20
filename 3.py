# Question 3 -- changePossibilities(amount, denominations): 
#   Write a function that, given an amount of money and an array of coin denominations, computes the number of ways to make the amount of money with denoms of the available denominations. 
#   Example: for amount=4 (4) and denominations=[1,2,3] (1¢, 2¢ and 3¢), your program would output 4—the number of ways to make 4¢ with those denominations: 
#   1¢, 1¢, 1¢, 1¢
#   1¢, 1¢, 2¢
#   1¢, 3¢
#   2¢, 2¢

def findNumOfResults(amount, denoms, results):
    if amount == 0:
        return 1
    if amount < 0 or not denoms:
        return 0
    key_pair = (amount, len(denoms))
    if key_pair not in results:
        results[key_pair] = findNumOfResults(amount - denoms[-1], denoms, results) + findNumOfResults(amount, denoms[:-1], results)
    return results[key_pair]
    
def changePossibilities(amount, denominations):
    return findNumOfResults(amount, denominations, {})

# Test Cases

print(changePossibilities(4, [1,2,3])) # => 4
print(changePossibilities(0, [1,2,3])) # => 1
print(changePossibilities(4, [])) # => 0
print(changePossibilities(5, [1, 2, 3])) # => 5
