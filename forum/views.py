from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.template import RequestContext, loader
from django.core.urlresolvers import reverse
from .models import Thread, Comment
from .forms import NameForm

#Default Page. List all thread in order of updatedAt
def index(request):
	latestThreads = Thread.objects.order_by('-updatedAt')
	template = loader.get_template('forum/index.html')
	context = RequestContext(request, {
		'latestThreads': latestThreads,
		})
	return HttpResponse(template.render(context))

def detail(request, threadID):
	thread = Thread.objects.get(id=threadID)
	relatedComments = Comment.objects.filter(thread=threadID).order_by('score')
	
	template = loader.get_template('forum/threadDetail.html')
	context = RequestContext(request, {
		'thread': thread,
		'relatedComments': relatedComments,
		})
	return HttpResponse(template.render(context))

def addComment(request, thread, text, username):
	comment = Comment(thread=request.POST['thread'], text=request.POST['text'], username=request.POST['username']);
	comment.save(t);

def get_name(request):
	# if this is a POST request we need to process the form data
    if request.method == 'POST':
        form = NameForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect('/')
    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()
    return render(request, 'name.html', {'form': form})
