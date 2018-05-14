from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from .models import ContactFormWidgetPluginModel
from django.utils.translation import ugettext as _
from .forms import ContactFormWidgetForm


class CMSContactFormWidgetPlugin(CMSPluginBase):
    model = ContactFormWidgetPluginModel
    name = _("Formularz kontaktowy")
    render_template = "contact_form.html"
#    change_form_template = 'base.html'
    form = ContactFormWidgetForm()

    def render(self, context, instance, placeholder):
        # print(instance.news)


        context.update({
            'contact_form_plugin_instance': instance,
            # 'placeholder': placeholder
        })
        return context

plugin_pool.register_plugin(CMSContactFormWidgetPlugin)
