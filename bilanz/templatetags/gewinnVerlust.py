from django import template
from bilanz.templatetags.kontoSum import totalSum

register = template.Library()

def gewinnVerlust(aktiv):

    if aktiv == True:

        difference = totalSum('A', True) - totalSum('P', True)
        if difference > 0:
            return
        else:
            return difference

    else:

        difference = totalSum('A', True) - totalSum('P', True)
        if difference < 0:
            return
        else:
            return difference

register.simple_tag(gewinnVerlust)