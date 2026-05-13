def is_anagram(str1, str2):
    # Optional: Normalize by removing spaces and converting to lowercase
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()
    
    # Anagrams must be the same length
    if len(str1) != len(str2):
        return False
        
    return sorted(str1) == sorted(str2)

# Example usage
print(is_anagram("Listen", "Silent"))  # Output: True
