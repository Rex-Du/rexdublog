from datetime import datetime

from django.core.paginator import PageNotAnInteger
from django.contrib.auth import logout
from django.shortcuts import render, redirect
from pure_pagination import Paginator
from rest_framework.views import APIView

from home.models import Article, Visitor


# Create your views here.


class HomePageView(APIView):
    def get(self, request):

        all_banner_articles = Article.objects.filter(is_banner=True).order_by('-add_time')
        banner_articles = all_banner_articles[:3]
        topic_banners = all_banner_articles[3:5]
        news_box_banners = all_banner_articles[5:11]
        pics_banners = all_banner_articles[11:14]

        banner_ids = [article.id for article in all_banner_articles[:14]]
        max_clicked = Article.objects.order_by('-click_nums')[:8]
        clicked_ids = [article.id for article in max_clicked]
        max_praise = Article.objects.exclude(id__in=clicked_ids).order_by('-praise_nums')[:8]

        articles = Article.objects.exclude(id__in=banner_ids).order_by('-add_time')
        page = request.GET.get('page', 1)
        paginator = Paginator(articles, 18, request=request)
        try:
            curr_page = paginator.page(page)
        except PageNotAnInteger:
            curr_page = paginator.page(1)
        remote_addr = request.META.get('REMOTE_ADDR')
        try:
            visitor = Visitor.objects.get(ip=remote_addr)
            visitor.visit_count += 1
            visitor.visit_time = datetime.now()
            visitor.save()
        except:
            visitor = Visitor(ip=remote_addr, visit_time=datetime.now(), visit_count=1)
            visitor.save()
        return render(request, 'home.html', locals())


class LoginView(APIView):
    def get(self, request):
        return render(request, 'login.html', locals())


class LogoutView(APIView):
    def get(self, request):
        logout(request)
        return redirect(to='home')


def page_not_found(request, exception):
    # 全局404页面配置
    from django.shortcuts import render_to_response
    response = render_to_response('404.html', {})
    response.status_code = 404
    return response


def page_error(request):
    # 全局500页面配置
    from django.shortcuts import render_to_response
    response = render_to_response('500.html', {})
    response.status_code = 500
    return response
