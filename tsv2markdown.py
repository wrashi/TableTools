#!/usr/bin/env python3
import pandas as pd
import pyperclip as pc # copy = copy to clipboard / paste = paste from clipboard

##  Read the clipboard
result = pd.read_clipboard(sep='\t')
##  Replace NA with blank
result = result.fillna('')
##  Output the results
output = f"\n{result.to_markdown(index=False)}\n"
##  Put results on clipboard
pc.copy(output)
##  Show the world!
print(output)
