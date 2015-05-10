from django import template

register = template.Library()

def multiply(x, y):
    '''Description...'''

    return x*y

register.simple_tag(multiply)
