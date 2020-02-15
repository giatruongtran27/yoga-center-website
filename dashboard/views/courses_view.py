from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse
from django.contrib.admin.views.decorators import staff_member_required
from django.views import View
from ..forms import courses_form
from django.utils.decorators import method_decorator
from ..decorators import admin_required
from django.views.generic.list import ListView
from django.contrib.auth.decorators import user_passes_test
from courses.models import Course
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required


@method_decorator([login_required, admin_required], name='dispatch')
class CourseListView(ListView):
    model = Course
    template_name = 'dashboard/courses/list.html'
    context_object_name = 'courses'
    ordering = ['-created_at']
    paginate_by = 5

    def get_context_data(self, **kwargs):
        context = super(CourseListView, self).get_context_data(**kwargs)
        context['active_nav'] = 'courses'
        return context


@method_decorator([login_required, admin_required], name='dispatch')
class CourseNewView(View):
    template_name = 'dashboard/courses/new.html'

    def get(self, request):
        form = courses_form.CourseForm()
        context = {
            'form': form,
            'active_nav': 'courses'
        }
        return render(request, self.template_name, context=context)

    def post(self, request, *args, **kwargs):
        form = courses_form.CourseForm(request.POST, request.FILES)
        context = {'form': form}

        if form.is_valid():
            form.save()
            return redirect('dashboard:courses-list')

        return render(request, self.template_name, context=context)


@method_decorator([login_required, admin_required], name='dispatch')
class CourseEditView(UpdateView):
    model = Course
    template_name = 'dashboard/courses/edit.html'
    slug_field = 'slug'
    form_class = courses_form.CourseEditForm

    def get_success_url(self):
            return reverse('dashboard:courses-list', kwargs={})

    def get_context_data(self, **kwargs):
        context = super(CourseEditView, self).get_context_data(**kwargs)
        context['active_nav'] = 'courses'
        return context


@method_decorator([login_required, admin_required], name='dispatch')
class CourseDeleteView(DeleteView):
    model = Course
    success_url = reverse_lazy('dashboard:courses-list')
