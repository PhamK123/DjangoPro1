from django.views import generic
from .models import Project

class ProjectList(generic.ListView):
    queryset = Project.objects.filter(status=1)
    template_name = 'index.html'

class ProjectDetail(generic.DetailView):
    model = Project
    template_name = 'post.html'