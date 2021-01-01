import json
import re
from typing import List

class Charecter:
    """
        To Store details of a charecter
    """

    def __init__(self, key, value=None, index=-1):
        self.key = key
        self.value = value
        self.index = index
        self.length = 0
        self.rows = 0

    def dictionary(self):
        
        return {
            "key" : self.key,
            "value" : self.value,
            "index" : self.index,
            "length": self.length,
            "rows" : self.rows
        }

    def __str__(self):
        return str(self.__dict__())


class CharecterEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, Charecter):
            return o.__dict__

        return super().default(o)



class Font:

    def __init__(self,char_array : List[Charecter] ):
        self.char_array = char_array

    def dictionary(self):
        dictionary = dict()
        for char in self.char_array:
            dictionary[char.key] = char.__dict__()
        return dictionary
        
    def __str__(self):
        return str(self.__dict__())


class FontEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, Font):
            return o.__dict__

        return super().default(o)

if __name__ == "__main__":        

    alphabets = []
    char_array = []



    with open("ASCII text/charecters.json") as char_file:
        chars = json.load(char_file)

        for char in chars['charecters']:
            this_char = Charecter(char)
            char_array.append(this_char)

        alphabets = chars['charecters']

    # LOAD FILE NAMES FROM JSON FILE
    with open("ASCII text/file-list.json") as file_list_json:
        file_names = json.load(file_list_json)

        # ITERATE THROUGH FILE NAMES ONE BY ONE
        for k,v in file_names.items():

            # OPEN THE TEXT FILE IN READ MODE
            with open(v['text'], mode='r', encoding="utf8") as text_file:

                # ALL LINES
                all_of_it = text_file.read()

                # REMOVE STARTING AND ENDING ```
                all_of_it_trimmed= re.sub("[`]+","",all_of_it)

                # SPLIT THE REMAINING INTO LIST
                all_of_it_split = re.split("[\n]{2,}[ ]*[\n]{2,}",all_of_it_trimmed)

                this_dictionary = dict() # TO STORE KEY AS ALPHABET AND VALUE AS THE STRING

                # ITERATE THROUGH THE KEY VALUE PAIRS AND ADDING THEM TO DICTIONARY
                index = 0
                for key, value, char_obj in zip(alphabets, all_of_it_split, char_array):
                    this_dictionary[key] = value
                    char_obj.index = index
                    char_obj.value = value
                    char_obj.length = len(str(char_obj.value))
                    char_obj.rows = str(char_obj.value).count("\n")
                    index += 1

                this_font = Font(char_array)

                # WRITING THE CREATED DICTIONARY TO A JSON FILE AND  STORE AS LIST
                with open(v['json'],'w') as json_file:
                    json_data = json.dumps(this_font.__dict__, default= lambda o: o.__dict__, indent=4)
                    json.dump(this_font.__dict__, default= lambda o: o.__dict__, indent=4,fp=json_file)


                # # WRITING THE JSON FONT OBJECT TO JSON FILE
                # with open(v['json-as-list'],'w') as json_file:
                #     # json_data = json.dumps(this_font.__dict__, default= lambda o: o.__dict__, indent=4)
                #     json_string = FontEncoder().encode(this_font)
                #     print(json_string)
                #     # print(json_data)
                #     # json.dump(this_font.__dict__, default= lambda o: o.__dict__, indent=4,fp=json_file)
                #     # json.dump(this_font.__dict__, json_file, indent = 4,)
                    

        
