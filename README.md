Demo Purpose
-----------------------------
Show machince learning intergration with MemSQL pipelines.
This is a simple decision tree classifier to determine if a tax return is fraud or not fraud.

Demo Contents
-----------------------------
ml_demo.sql - database, table and pipeline creation script

requirements.txt - required python libraries for demo (pip install -r requirements.txt)

stdin_mldemo.py - python script with sklearn decision tree

tax_data.csv - training dataset wit 100 'records'

test_fraud.csv - put in the filesystem pipeline and predict (it's fraud == 1)

test_nofraud.csv - put in the filesystem pipeline and predict (it's NOT fraud == 0)

makeData.sh - shell script to create random tax returns