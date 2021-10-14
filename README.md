# touch for windows
Creates files for windows like the basic functionality of the Unix command touch.  

Eventually I plan on adding all of the capabilities of touch to windows but this it here for now. I made it a exe file using pyinstaller and added it to my python directory so I can use it in any dir and with out needing the .exe at the end of touch.

## pyinstaller tut
```
pyinstaller --onefile touch.py
```
copy the file created into your python location and your good to go

## But you can do that with normal windows commands
Yes you can but look at the difference in command length.

Normal Windows
```
type nul >> "file.txt"
```
this adds a nul char in the file and you can't remove it so it breaks python scripts

Touch For Windows
```
touch <filename>
```
As you can see less typing plus you can do as many files at once as you like

