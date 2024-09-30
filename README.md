# Openspace-project
First Becode project to make openspace algorithm

## Description

The company moved to a new office in Gent. Its an openspace with 6 tables of 4 seats. As many of you are new colleagues, you come up with the idea of changing seats everyday and get to know each other better by working side by side with your new colleagues. 

This script runs everyday to re-assign everybody to a new seat.

## Repo structure

.
├── src /
    ├──openspace.py
    ├──table.py
    ├──file_utils.py
    ├──__init__.py
    >__pycache__
    >venv
├──.gitignore
├──main.py
├──new_colleagues.csv
├──output.csv
├──README.md

## Usage
1. Clone the repository to your local machine.

2 .To run the script, you can execute the `main.py` file from your command line:

    ```
    python main.py
    ```

3. The script reads your input file (new_colleagues.csv), and organizes your colleagues to random seat assignments. The resulting seating plan is displayed in your console and also saved to an "output.csv" file in your root directory. 

```python
input_filepath = "new_colleagues.csv"
output_filename = "output.csv"

# Creates a list that contains all the colleagues names
names = utils.read_names_from_csv(input_filepath)

# create an OpenSpace()
open_space = OpenSpace()

# assign a colleague randomly to a table
open_space.organize(names)

# save the seat assigments to a new file
open_space.store(output_filename)

# display assignments in the terminal
open_space.display()

## Timeline
This project took two and a half days for completion.

## 📌 Personal Situation
This project was done as part of the AI Boocamp at BeCode.org. 

Connect with me on [LinkedIn](https://www.linkedin.com/in/k-griff/).