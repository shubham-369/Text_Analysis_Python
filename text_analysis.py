def read_txt_file(file_path):
    try:
        with open(file_path, 'r') as file:
            return file.read()
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return None
    except Exception as e:
        print(f"Error reading file: {e}")
        return None
    

def analyze_text(text):
    try:
        # Count words
        word_count = len(text.split())

        # Count lines
        line_count = text.count('\n') + 1  

        # Count characters
        char_count = len(text)

        return word_count, line_count, char_count
    except Exception as e:
        print(f"Error analyzing text: {e}")
        return None

def modify_text(file_path, old_word, new_word):
    try:
        with open(file_path, 'r') as file:
            content = file.read()

        modified_content = content.replace(old_word, new_word)

        with open(file_path, 'w') as file:
            file.write(modified_content)

        print("Modified content written back to the file successfully.")
        return modified_content
    except Exception as e:
        print(f"Error modifying and writing file: {e}")
        print(f"File path: {file_path}")
        return None



file_path = './test.txt'
content = read_txt_file(file_path)

if content:
    print('Content read successfully!')
    print(content)

    analysis_result = analyze_text(content)
    if analysis_result:
        word_count, line_count, char_count = analysis_result
        print("Text Analysis:")
        print(f"Number of words: {word_count}")
        print(f"Number of lines: {line_count}")
        print(f"Number of characters: {char_count}")
    
    old_word = input("Enter the word you want to replace: ")
    new_word = input("Now enter the new word: ")
    modified_content = modify_text(file_path, old_word, new_word)

    if modified_content:
        print("Modified Content:")
        print(modified_content)
