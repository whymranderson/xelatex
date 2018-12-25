cd 'C:\Users\user\Desktop\myblog'

pwd

sleep 5

git log -30 --format=format:"%w(90,0,5)%ad  %B" --date=short > 'C:\Users\user\Desktop\xelatex_Transend\drawing_code\latex\venture_planning\mysite.log'

echo -----SUBMODULE LOG----- >> 'C:\Users\user\Desktop\xelatex_Transend\drawing_code\latex\venture_planning\mysite.log'

cd 'C:\Users\user\Desktop\db_op'

pwd

sleep 5

git log -30 --format=format:"%w(90,0,5)%ad  %B" --date=short >> 'C:\Users\user\Desktop\xelatex_Transend\drawing_code\latex\venture_planning\mysite.log'
