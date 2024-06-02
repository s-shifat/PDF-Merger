# PDF Merger

This is a very simple gui program to merge two or more 
pdf files into one.<br>


<!-- [![PDF Merger Demo V1.1](./demo/demo-v1_1.gif)](https://youtu.be/tos6T_d9Wog "PDF Merger V1.1 Demo") -->
<div align="center">
      <a href="https://youtu.be/tos6T_d9Wog">
         <img src="./demo/demo-v1_1.gif" style="width:100%;" />
      </a>
      <br>
      <i><a href="https://youtu.be/tos6T_d9Wog">Watch Demo on YouTube</a></i>
</div>


<!-- [Watch Demo at YouTube](https://youtu.be/tos6T_d9Wog) -->


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

The [`main_gui.py`](./source/main_gui.py) is responsible for this GUI program and contatins all the code.
<br>So Simply do:

```bash
python3 source/main_gui.py
```



 I have also provided two sample pdfs in directory [samples](https://github.com/s-shifat/mrg-pdf/tree/main/samples) If you need to test them


###### Also if you need, feel free to clone the repository to modify the source code.

