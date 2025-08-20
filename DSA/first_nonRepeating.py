def first_nonReapeating(str):

    freq = {}

    # Step 1: Count frequency
    for char in str:

        if char in freq:
            freq[char] +=1

        else:
            freq[char] = 1

    # Step 2: Find first character with frequency 1
    for char in str:

        if freq[char] == 1:
            return char
        
    return None


string = "zxabcedabecdabcd"
a = first_nonReapeating(string)
print(a)