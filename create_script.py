def create_script_string(bookmarks, browser = "chrome"):
	if len(bookmarks) is 0:
		return ""

	browser_cmd_map = {"edge" : "microsoft-edge:", "firefox": "firefox ", "chrome" : "chrome ", "ie": "iexplore "}
	browser_cmd = browser_cmd_map[browser]
	
	file_start = '''GOTO :URL_%1
exit
'''

	goto_format_string = ''':URL_{}
start {}{}
exit
'''
	
	script = file_start
	for name, url in bookmarks.iteritems():
		script += goto_format_string.format(name, browser_cmd, url)
	
	return script