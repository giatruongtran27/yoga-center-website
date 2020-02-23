from django.http import HttpResponse, Http404

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from dashboard.forms.lesssons_form import LessonForm
from lessons.models import Lesson
from lessons.serializers.lesson_serializer import LessonSerializer
from ..decorators import admin_required, staff_required
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views.generic.list import ListView
from django.views import View
from django.shortcuts import render


@method_decorator([login_required, staff_required], name='dispatch')
class LessonListView(ListView):
    model = Lesson
    template_name = 'dashboard/lessons/list.html'
    context_object_name = 'lessons'
    paginate_by = 5
    ordering = ['-day']

    def get_context_data(self, **kwargs):
        context = super(LessonListView, self).get_context_data(**kwargs)
        context['active_nav'] = 'roll_calls'
        return context


@method_decorator([login_required, staff_required], name='dispatch')
class LessonDetailApiView(APIView):
    def get_object(self, pk):
        try:
            return Lesson.objects.get(pk=pk)
        except Lesson.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        lesson = self.get_object(pk)
        serializer = LessonSerializer(lesson)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        instance = self.get_object(pk)
        form = LessonForm(request.POST, request.FILES, instance=instance)
        if form.is_valid():
            lesson = form.save()
            serializer = LessonSerializer(lesson)
            return Response(serializer.data)
        return HttpResponse(form.errors.as_json(), status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        lesson = self.get_object(pk)
        lesson.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@method_decorator([login_required, staff_required], name='dispatch')
class ListRollCallApiView(View):
    template_name = 'dashboard/lessons/roll_calls.html'

    def get(self, request, pk):
        lesson = Lesson.objects.get(pk=pk)
        un_studied_roll_calls = lesson.roll_calls.filter(studied=False)
        studied_roll_calls = lesson.roll_calls.filter(studied=True)
        total_count = un_studied_roll_calls.count() + studied_roll_calls.count()
        context = {
            'lesson': lesson,
            'un_studied_roll_calls': un_studied_roll_calls,
            'studied_roll_calls': studied_roll_calls,
            'active_nav': 'roll_calls',
            'total_count':total_count
        }
        return render(request, self.template_name, context=context)
