from django.shortcuts import render
import os

def home_view(request):
    context = {
        "kafka_host": os.environ['KAFKA_HOST'],
        "kafka_port": os.environ['KAFKA_PORT'],
    }
    return render(request, "index.html", context)