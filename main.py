import get_bookmarks as gb
import create_script as cs
import sys

def show_usage():
	print "usage: python main.py <folder_name>"

if __name__ == "__main__":
	if len(sys.argv) is not 2:
		show_usage()
	else:
		file_path = sys.argv[1] + "\\b.bat"
		bookmarks = gb.get_bookmark_dict()
		script = cs.create_script_string(bookmarks)
		output = open(file_path, "w")
		output.write(script)
		output.close()
	

