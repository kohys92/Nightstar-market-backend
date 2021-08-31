#작성중인 파일

import os
import sys
import django
import csv

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "BBmarket.settings")
django.setup()

#from .products.models import *

CSV_FILE = './csv_file.csv'

with open(CSV_FILE) as csv_f:
    rows = csv.reader(csv_f)
    
    next(rows, None)
    
    def prod:
        for row in rows:
        
