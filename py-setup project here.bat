@echo on

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

echo Creating main.py...


echo Creating main.bat...


pause
