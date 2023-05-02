
def romanToInt(s: str) -> int:
    numValues = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    totalSum = 0
    i = 0

    for x in range(len(s)):
        if (i != (len(s) - 1)) and (numValues[s[i]] < numValues[s[i+1]]):
            totalSum -= numValues[s[i]]
        else:
            totalSum += numValues[s[i]]
        
        i += 1

    return totalSum

def main():
    s = input("Enter all caps roman numerals: ")
    intAnswer = romanToInt(s)
    print("\nYour roman numeral value in integer form is:", intAnswer, "\n")

main()