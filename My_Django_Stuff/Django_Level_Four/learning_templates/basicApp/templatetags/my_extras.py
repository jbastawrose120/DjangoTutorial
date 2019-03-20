from django import template

register = template.Library()
@register.filter(name='namedCut')
def my_cut(value,arg):
    """
    This cuts out all values of 'arg' from the string!
    """

    return value.replace(arg,'')

#register.filter('namedCut', my_cut)
