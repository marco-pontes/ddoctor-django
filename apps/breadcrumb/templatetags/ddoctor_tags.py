from django import template
register = template.Library()

def render_breadcrumb(request, nome, url, reset):
    if  'breadcrumb' not in request.session or reset == True:
        request.session['breadcrumb'] = []
    item = {'nome': nome, 'url': url }
    if item not in request.session['breadcrumb']:
        request.session['breadcrumb'].append(item)
    return {'nome' : nome, 'breadcrumb' : request.session['breadcrumb'], 'item' : item}  
  
register.inclusion_tag('tags/breadcrumb.html')(render_breadcrumb)

def render_pagination(request, objects):
    return {'objects': objects}  
  
register.inclusion_tag('tags/pagination.html')(render_pagination)
