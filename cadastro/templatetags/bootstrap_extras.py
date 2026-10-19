from django import forms, template

register = template.Library()


@register.filter
def bs_field(field):
    """Desenha o campo com as classes certas do Bootstrap."""
    widget = field.field.widget
    if isinstance(widget, forms.CheckboxInput):
        css = 'form-check-input'
    elif isinstance(widget, (forms.Select, forms.SelectMultiple)):
        css = 'form-select'
    else:
        css = 'form-control'
    if field.errors:
        css += ' is-invalid'
    return field.as_widget(attrs={'class': css})
