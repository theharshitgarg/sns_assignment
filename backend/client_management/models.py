from django.db import models
from django.contrib.auth.models import User


class BaseModel(models.Model):
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	class Meta:
		abstract = True


class Client(BaseModel):
	name = models.CharField(max_length=256)
	user = models.OneToOneField(
		User,
		on_delete=models.CASCADE
	)

	def __repr__(self):
		return f"{self.name} : {self.user.username}"

	def __str__(self):
		return self.__repr__()


class Work(BaseModel):
	YOUTUBE = 'YOUTBE'
	INSTAGRAM = 'INSTAG'
	OTHER = 'OTHER'
	WORK_TYPE_CHOICES = (
		(YOUTUBE, 'YOUTUBE'),
		(INSTAGRAM, 'INSTAGRAM'),
		(OTHER, 'OTHER'),
	)
	work_link = models.URLField(max_length=2048)
	work_type = models.CharField(
		max_length=8,
		choices=WORK_TYPE_CHOICES)


	def __repr__(self):
		return f"{self.work_type} : {self.work_link}"

	def __str__(self):
		return self.__repr__()


class Artist(BaseModel):
	name = models.CharField(max_length=256)
	work = models.ManyToManyField(
		Work,
		through='Assignment',
		related_name='work')

	def __repr__(self):
		return f"{self.name}"

	def __str__(self):
		return self.__repr__()


class Assignment(BaseModel):
	artist = models.ForeignKey(
		Artist, on_delete=models.CASCADE)
	work = models.ForeignKey(
		Work, on_delete=models.CASCADE)
	due_date = models.DateTimeField()

	def __repr__(self):
		return f"{self.artist.name} : {self.work.work_type}"

	def __str__(self):
		return self.__repr__()