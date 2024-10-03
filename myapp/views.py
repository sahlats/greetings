from django.shortcuts import render
from django.views.generic import View


class HelloWorldView(View):
    def get(self,request,*args,**kwargs):
        return render(request,'HelloWorld.html')

class GoodMorning(View):
    def get(self,request,*args,**kwargs):
        return render(request,'goodmorning.html')

class GoodAfternoon(View):
    def get(self,request,*args,**kwargs):
        return render(request,'goodafter.html')

class GoodEvening(View):
    def get(self,request,*args,**kwargs):
        return render(request,'goodevening.html')

class SelfIndroView(View):
    def get(self,request,*args,**kwargs):
        data={
            'name':'sahla',
            'qualification':'BCA',
            'cource':'computer science',
            'contact':'726172617',
        }
        return render(request,'self.html',data)

class ActorsView(View):
    def get(self,request,*args,**kwargs):
        return render(request,'actors.html')

class CourseView(View):
    def get(self,request,*args,**kwargs):
        data={
        'coursename':'djangoreactfullstack',
        'backendframework':'pythondjango',
        'frontend':'react',
        'duration':'7 month',
        }

        return render(request,'cource.html',data)