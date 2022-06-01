from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.views import View
import datetime
from store.models import MyModel
from store.forms import MyForm


def create_view(request):
    context = {}
    form = MyForm(request.POST or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/api/v1/list/")

    context['form'] = form
    return render(request, "create_view.html", context)


def list_view(request):
    context = {}
    context["dataset"] = MyModel.objects.all()

    return render(request, "list_view.html", context)

def detail_view(request, pk):
    context = {}

    context["data"] = MyModel.objects.get(pk=pk)

    return render(request, "detail_view.html", context)

def update_view(request, pk):
    context = {}

    obj = get_object_or_404(MyModel, pk=pk)
    
    # Pass obj as an instance in form
    form = MyForm(request.POST or None, instance=obj)

    # Save the data from the form and redirect to detail_view
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/api/v1/" + pk)

    # add form dictionary to context
    context["form"] = form

    return render(request, "update_view.html", context)


def delete_view(request, pk):
    context = {}

    obj = get_object_or_404(MyModel, pk=pk)

    if request.method == "POST":
        obj.delete()

        return HttpResponseRedirect("/api/v1/list/")
        

    return render(request, "delete_view.html", context)




# from django.core.serializers import serialize
# from django.http import HttpResponse

# class SerializedListView(View):
#     def get(self, request, *args, **kwargs):
#         qs = MyObj.objects.all()
#         json_data = serialize("json", qs, fields=('my_field', 'my_other_field'))
#         return HttpResponse(json_data, content_type='application/json')