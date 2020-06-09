from django.shortcuts import render
from rest_framework.views import APIView

from about.models import Experiences

# Create your views here.
class AboutMeView(APIView):
    def get(self, request):
        experiences = Experiences.objects.order_by('-add_time')[:4]
        return render(request, 'about.html', locals())
