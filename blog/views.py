from django.shortcuts import render

from django.views.generic import ListView, DetailView
from django.views.generic.dates import ArchiveIndexView, YearArchiveView, MonthArchiveView
from django.views.generic.dates import DayArchiveView, TodayArchiveView

from blog.models import Post

# Create your views here.

#--- ListView
class PostLV(ListView):
    model = Post                            # PostLV 클래스의 대상 테이블은 Post 클래스임
    template_name = 'blog/post_all.html'    # 템플릿 파일 지정
    context_object_name = 'posts'           # 템플릿 파일로 넘겨주는 객체 리스트에 대한 컨텍스트 변수명 지정(object_list도 함께 사용가능)
    paginate_by = 2                         # 한 페이지에 보여주는 객체 리스트의 숫자

#--- DetailView
class PostDV(DetailView):
    model = Post

#--- ArchiveView
class PostAV(ArchiveIndexView):
    model = Post
    date_field = 'modify_date'              # 기준이 되는 날짜 필드, 즉 변경날짜가 최근인 포스트를 먼저 출력

class PostYAV(YearArchiveView):
    model = Post
    date_field = 'modify_date'
    make_object_list = True

class PostMAV(MonthArchiveView):
    model = Post
    date_field = 'modify_date'

class PostDAV(DayArchiveView):
    model = Post
    date_field = 'modify_date'

class PostTAV(TodayArchiveView):
    model = Post
    date_field = 'modify_date'