from typing import List, Tuple

def find_words_with_max_vowel(text: str) -> Tuple[str, float]:

    vowels = set("aeiouyAEIOUYауеыоэяиюАУЕЫОЭЯИЮ")
    
    words = []
    current_word_chars = []
    
    for char in text:
        if char.isalpha(): 
            current_word_chars.append(char)
        else:
            if current_word_chars:
                words.append("".join(current_word_chars))
                current_word_chars = []
    
    if current_word_chars:
        words.append("".join(current_word_chars))

    if not words:
        return "", 0.0

    max_ratio = -1.0
    best_words = []

    for word in words:
        if not word: 
            continue
            
        vowel_count = sum(1 for char in word if char in vowels)
        ratio = vowel_count / len(word)
        
        if ratio > max_ratio:
            max_ratio = ratio
            best_words = [word]
        elif ratio == max_ratio:
            if max_ratio > 0: 
                best_words.append(word)
                
    result_string = " ".join(best_words)
    return result_string, max_ratio


text = "u i u a a six seven сорок два вот."
print(f"Исходный текст:\n\"{text}\"")

result_words, max_vowel_ratio = find_words_with_max_vowel(text)

print(f"\nСлова с макс. долей гласных: \"{result_words}\"")
print(f"Доля гласных: {max_vowel_ratio:.2%}")