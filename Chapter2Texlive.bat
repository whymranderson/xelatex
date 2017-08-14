@echo off

cd C:\Documents and Settings\The One\My Documents\tony\2014\xelatexfolder\

set /p id="Choose chapter: (1)Program (2)Case_Study (3)Orientation Estimation (4)accuracy  "

IF %id% == 1 SET chapname=Program
IF %id% == 2 SET chapname=Case_Study
IF %id% == 3 SET chapname=Orientation_Estimation
IF %id% == 4 SET chapname=accuracy

python Encode_Preamble_Adjust_for_chapter.py %chapname%

xelatex --shell-escape Chapter_%chapname%_upa.tex

Chapter_%chapname%_upa.pdf
