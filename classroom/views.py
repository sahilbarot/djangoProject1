from django.shortcuts import render
from django.http import JsonResponse
from .models import standard,classroom,students
# Create your views here.


def student(request,classroom_id):
    data=classroom.objects.get(pk=classroom_id)

    return JsonResponse({
                            'data':data,
                            "student":data.class_room.all()
                                        },safe=False)