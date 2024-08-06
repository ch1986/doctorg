from django.shortcuts import render
from django.utils.timezone import datetime
from main.forms import QueryForm
from main.models import Query
import google.generativeai as genai
import os


genai.configure(api_key=os.environ["GOOGLE_API_KEY"])

model = genai.GenerativeModel('gemini-1.5-pro-latest')

def home(request):
    form = QueryForm(request.POST or None)

    if request.method == "POST":
        if form.is_valid():
            query = form.save(commit=False)
            query.log_date = datetime.now()
            query.save()
            message = "Quiero que me respondas en lengua inglesa y que tu respuesta se limite a una lista ordenada de html. Enumera por orden de probabilidad las enfermedades que podría padecer el paciente con estos datos:"
            message += "\nEdad: " + str(query.age)
            message += "\nGénero: " + query.gender
            message += "\Síntomas: " + query.symptoms
            message += "\nAntededentes médicos del paciente: " + query.history
            message += "\nAntecedentes médicos familiares: " + query.family
            message += "\nEstilo de vida: " + query.lifestyle
            message += "\nResultados de pruebas médicas: " + query.tests
            message += "\nOtros detalles relevantes: " + query.other
            response = model.generate_content(message)
            return render(request, "main/home.html", {"form": form, "query": message, "response": response.text,})
    else : return render(request, "main/home.html", {"form": form,})
