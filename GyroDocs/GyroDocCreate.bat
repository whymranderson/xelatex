
cd C:\Documents and Settings\The One\My Documents\tony\2014\xelatexfolder\GyroDocs

REM sphinx-build -b latex . _build/latex (doesn't work, process won't start, also activate env stop working)

python "C:\Documents and Settings\The One\Anaconda\Scripts\sphinx-build-script.py" -b latex . _build/latex

REM python "C:\Documents and Settings\The One\Anaconda\envs\python3\Scripts\sphinx-build-script.py" -b latex . _build/latex
pause

cd C:\Documents and Settings\The One\My Documents\tony\2014\xelatexfolder\GyroDocs\_build\latex\

pdflatex GyroSoftdocumentation.tex

pdflatex GyroSoftdocumentation.tex

pause