## Mock Test

### A Python program acting as a Mock Test using OOP and functions to access a .txt file with questions for the AWS Cloud Practitioner Test. 

#### Features:
* It accesses **'questions.txt'**.
* Lets user choose how many questions they would like to answer. 
* The order in which the answers for each question is displayed will always be different and randomised.
* The questions will all be randomly chosen and displayed in no particular order, without repeats.
* Program at the end will display the total number of correct answers as well as the score as a percentage.
* Gives the ability to take the quiz multiple times.

<br>

![AltText](preview.png)

### Turning program into .exe, which will run as a separate terminal (no need for any dependencies to run the .exe file):

1. Installing pyinstaller:

```shell
python -m pip install pyinstaller
```

2. Running the command from current folder:

```shell
pyinstaller --onefile --add-data="questions.txt;." mock_test_app.py
```

#### Possible blockers:

* it might not access the .txt file properly unless you run it directly from the terminal:

```shell
./dist/mock_test_app.exe  
```

* In that case, you need to add this code to your script (this will allow opening the .exe file from anywhere, without any need for dependencies):

```python
import sys, os
os.chdir(sys._MEIPASS)
```