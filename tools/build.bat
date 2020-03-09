@echo off
pip install -r requirements.txt
python tools/compile.py build
python tools/compile.py bdist_msi

