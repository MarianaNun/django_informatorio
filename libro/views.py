from django.shortcuts import render
from .models import Libro

from django.views.generic import DetailView, ListView

# Create your views here.
def listar_todos(request):
	lista = Libro.objects.all().order_by('titulo')
	context = {"lista": lista}
	return render(request, 'listar.html', context)


class ListaLibro(ListView):
	model = Libro
	template_name= 'listar.html'
	paginate_by=3

	def get_queryset(self):
		query= super(ListaLibro, self).get_queryset()
		return query.filter(disponible=True)


def filtrar_por_id(request, id):
	libro = Libro.objects.get(id=id)
	context = {"libro": libro}
	return render(request, 'detalle.html', context)

class DetalleLibro(DetailView):
	model = Libro
	template_name= 'detalle.html'

	def get_queryset(self):
		query= super(DetalleLibro, self).get_queryset()
		return query.filter(disponible=True)

