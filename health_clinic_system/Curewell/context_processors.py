from Curewell.models import Department


def my_links(request):
    links=Department.objects.all()
    return dict(links=links)