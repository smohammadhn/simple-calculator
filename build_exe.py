"""
Build script to create Windows executable
Run this with: python3 build_exe.py
"""
import os
import sys

print("Installing PyInstaller...")
os.system("pip3 install pyinstaller")

print("\nBuilding executable...")
# --windowed: no console window
# --onefile: single exe file
# --name: name of the exe
# --icon: optional icon file
command = 'pyinstaller --windowed --onefile --name "PlusMinusCalculator" app.py'

os.system(command)

print("\n✅ Done! Check the 'dist' folder for your .exe file")
