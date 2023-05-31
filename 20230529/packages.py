import cleantext


clean_text = cleantext.clean_words(
    'Some_WoRdS12_TO_52_clean',
    lowercase=True,
    numbers=True
)

print(clean_text)
