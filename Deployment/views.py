from django.shortcuts import render

# Create your views here.

from joblib import load
model = load('./savemodels/model.joblib')


def predict(request):

    if request.method == 'POST':
        sepal_length = request.POST['sepal_length']
        sepal_width = request.POST['sepal_width']
        petal_length = request.POST['petal_length']
        petal_width = request.POST['petal_width']
        y_pred = model.predict([[sepal_length, sepal_width, petal_length, petal_width]])
        print(y_pred)
        if y_pred[0] == 0:
            y_pred = 'Setosa'
        elif y_pred[0] == 1:
            y_pred = 'Verscicolor'
        else:
            y_pred = 'Virginica'
        return render(request, 'main.html', {'result' : y_pred})
    return render(request,'main.html')