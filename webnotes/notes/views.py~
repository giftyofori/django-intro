# Create your views here.
from django.template import context,loader
from django.http import HttpResponse
from models import Notes
def notes_list(request):
    note_list=Notes.objects.all()
    t=loader.get_template('notes/list.html')
    c= context({
	'note_list': note_list,
    })
    return HttpResponse(t.render(c)) 
def notes_detail(request,id):
    notes=Notes.objects.get(pk=id)
    t= loader.get_template('notex/list.html')
    c= context({
	'note':note,
    })
    return HttpResponse(t.render(c))
