## Mock Test

### A Python program acting as a Mock Test using OOP and functions to access a .txt file with questions for the AWS Cloud Practitioner Test. 

#### Features:
* It accesses **'questions.txt'**.
* Lets user choose how many questions they would like to answer. 
* Displays their score at the end.

<br>

### Turning program into .exe

1. Installing pyinstaller:

```shell
python -m pip install pyinstaller
```

2. Running the command from current folder:

```shell
pyinstaller --onefile --add-data="questions.txt;." mock_test_app.py
```

#### Possible blockers:

* it might not access the .txt file unless you run it directly from the terminal:
```shell
./dist/mock_test_app.exe  
```
* In that case, you need to add this code to your script:

```python
import sys, os
os.chdir(sys._MEIPASS)
```