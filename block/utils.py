import datetime
from django.utils import timezone
from django.contrib.contenttypes.models import ContentType
from .models import Block
from hashlib import sha256
from actions.models import Action


def create_block():
    # check for any similar action made in the last minute
    now = timezone.now()
    last_minute = now - datetime.timedelta(seconds=15)
    s = " "
    if Block.objects.filter().count() > 0:
        prev = Block.objects.latest('created')
        actions = Action.objects.filter(saved = False)
        if prev.created <= last_minute and actions.count() > 0:
            prev_hash = hash(prev)
            for action in actions:
                s += str(actions)

            block = Block(data=s, block_number=prev.block_number + 1, block_prev=prev, block_prev_hash=prev_hash)
            block.save()
            for action in actions:
                action.saved = True
                action.save()
            return True
    else:
        actions = Action.objects.filter(saved = False)
        for action in actions:
                s += str(actions)

        block = Block(data=s, block_number=1, block_prev=None)
        block.save()
        for action in actions:
            action.saved = True
            action.save()
        return True

def hash(prev):

    return sha256(
        u'{}{}{}'.format(
            prev.block_number,
            prev.data,
            prev.block_prev_hash).encode('utf-8')).hexdigest()


