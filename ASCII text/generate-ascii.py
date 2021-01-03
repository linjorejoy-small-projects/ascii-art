import json


if __name__ == "__main__":

    options = []
    json_file = None
    with open("ASCII text/file-list.json") as file_list:

        json_file = json.load(file_list)
        [options.append(font) for font in json_file.keys()]
    print(json_file)

    font_index = 0
    font_style = ''
    while(True):
        print("\n\nFonts Present")
        print("-"*10)
        [print(i, " : ", options[i]) for i in range(len(options))]
        font_index = int(input("\n\nSelect The Font : "))
        
        try:
            font_style = options[font_index]
            break
        except Exception as r:
            print("Wrong Index. Try again")
    
    json_font = ''
    with open(json_file[font_style]['json']) as json_file:
        json_font = json.load(json_file)

    text = input("Write your text : ")

    print("\n\nCopy from here")

    print("\n```")
    
    print("\n".join([json_font[char]['value'] for char in text]))

    print("```")