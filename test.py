__author__ = 'pv'

class IndexView(generic.ListView):
    template_name = 'network/index.html'
    context_object_name = 'objects_list'
    model = TreeObject
    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['interfaces'] = Interface.objects.all()
        return context
#