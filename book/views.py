from django.shortcuts import render
import os

def index(request):
    db_user = os.environ.get('DB_USER')
    db_pass = os.environ.get('DB_PASS')
    db_data = os.environ.get('DB_DATA')
    print(db_user)
    print(db_pass)
    print(db_data)
    return render(request, "html/index.html", {})