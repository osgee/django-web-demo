from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.template import RequestContext, loader
from django.views.decorators.csrf import csrf_exempt

def index(request):
    template = loader.get_template('index.html')
    result=10
    context = RequestContext(request, {
        # 'result': result,
    })
    return HttpResponse(template.render(context))
@csrf_exempt
def predict(request):
    result=5
    try:
        img=request.POST['img']
        
    except KeyError:
        # Redisplay the question voting form.
        # return render(request, 'polls/detail.html', {
        #     'question': p,
        #     'error_message': "You didn't select a choice.",
        # })
    #     print "error_message"
        return HttpResponse("Your predict is %s." % result)
    else:
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        # return HttpResponseRedirect(reverse('polls:results', args=(p.id,)))
        return HttpResponse("Your predict is %s." % result)
        # pass
        # name = request.POST.get('name')
        # return HttpResponse(json.dumps({'name': name}), content_type="application/json")
