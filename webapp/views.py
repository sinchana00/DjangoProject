from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import University
from django.http import JsonResponse
from django.contrib import messages
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import  UniversitySerializer


# Create your views here.

def home(request):
    uni = University.objects.all()
    return render(request, 'home.html', {'uni': uni})

#returns a json format of all the unis
def listOfUniversities(request):
    data = list(University.objects.values())
    return JsonResponse(data, safe=False)

#same like the abovce function using serializers
class UniversityList(APIView):
    def get(self, request):
        uni_id = University.objects.all()
        serializer = UniversitySerializer(uni_id, many=True)
        return Response(serializer.data)
    def post(self):
        pass





# def all_unis(request):
#     if request.method == 'POST':
#         university_id = request.POST['university_id']
#         if University.objects.filter(university_id=university_id).exists():
#             # uni = University.objects.all();
#             uni_list = University.objects.filter(university_id=university_id)
#             return render(request, 'lists.html', {'uni_list': uni_list})
#         else:
#             messages.info(request, 'Theres no college with the mentioned ID.')
#
#     uni_list = University.objects.all().order_by('university_id')
#     return render(request, 'lists.html', {'uni_list': uni_list})
#
#
