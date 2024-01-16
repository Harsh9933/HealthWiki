from django.shortcuts import render
from joblib import load

model = load('./Model/rndForestModel.joblib')

# Create your views here.

def Predictor(request):
     if request.method == 'POST':
        print(request.POST)
        symptom1 = request.POST.get('symptom1', 0)
        symptom2 = request.POST.get('symptom2', 0)
        symptom3 = request.POST.get('symptom3', 0)
        symptom4 = request.POST.get('symptom4', 0)
        symptom5 = request.POST.get('symptom5', 0)
        symptom6 = request.POST.get('symptom6', 0)
        y_pred = model.predict([[symptom1,symptom2,symptom3,symptom4,symptom5,symptom6,0,0,0,0,0,0,0,0,0,0,0]])
        print(y_pred)
        return render(request , 'predict.html', {'result' : y_pred})
     return render(request, 'predict.html')


