from django.shortcuts import render
from django.http import JsonResponse
from .models import *

# Create your views here.
def index(request):
	return render(request, './register_member.html')

def index2(request):
	return render(request, './second.html')

def check_id(request):

	if request.method =='GET':

		print(request.GET.get('user_id',None)) #cmd에 출력
		user_id = request.GET.get('user_id',None)

		try:
			member_list =Member.objects.get(user_id=user_id)
			result={"result":'true'}
		except :
			result={"result":'false'}

		return JsonResponse(result)

def register_member_db(request):

	if request.method=='POST':

		user_id=request.POST['user_id'] #name
		user_psw=request.POST['user_psw']

		new_member=Member(user_id=user_id, user_psw=user_psw)
		new_member.save()

		return render(request, './register_member.html')