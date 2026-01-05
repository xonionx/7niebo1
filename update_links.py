import sys
import os

file_path = sys.argv[1]
# We want to replace href="rezerwacja.html" with the booksy link
# We also want to handle the index.html case separately or just do another replacement

search_text = 'href="rezerwacja.html"'
replace_text = 'href="https://booksy.com/pl-pl/213708_7-niebo-massage-beauty_brwi-i-rzesy_17074_slupca#ba_s=sh_1" target="_blank"'

try:
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    if search_text in content:
        new_content = content.replace(search_text, replace_text)
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Updated {file_path}")
    else:
        print(f"No match in {file_path}")

except Exception as e:
    print(f"Error processing {file_path}: {e}")
