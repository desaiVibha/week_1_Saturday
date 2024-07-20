#You are given a string S containing both uppercase and lowercase letters.           
#Note:-   You need to find out the number of vowels in the given string.
def vowel_count(str):
    count = 0     
    vowel = set("aeiouAEIOU") # Creating a set of vowels     
    # Loop to traverse the alphabet
    # in the given string
    for alphabet in str:     
        # If alphabet is present
        # in set vowel
        if alphabet in vowel:
            count = count + 1     
    print("No. of vowels :", count)
string=input("Enter the string to check for number of vowels present in it!")
vowel_count(string)
