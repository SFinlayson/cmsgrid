from django.db import models
from cms.models import CMSPlugin
from cms.models.fields import PageField
from filer.fields.image import FilerImageField
from django.conf import settings
from djangocms_attributes_field.fields import AttributesField


class Grid(CMSPlugin):
    """
    A plugin that has sub Column classes
    """

    label = models.CharField(max_length=80, blank=True, null=True)
    class_name = models.CharField(max_length=80)
    template_areas = models.TextField(
        blank=True, null=True,
        help_text="Encapsulate rows with quotes")
    grid_template_columns = models.CharField(
        max_length=255, blank=True, null=True,
        help_text="1fr 10px 1fr")
    grid_template_rows = models.CharField(
        max_length=255, blank=True, null=True)

    attributes = AttributesField(
        verbose_name='Attributes',
        blank=True,
        excluded_keys=['href', 'target'],
    )
    cmsplugin_ptr = models.OneToOneField(
        CMSPlugin,
        related_name='%(app_label)s_%(class)s',
        parent_link=True,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        if self.label:
            return self.label
        else:
            return "Grid"


class GridCell(CMSPlugin):
    """
    A cell for the Grids Plugin
    """
    label = models.CharField(max_length=80, blank=True, null=True)
    gridarea = models.CharField(max_length=80, blank=True, null=True)

    attributes = AttributesField(
        verbose_name='Attributes',
        blank=True,
        excluded_keys=['href', 'target']
    )
    cmsplugin_ptr = models.OneToOneField(
        CMSPlugin,
        related_name='%(app_label)s_%(class)s',
        parent_link=True,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        if self.label:
            return self.label
        else:
            return "GridItem"

"
