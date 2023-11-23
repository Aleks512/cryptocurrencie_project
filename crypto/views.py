from django.http import HttpResponseForbidden, HttpResponse, JsonResponse
from django.shortcuts import render, redirect, get_object_or_404


def crypto(request):
    return render(request, 'crypto/crypto.html')
