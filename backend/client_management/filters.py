import django_filters

from client_management.models import Work


class WorkFilter(django_filters.FilterSet):
  artist = django_filters.CharFilter(
    field_name='assignment__artist__name',
    lookup_expr='iexact'
  )

  work_type = django_filters.ChoiceFilter(
    choices=Work.WORK_TYPE_CHOICES
  )

  # work_type = django_filters.CharFilter(
  #   field_name='work_type',
  #   lookup_expr='iexact'
  # )

  class Meta:
    model = Work
    fields = ('artist', 'work_type')

