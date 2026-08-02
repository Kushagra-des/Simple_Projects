# File Splitter Utility using Python

## Description

A command-line Python utility that splits large CSV or TXT files into multiple smaller files based on a user-defined number of rows. The project automates file partitioning and stores the output in a dedicated directory.

---

## Features

- Split CSV files
- Split TXT files
- User-defined split size
- Automatic output directory creation
- Handles remaining rows automatically
- Command-line execution

---

## Concepts Used

- Python Classes
- Object-Oriented Programming
- Command-Line Arguments
- File Handling
- Directory Management
- Pandas DataFrame
- Exception-free Program Flow

---

## Project Structure

```
file-splitter-python/
│
├── input.csv
├── file_splitter.py
├── file_split/
│   ├── split_file1.csv
│   ├── split_file2.csv
│   └── ...
└── README.md
```

---

## Installation

```bash
git clone <repository-url>

cd file-splitter-python

pip install pandas
```

---

## How to Run

```bash
python file_splitter.py input.csv 100
```

Example:

```bash
python file_splitter.py employees.csv 500
```

This creates:

```
file_split/
    split_file1.csv
    split_file2.csv
    split_file3.csv
```

---

## Example Output

```
Input File:
employees.csv

Rows per file:
500

Output:
file_split/
    split_file1.csv
    split_file2.csv
    split_file3.csv
```

---

## Future Improvements

- Progress bar
- Input validation
- Support Excel files
- Support JSON files
- Preserve CSV headers
- Logging
- Custom output directory
- Custom output filename
- GUI version
- Unit testing

---

---

## License

MIT License
