from django import forms
from grid.models import GridItem


class GridForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        if self.instance.pk is not None:
            self.fields['create'].initial = 0

    create = forms.IntegerField(
        label="Create # Grid items",
        help_text="Create this number of grid cells",
    )

    class Meta:
        model = GridItem
        exclude = ('page', 'position', 'placeholder',
                   'language', 'plugin_type')
