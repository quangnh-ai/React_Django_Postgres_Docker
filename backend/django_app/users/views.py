from django.shortcuts import render

from rest_auth.views import LoginView, LogoutView, PasswordChangeView
from rest_framework import permissions
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

# Create your views here.
class APILogoutView(LogoutView):

    # Check token of the user and this token has permission.
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]


class APILoginView(LoginView):
    pass

class APIPasswordUpdateView(PasswordChangeView):
    authentication_classes = [TokenAuthentication]