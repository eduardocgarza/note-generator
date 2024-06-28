# Note Generator

## How It Works

- Input a list of strings in the `strings` variable in `run.py`
- Name the strings as the chapter names
- Configure the `run.py` to execute
- The output will be a set of chapter files for your textbook notes

## Example

```bash
$ python3 -m venv venv
$ source venv/bin/activate

$ python3 run.py
```

## Output
└── chapters/
    ├── Chapter 1 - Introduction.docx
    ├── Chapter 2 - Getting Started.docx
    ├── Chapter 3 - Advanced Techniques.docx
    └── Chapter 4 - Conclusion.docx
```
