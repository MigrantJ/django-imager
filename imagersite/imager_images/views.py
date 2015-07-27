from django.http import HttpResponse
from django.template import loader
# from django.views.generic import TemplateView


def index(request):
    template = loader.get_template('index.html')
    response_body = template.render()
    return HttpResponse(response_body)


# class ClassView(TemplateView):
#     template_name = 'index.html'

#     def get_context_data(self, num=0, name='balloons'):
#         return {}
