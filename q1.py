#write a programm to count vowels and consonants present in input string
def q1(input_string):
    vowels = 'aeiouAEIOU'
    vowel_count = 0
    consonant_count = 0
    
    for char in input_string:
        if char in vowels:
            vowel_count += 1
        elif ('A' <= char <= 'Z') or ('a' <= char <= 'z'):
            consonant_count += 1
    
    return vowel_count, consonant_count

def main():
    input_string = input("Enter a string: ")
    vowel_count, consonant_count = q1(input_string)
    
    print("Number of vowels:", vowel_count)
    print("Number of consonants:", consonant_count)


main()
