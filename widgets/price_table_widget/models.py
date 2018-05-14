from django.db import models
from cms.models import CMSPlugin
from django.utils.translation import ugettext as _


class PriceTableWidgetPluginModel(CMSPlugin):
    limit_per_page = models.IntegerField(default=10, verbose_name=_('Ilość usług'))

