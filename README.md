
# Charles Session Parser

This is a simple parser for Charles session file base on Python.
Using the parser to format Charles session file to a simple elegant txt file.


## Usage

1. Export Charles session to json file
    1. Right-click on the session you selected and select "Export..."
    2. **Make sure the Format is "JSON Session File"**
    3. Save the file with extension name ".chlsj"
2. Run the parser

```python
python3 [path-to/]parser.py path-to-chlsj-file [out-put-file-name]
```
