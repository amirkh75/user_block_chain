from block.models import Block
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from actions.utils import create_action


class BlockList(LoginRequiredMixin, ListView):

    def get(self, request, *args, **kwargs):
        user = request.user
        create_action(user, 'seen blocks', user)
        return super().get(request, *args, **kwargs)

    model = Block
    context_object_name = 'blocks'
    queryset = Block.objects.all()[:5]
    template_name = 'block/BlockList.html'
