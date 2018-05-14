from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from .models import NewsListWidgetPluginModel
from django.utils.translation import ugettext as _
from .forms import NewsListWidgetForm
from hairdresser.models import News

class CMSNewsListWidgetPlugin(CMSPluginBase):
    model = NewsListWidgetPluginModel
    name = _("Lista newsów")
    render_template = "news_list.html"
#    change_form_template = 'base.html'
    form = NewsListWidgetForm

    def render(self, context, instance, placeholder):
        # print(instance.news)

        last_newses = News.objects.all()

        context.update({
            'last_newses': last_newses,
            'news_list_plugin_instance': instance,
            # 'placeholder': placeholder
        })
        return context

plugin_pool.register_plugin(CMSNewsListWidgetPlugin)
