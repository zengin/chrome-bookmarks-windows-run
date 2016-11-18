def create_script_string(bookmarks):
	if len(bookmarks) is 0:
		return ""
		
	file_start = '''GOTO :URL_%1
exit
'''

	goto_format_string = ''':URL_{}
start chrome {}
exit
'''
	
	script = file_start
	for name, url in bookmarks.iteritems():
		script += goto_format_string.format(name, url)
	
	return script