#-*- coding: utf-8 -*-
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.views import generic

from .models import Amenities, Rooms


class IndexView(generic.ListView):
    template_name = 'rooms/index.html'
    context_object_name = 'latest_rooms_list'

    def get_queryset(self):
        return Rooms.objects.all()


class DetailView(generic.DetailView):
    model = Rooms
    template_name = 'rooms/detail.html'


class ResultsView(generic.DetailView):
    model = Rooms
    template_name = 'rooms/results.html'


def vote(request, poll_id):
    p = get_object_or_404(Rooms, pk=poll_id)
    try:
        selected_choice = p.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Amenities.DoesNotExist):
        # Redisplay the poll voting form.
        return render(request, 'rooms/detail.html', {
            'rooms': p,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('rooms:results', args=(p.id,)))
