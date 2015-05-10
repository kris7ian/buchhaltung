from django import template
from bilanz.templatetags.totalSum import totalSum

register = template.Library()

def gewinnVerlust():

        gewinn = totalSum('A', False) - totalSum('P', False)
        return int(gewinn * 100) / 100

register.simple_tag(gewinnVerlust)