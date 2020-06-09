from django.core.paginator import EmptyPage
from django.http import HttpResponseRedirect, request
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
# from rest_framework.pagination import PageNumberPagination, CursorPagination
from pure_pagination import Paginator, PageNotAnInteger

from home.models import Article, ReadAndPraise, Comment


# Create your views here.


class LearningView(APIView):
    def get(self, request, category=None):
        if category:
            articles = Article.objects.filter(category__name=category).order_by('-add_time')
        else:
            articles = Article.objects.order_by('-add_time')
        page = request.GET.get('page', 1)
        paginator = Paginator(articles, 8, request=request)
        try:
            curr_page = paginator.page(page)
        except (PageNotAnInteger, EmptyPage):
            return HttpResponseRedirect('handler404')

        max_clicked = Article.objects.order_by('-click_nums')[:8]
        clicked_ids = [article.id for article in max_clicked]
        max_praise = Article.objects.exclude(id__in=clicked_ids).order_by('-praise_nums')[:8]

        return render(request, 'learning.html', locals())


class DetailView(APIView):
    def get(self, request, id, cate=1):
        remote_addr = request.META.get('REMOTE_ADDR')
        try:
            article = Article.objects.get(id=int(id))
        except Exception as e:
            return HttpResponseRedirect('handler404')

        article_ids = Article.objects.filter(category=article.category).order_by(
            '-add_time').values_list('id', flat=True)
        article_ids = list(article_ids)
        curr_article_index = article_ids.index(int(id))
        pre_article_id = article_ids[curr_article_index - 1] if curr_article_index > 0 else -1
        next_article_id = article_ids[curr_article_index + 1] if curr_article_index < len(
            article_ids) - 1 else -1
        pre_article = Article.objects.get(id=pre_article_id) if pre_article_id != -1 else None
        next_article = Article.objects.get(id=next_article_id) if next_article_id != -1 else None

        try:
            read_and_praise = ReadAndPraise.objects.get(ip=remote_addr, article_id=int(id),
                                                        category=cate)
            read_and_praise.read_nums += 1
            read_and_praise.save()
            has_praise = read_and_praise.is_praise
            is_valid_clicked = True if read_and_praise.read_nums < 2 else False
        except Exception as e:
            record = ReadAndPraise(ip=remote_addr, article_id=int(id), category=cate,
                                   is_praise=False, read_nums=1)
            record.save()
            is_valid_clicked = True

        if is_valid_clicked:
            article.click_nums += 1
            article.save()
        comments = Comment.objects.filter(article_id=id).order_by('date_publish')
        return render(request, 'detail.html', locals())


class PraiseView(APIView):
    def post(self, request):
        remote_addr = request.META.get('REMOTE_ADDR')
        article_id = request.data.get('article_id')
        category = request.data.get('category')

        read_and_praise = ReadAndPraise.objects.get(ip=remote_addr, article_id=article_id,
                                                    category=category)
        # todo when category is not 1
        article = Article.objects.get(id=article_id)

        if read_and_praise.is_praise:
            read_and_praise.is_praise = False
            article.praise_nums -= 1
        else:
            read_and_praise.is_praise = True
            article.praise_nums += 1
        read_and_praise.save()
        article.save()
        return Response(article.praise_nums)


class CommentView(APIView):
    def post(self, request, article_id):
        comment_text = request.POST.get('user_comment')
        user = request.user.first_name or request.META.get('REMOTE_ADDR')
        comment = Comment(content=comment_text, article_id=int(article_id), user=user)
        comment.save()
        return HttpResponseRedirect(redirect_to=f'detail/{article_id}')
