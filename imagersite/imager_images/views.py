from django.shortcuts import render
from .models import Photos
# from django.views.generic import TemplateView

# import pdb; pdb.set_trace()


def index(request):
    rand_photo = Photos.objects.filter(published='public').first()
    context = {
        'photo': rand_photo
    }
    return render(request, 'index.html', context=context)


# class ClassView(TemplateView):
#     template_name = 'index.html'

#     def get_context_data(self, num=0, name='balloons'):
#         return {}
