@echo off

cd C:\Documents and Settings\The One\My Documents\tony\2014\xelatexfolder\otherstuff\venture_planning

set /p id="Choose chapter: (9)unfinished_tasks (8)all_venture_directions (7)website_planning (6)baking (5)connectors (4)CSGO_arrangement (3)develope_process_v2 (2) fixing (1)tex_venture "

IF %id% == 9 SET chapname=unfinished_tasks
IF %id% == 8 SET chapname=all_venture_directions
IF %id% == 7 SET chapname=website_planning
IF %id% == 6 SET chapname=baking
IF %id% == 5 SET chapname=connectors
IF %id% == 4 (
	SET chapname=CSGO_arrangement
	bash grab_mysite_git_log.sh
	)
IF %id% == 3 ( 
	SET chapname=develope_process_v2
	bash grab_cordtrans_git_log.sh
	)
IF %id% == 2 SET chapname=fixing
IF %id% == 1 (
	SET chapname=tex_venture
	bash grab_xelatex_git_log.sh
	)



xelatex --shell-escape %chapname%.tex

%chapname%.pdf
