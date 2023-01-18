from django.shortcuts import render
from django.views import View  
from django.http import JsonResponse
import pickle 
import time 
# Create your views here.
model=pickle.load(open("app/data/model.pkl","rb"))

class  HomeView(View):
    
    def get(self,request):
        return render(request,"app/index.html")

    def post(self,request):
        names={"0":"setosa","1":"versicolor","2":"virginica"}
        sepalLength=request.POST.get("SepalLength")
        sepalWidth=request.POST.get("SepalWidth")
        petalLength=request.POST.get("PetalLength")
        petalWidth=request.POST.get("PetalWidth")
        predict=model.predict([[float(sepalLength),float(sepalWidth),float(petalLength),float(petalWidth)]])
        time.sleep(2)
        
        return JsonResponse({"payload":names[str(predict[0])]})
