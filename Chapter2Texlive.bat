@echo off

cd C:\Documents and Settings\The One\My Documents\tony\2014\xelatexfolder

set /p id="Choose chapter: (4) Case_Study (3) Program (2) Orientation_Estimation "

IF %id% == 4 SET chapname=Case_Study
IF %id% == 3 SET chapname=Program
IF %id% == 2 SET chapname=Orientation_Estimation

python.exe Encode_Preamble_Adjust_for_chapter.py %chapname%

pause

xelatex --shell-escape Chapter_Case_Study_upa.tex

pause