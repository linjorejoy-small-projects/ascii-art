import json
import re

alphabets = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

# LOAD FILE NAMES FROM JSON FILE
with open("ASCII text/file-list.json") as file_list_json:
    file_names = json.load(file_list_json)

    # ITERATE THROUGH FILE NAMES ONE BY ONE
    for k,v in file_names.items():

        # OPEN THE TEXT FILE IN READ MODE
        with open(v['text'], mode='r') as text_file:

            # ALL LINES
            all_of_it = text_file.read()

            # REMOVE STARTING AND ENDING ```
            all_of_it_trimmed= re.sub("[`]+","",all_of_it)

            # SPLIT THE REMAINING INTO LIST
            all_of_it_split = re.split("[\n]{2,}[ ]*[\n]{2,}",all_of_it_trimmed)

            this_dictionary = dict() # TO STORE KEY AS ALPHABET AND VALUE AS THE STRING

            # ITERATE THROUGH THE KEY VALUE PAIRS AND ADDING THEM TO DICTIONARY
            for key, value in zip(alphabets, all_of_it_split):
                this_dictionary[key] = value

            # WRITING THE CREATED DICTIONARY TO A JSON FILE
            with open(v['json'],'w') as json_file:
                json.dump(this_dictionary, json_file, indent = 4, sort_keys=True)
                
