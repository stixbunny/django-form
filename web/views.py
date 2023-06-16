from django.shortcuts import render
from .forms import MessageForm
from .models import Message
from django.http import HttpResponseRedirect


def form(request):
    messages = Message.objects.all().order_by("-pub_date").values()
    if request.method == "POST":
        form = MessageForm(request.POST)
        if form.is_valid():
            message = Message.objects.create(**form.cleaned_data)
            message.save()
        return HttpResponseRedirect("/")
    else:
        form = MessageForm()
    return render(
        request,
        "index.html",
        {"form": form, "messages": messages},
    )
