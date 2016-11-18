# Chrome Bookmarks for Windows Run
This parses Chrome bookmarks in Windows, creates useful run commands out of them.

## Example usage
<code>python main.py C:\Users\zengin\bookmarks</code>

This creates (or replaces):

<code>C:\Users\zengin\bookmarks\b.bat</code>

If you add this bat file into your <code>PATH</code> environment variable, batch file becomes available in Windows Run.


For example if you had github as bookmark name for https://github.com, then type

<code>b github</code>

in Windows Run command prompt. This will open https://github.com in Chrome.

## Optional browser parameter:

You can optionally pass a browser parameter to script:

<code>python main.py C:\Users\zengin\bookmarks edge</code>

This will create the same b.bat file, but this time to launch Edge instead of Chrome.
