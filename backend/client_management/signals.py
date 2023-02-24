from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from django.db import transaction

from client_management.models import Client


@receiver(post_save, sender=User)
def creat_user_handler(sender, instance, created, **kwargs):
	if created:
		with transaction.atomic():
			Client.objects.create(
				name=instance.username,
				user=instance
			)