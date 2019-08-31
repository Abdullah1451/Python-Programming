# 'subprocess' Is A Package Or Class Which We Can Use By Import.After Import We Can Access All The Methods

import subprocess  
# One Of The Methods Is 'check_call'.It Executes Another .py File And Write The Output To The Open File
with open("output.txt", "wb") as f:  
    subprocess.check_call(["python", "ReadFile.py"], stdout=f)  