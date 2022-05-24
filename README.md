# PDF Merger

This is a very simple gui program to merge two or more 
pdf files into one.<br>

## Requirements

1. Python3.x
2. virtualenv (optional)

## Setup

1. Clone this repository and go inside the project. Or copy paste the below to your bash/powershell terminal<br>

```bash
git clone https://github.com/s-shifat/PDF-Merger.git; cd PDF-Merger
```

2. _(OPTIONAL)_ If you have virtualenv installed then do Otherwise directly go to #3:

      2.1 Create a virtual environment
    ```bash
    virtualenv venv
    ```
     2.2.A If you're on windows:
    ```powershell
    .\venv\Scripts\activate.PS1
    ```
     2.2.B If you're on Linux/Mac:
    ```bash
      source ./venv/bin/activate
    ```
3. Install dependencies:

```bash
pip install -r requirements.txt
```
All set now you're good to go.

## Run The Script

Simply do:
```bash
python3 source/main_gui.py
```



 I have also provided two sample pdfs in directory [samples](https://github.com/s-shifat/mrg-pdf/tree/main/samples) If you need to test them<br>
###### Also if you need, feel free to clone the repository to modify the source code.

