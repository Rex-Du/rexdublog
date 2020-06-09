from django.shortcuts import render
from rest_framework.views import APIView
from pure_pagination import Paginator, PageNotAnInteger

from home.models import Article


# Create your views here.
class TimeLineView(APIView):
    def get(self, request):
        articles = Article.objects.order_by('-add_time')
        page = request.GET.get('page', 1)
        paginator = Paginator(articles, 20, request=request)
        try:
            curr_page = paginator.page(page)
        except PageNotAnInteger:
            curr_page = paginator.page(1)
        return render(request, 'time.html', locals())
