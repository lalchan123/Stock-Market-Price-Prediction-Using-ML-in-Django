from django.shortcuts import render
import pandas as pd
import numpy as np
from sklearn import metrics
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from .models import StockPredict
from django.core.paginator import Paginator

# Create your views here.
def home(request):
    return render(request, "home.html")

def predict(request):
    return render(request, "predict.html")

def result(request):
    dataset=pd.read_csv(r'F:\Project and Thesis\Project\Django Project\ML Django Project\Stock Market Price Prediction\Stock_Market_Price_Prediction/tesla-stock-price.csv')
    dataset.drop('date',axis = 1, inplace = True)
    X  = dataset[['open','high','low','volume']]
    y = dataset['close']
    X_train , X_test , y_train , y_test = train_test_split(X, y, test_size=0.15, random_state = 0)
    regressor = LinearRegression()
    regressor.fit(X_test,y_test)
    if request.method == "POST":
        n1 = float(request.POST['n1'])
        n2 = float(request.POST['n2'])
        n3 = float(request.POST['n3'])
        n4 = float(request.POST['n4'])
    
        pred = regressor.predict(np.array([n1,n2,n3,n4]).reshape(1,-1))
        
        data = StockPredict(open=n1,high=n2,low=n3,volume=n4,pre_price_close=pred)
        data.save()
    
    return render(request, "predict.html", {"result":pred,})

def recordData(request):
    data = StockPredict.objects.all().order_by('-id')
    paginator = Paginator(data, 10) 
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, "recordData.html",{"page_obj":page_obj, })  
