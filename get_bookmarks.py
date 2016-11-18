import os

def read_file_into_list (file_path):
	f = open (file_path, "r")
	lines = f.readlines()
	f.close()
	return lines;

def get_bookmark_dict ():
	bookmark_path = os.getenv("LOCALAPPDATA") + "\\Google\\Chrome\\User Data\\Default\\Bookmarks"
	lines = read_file_into_list(bookmark_path);

	bookmark_dict = {}
	
	for i in range(len(lines)):
		if lines[i].strip() == '"type": "url",':
			name = lines[i-1].split('"name":')[1].split('"')[1]
			url = lines[i+1].split('"url":')[1].split('"')[1]
			
			# get lines with single word name only
			if " " not in name:
				bookmark_dict[name] = url
			
	return bookmark_dict
			