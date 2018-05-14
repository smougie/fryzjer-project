from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from .models import PriceTableWidgetPluginModel
from django.utils.translation import ugettext as _
from .forms import PriceTableWidgetForm
from hairdresser.models import PriceTable


class CMSPriceTableWidgetPlugin(CMSPluginBase):
    model = PriceTableWidgetPluginModel
    name = _("Ceny")
    render_template = "price_table.html"
#    change_form_template = 'base.html'
    form = PriceTableWidgetForm

    def render(self, context, instance, placeholder):
        # print(instance.news)

        price_table = PriceTable.objects.all()

        context.update({
            'price_table': price_table,
            'price_table_plugin_instance': instance,
            # 'placeholder': placeholder
        })
        return context

plugin_pool.register_plugin(CMSPriceTableWidgetPlugin)
