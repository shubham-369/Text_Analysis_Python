def read_txt_file(file_path):
    try:
        with open(file_path, 'r') as file:
            file_content = file.read()
            return file_content
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return None
    except Exception as e:
        print(f"Error reading file: {e}")
        return None
    
file_path = './test.txt'
# content = read_txt_file(file_path)
# if content:
#     print('Content read successfully!')
#     print(content)

def analyze_text(text):
    # Count words
    word_count = len(text.split())

    # Count lines
    line_count = text.count('\n') + 1  # Add 1 for the last line

    # Count characters
    char_count = len(text)

    return word_count, line_count, char_count

# Read content from the text file
file_path = "./test.txt"  # Replace 'sample.txt' with the actual path to your text file
content = read_txt_file(file_path)  # Assuming you have already defined the read_text_file function

if content:
    # Analyze the text
    word_count, line_count, char_count = analyze_text(content)

    # Print the results
    print("Text Analysis:")
    print(f"Number of words: {word_count}")
    print(f"Number of lines: {line_count}")
    print(f"Number of characters: {char_count}")
