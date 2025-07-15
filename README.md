# MD Table Gen
A Python Library for Easily Generating Markdown Tables

## Purpose
This is a library to help you generate tables in markdown.  

### What it Does Do
Generates markdown tables given column headers and row data

### What it Does Not Do
Pretty print the tables

## How To Use It
 1. Import it an instantiate it by giving it the column names
 2. Add the rows
 3. Generate the text

### Can I get an example?
Yes, you can!
```
 m = MarkdownTableGenerator(["h1", "h2", "h3"])
     m.add_row(["11", "12", "13"])
     m.add_row(["21", "22", "23"])
     m.add_row(["31", "32", "33"])

     print(m.make_table_string())
```

