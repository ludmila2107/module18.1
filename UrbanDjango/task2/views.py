from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView


# Функциональное представление
def function_based_view(request):
	return render(request, 'second_task/func_template.html')


# Классовое представление
# class classBasedView(View):
# 	def get(self, request):
# 		return render(request, 'second_task/class_template.html')


class ViewByClass(TemplateView):
    template_name = 'second_task/class_template.html'