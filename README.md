# TableTools
Two Python scripts that use `pyperclip` and `pandas` to work with tabular data found (often on the web).
Both dependencies are cross-platform (Mac, Linux & Windows) so this should work wherever you do.

##  Use Case
You find data and it's not in the form you want.
For example, you copy some table data that looked like this

| BUY | Aug 17, 2022 | 8935141660703884562 | BTC | BTC-CAD | BTC.1 | $30,292.00 | CAD |
|:--- |:------------ | -------------------:|:--- |:------- |:----- |:---------- | --- |
| BUY | Aug 17, 2022 | 8935141660704765460 | BTC | BTC-CAD | BTC   | $30,500.00 | CAD |

but when you paste it looks like this:

```
BUY
Aug 17, 2022
8935141660703884562
BTC
BTC-CAD
BTC
$30,292.00
…
```

Or, the data is tab separated (TSV format) and you want to paste it into your Markdown notes.

###   Usage

Usage should be straightforward, but more details can be found on [this blog post](https://wpenner.com/en/blog/dealing-with-table-data).
