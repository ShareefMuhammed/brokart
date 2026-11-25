from django import template

<<<<<<< HEAD
register=template.Library()

@register.filter(name='chunks')
def chunks(list_data,chunk_size):
    chunk=[]
    i=0
    for data in list_data:
        chunk.append(data)
        i=i+1
        if i==chunk_size:
            yield chunk
            i=0
            chunk=[]
    if chunk:
        yield chunk
        
=======
register = template.Library()

@register.filter(name='chunks')
def chunks(list_data, chunk_size):
    chunk = []
    i = 0
    for data in list_data:
        chunk.append(data)
        i += 1
        if i == chunk_size:
            yield chunk
            i = 0
            chunk = []
    if chunk:
        yield chunk
>>>>>>> 47f48488ab9d220bc453ea1f9bde29fe7ebeac82
