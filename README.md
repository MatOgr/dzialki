# Dzialki
Simple python program processing xml files. New formats and labels to process can be added to the file `format.xml`, includes `aaa` `nas`, currently <br/>
**Files `format.xml` and `main.py` need to be next to each other (or parsing path of `format.xml` has to be changed inside `main.py`)**

## Modules used:
+ os
+ sys
+ argparse
+ xml.etree.ElementTree

## Running the programm 

Python required, run commands from terminal in format below

+ Rigth from the terminal <br/>
`[python] main.py path_to_file file_format` - [python] whether you run from 'clean' terminal or python venv

Example: `main.py ./my_xml_xyzformat.xml xyz`
