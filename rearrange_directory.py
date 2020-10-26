import os
import shutil

base_path = input("Enter Base path : ")
substrings_to_be_match = input("Enter list of substrings in File Name to look for (case insensitive) (* for any):").split()
match_all = input("Match All substrings (y) or any one (n) ?")
match_all = match_all[0]
dest_path = input("Enter Destination path : ")

type_of_extentions = input("Enter Type of Files (all, text, video, music, images) :")
acceptable_extentions = []
if (type_of_extentions == "all" or type_of_extentions == "text"):
	acceptable_extentions.extend(["pdf", "txt", "docs", "docx", "ppt", "pptx", "doc", "pages", "keynote"])
if (type_of_extentions == "all" or type_of_extentions == "video"):
	acceptable_extentions.extend(["mp4", "mov", "mkv", "wmv", "flv", "avi"])
if (type_of_extentions == "all" or type_of_extentions == "music"):
	acceptable_extentions.extend(["mp3", "wav", "wma", "aac"])
if (type_of_extentions == "all" or type_of_extentions == "images"):
	acceptable_extentions.extend(["png", "jpg", "jpeg", "gif"])

files = os.listdir(base_path)


def has_substring(list_substring, base_string):
    found_a_match = False
    if (list_substring[0] == '*'):
    	return True
    for substring in list_substring:
        if match_all.lower() == 'y' and substring.lower() not in base_string.lower():
            return False
        elif match_all.lower() == 'n' and substring.lower() in base_string.lower():
            return True

    if (match_all.lower() == 'y'):
        return True
    return False

def has_acceptable_extention(file):
    extention = os.path.splitext(file)
    return extention[1][1:] in acceptable_extentions

def is_hidden(file_name):
	return file_name[0] == '.'

def make_dir(path):
	if (not os.path.exists(path)):
		os.makedirs(path)

def find_files(search_path):
    files = os.listdir(search_path)
    for file_name in files:
        file_path = os.path.join(search_path, file_name)
        if (os.path.isdir(file_path)):
            find_files(file_path)
        elif (has_substring(substrings_to_be_match, file_name) and
              has_acceptable_extention(file_path) and
              not is_hidden(file_name)):
        			make_dir(dest_path)
        			if (not os.path.exists(os.path.join(dest_path, file_name))):
        				shutil.move(file_path, dest_path)
        			print("Moving ", file_name)


find_files(base_path)