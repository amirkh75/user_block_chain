from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from hashlib import sha256
import datetime


class Block(models.Model):
    signers = models.ForeignKey('users.CustomUser', on_delete=models.CASCADE, null=True,
                                            blank=True)

    data = models.TextField(null=True, blank=True)
    
    block_number = models.PositiveIntegerField(null=True,
                                            blank=True)
    block_prev = models.ForeignKey("Block",
                                    on_delete=models.CASCADE, null=True,
                                    blank=True)
    block_prev_hash = models.CharField(max_length=255, blank=True, null=True)

    created = models.DateTimeField(auto_now_add=True,
                                   db_index=True)

    def __str__(self):
        return "Block " + str(self.block_number)
