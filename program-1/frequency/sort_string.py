from collections import Counter

def sort_string_by_frequency(s):
  # Count the frequency of each character in the string
    freq = Counter(s)
    # Sort the characters by frequency (most frequent first)
    sorted_chars = sorted(freq, key=freq.get, reverse=True)
    # Build the sorted string by repeating each character by its frequency
    sorted_string = ''.join(char * freq[char] for char in sorted_chars)
    return sorted_string

# Example usage:
s = "hello world"
sorted_s = sort_string_by_frequency(s)
print(sorted_s)
