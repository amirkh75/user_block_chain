from actions.models import Action
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from actions.utils import create_action


class Actions(LoginRequiredMixin, ListView):

    def get(self, request, *args, **kwargs):
        user = request.user
        create_action(user, 'seen actions', user)
        return super().get(request, *args, **kwargs)

    model = Action
    context_object_name = 'action'
    queryset = Action.objects.all()[:5]
    template_name = 'actions/action/detail.html'
