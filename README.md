# App Switching Shortcut for the Surface Pen
This Python script allows the Surface Pen's eraser button to be used to switch applications (by mimicking the Alt + Tab shortcut). 
The script is especially useful when using applications in full-screen mode and without a keyboard connected.

## How to Use
### Prerequisites
- Python must be installed on your Surface Pro. Python can be downloaded from [here](https://www.python.org/downloads/windows/)
- PyInstaller must also be installed on your Surface Pro. For instructions on how to do so, please see [this link](https://www.pyinstaller.org/)

Note: this script has been tested on a Surface Pro 7 tablet, running Windows 10, with a 4th generation Surface Pen and Python 3  

### Installation
1.  Clone or download the repository
2.  In Command Prompt, navigate to the folder in which the script is located
3.  Run the following command: `pyinstaller app.pyw`. 
    This command will create a folder called "dist" in the same directory as the Python file. Inside the "dist" folder will be an executable file with the same name as the Python script. 
4.  Next, go to Windows Settings -> Devices -> Pen & Windows Ink and then scroll down to the "Pen shortcuts" section
5.  For the Click once action, set it to "Launch a classic app". Then, use the browse button to select the executable file created in step 3.

### Usage
Once installed, the Python script will run each time the Eraser button on the Surface Pen is clicked once. Clicking the Eraser button once will be equivalent to pressing and holding down the Alt key and then pressing the Tab key once.

To switch between more than one app at a time (i.e. the equivalent of pressing the Tab key more than once while holding down the Alt key), hold down the eraser button.
When you have selected the app that you want to switch to, click the eraser button once again (this will be equivalent to letting the Alt key go).

To quickly switch between two apps, you can double-click the eraser button with a small delay in-between.
