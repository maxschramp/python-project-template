@echo off

echo Creating requirements.txt...
type nul > requirements.txt

echo Creating virtual environment...
python -m venv venv

echo Activating virtual environment...
call .\venv\Scripts\activate.bat

echo Updating pip...
python -m pip install -U pip

echo Installing pip pre-built packages...
pip install -U wheel

echo Installing pip requirements...
pip install -Ur requirements.txt

echo Creating main.bat...
curl -o main.bat https://raw.githubusercontent.com/maxschramp/python-project-template/main/main.bat

echo Creating template.py...
curl -o template.py https://raw.githubusercontent.com/maxschramp/python-project-template/main/template.py

echo Creating main.py
copy template.py main.py

pause
