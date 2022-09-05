from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from cms.models.pluginmodel import CMSPlugin
from .models import Grid, GridItem
from .forms import GridForm


@plugin_pool.register_plugin
class GridPlugin(CMSPluginBase):
    model = Grid
    module = "Page"
    name = "Grid"
    render_template = "cms/plugins/grid.html"
    allow_children = True
    child_classes = ["GridItemPlugin"]
    form = GridForm

    def save_model(self, request, obj, form, change):
        response = super().save_model(
            request, obj, form, change
        )
        for _ in range(int(form.cleaned_data['create'])):
            col = GridItem(
                parent=obj,
                placeholder=obj.placeholder,
                language=obj.language,
                position=CMSPlugin.objects.filter(parent=obj).count(),
                gridcell_name="grid_item",
                plugin_type=GridItemPlugin.__name__
            )
            col.save()
        return response


@plugin_pool.register_plugin
class GridItemPlugin(CMSPluginBase):
    model = GridItem
    module = "Grid"
    name = "GridItem"
    render_template = "cms/plugins/griditem.html"
    parent_classes = ["GridPlugin"]
    allow_children = True
