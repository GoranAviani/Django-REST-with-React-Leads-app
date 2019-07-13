from django.shortcuts import render

# Create your views here.
from leads.models import Lead
from leads.serializers import LeadSerializer
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status    
'''
#Abandoned due to custom API view CreateLead
class LeadListCreate(generics.ListCreateAPIView):
    queryset = Lead.objects.all()
    serializer_class = LeadSerializer
'''
class CreateLead(APIView):
    serializer_class = LeadSerializer

    def post(self, request):
        name = request.data.get("name")
        if name == "testing":
            specialMessage = {'Special Message': name + "is not an allowed name"}
            return Response(specialMessage, status=status.HTTP_406_NOT_ACCEPTABLE)
        email = request.data.get("email")
        message = request.data.get("message")
        data = {'name': name, 'email': email, 'message': message}
        serializer = LeadSerializer(data=data)
        if serializer.is_valid():
            lead = serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




#Depreciated due to using custom views class ShowLeadsList(APIView):
'''
class LeadListShow(generics.ListAPIView):
    queryset = Lead.objects.all()
    serializer_class = LeadSerializer
'''
class ShowLeadsList(APIView):
    def get(self, request):
        leads = Lead.objects.all()[:20]
        data = LeadSerializer(leads, many=True).data
        return Response(data)

