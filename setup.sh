#!bin/bash
# run: source setup.sh 
python3 -m venv ./venv

source venv/bin/activate

pip install -r requirements.txt

# pip install django

django-admin startproject setup .

echo "\n==== END SETUP ===="