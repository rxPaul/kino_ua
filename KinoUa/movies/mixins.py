from django.shortcuts import render


class ObjectListMixin:
    model = None
    template = None
    multiple_str = None

    def get(self, request):

        objects = self.model.objects.all()
        context = {self.multiple_str: objects}
        return render(request, self.template, context=context)


