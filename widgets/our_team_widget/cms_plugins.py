from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from .models import OurTeamWidgetPluginModel
from django.utils.translation import ugettext as _
from .forms import OurTeamWidgetForm
from hairdresser.models import Barbers


class CMSOurTeamWidgetPlugin(CMSPluginBase):
    model = OurTeamWidgetPluginModel
    name = _("Lista fryzjerów")
    render_template = "barbers_list.html"
#    change_form_template = 'base.html'
    form = OurTeamWidgetForm

    def render(self, context, instance, placeholder):
        # print(instance.news)

        barbers = Barbers.objects.all()

        context.update({
            'barbers': barbers,
            'news_list_plugin_instance': instance,
            # 'placeholder': placeholder
        })
        return context

plugin_pool.register_plugin(CMSOurTeamWidgetPlugin)
