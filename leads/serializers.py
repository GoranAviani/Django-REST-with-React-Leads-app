from rest_framework import serializers
from leads.models import Lead
class LeadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lead
        fields = ('id', 'name', 'email', 'message')
        

class NoModelSerializer(serializers.Serializer):
   """Your data serializer, define your fields here."""
   testChar = serializers.CharField()
   testList = serializers.CharField()
    #testList = serializers.ListField()