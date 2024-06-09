from Repositorios.RepositorioEgreso import RepositorioEgreso
from Modelos.Egreso import Egreso
from Repositorios.RepositorioCategoria import RepositorioCategoria
from Modelos.Categoria import Categoria

class ControladorEgreso():

    def __init__(self):
        self.repositorioEgreso = RepositorioEgreso()
        self.repositorioCategoria = RepositorioCategoria()
        print("Creando ControladorEgreso")

    def index(self):
        print("Listar todas los Egresos")
        return self.repositorioEgreso.findAll()

    def create(self, elEgreso):
        print("Crear un Egreso")
        nuevoEgreso = Egreso(elEgreso)
        return self.repositorioEgreso.save(nuevoEgreso)

    def show(self, id):
        elEgreso = Egreso(self.repositorioEgreso.findById(id))
        return elEgreso.__dict__

    def update(self, id, elEgreso):
        egresoActual = Egreso(self.repositorioEgreso.findById(id))
        egresoActual.egreso_codigo = elEgreso["egreso_codigo"]
        egresoActual.egreso_fecha = elEgreso["egreso_fecha"]
        egresoActual.egreso_monto = elEgreso["egreso_monto"]
        egresoActual.egreso_descripcion = elEgreso["egreso_descripcion"]
        return self.repositorioEgreso.save(egresoActual)

    def delete(self, id):
        print("Eliminando un Egreso ", id)
        return self.repositorioEgreso.delete(id)

    """
       Relación categoria A Egreso
    """

    def asignarCategoria(self, id, id_categoria):
        egresoActual = Egreso(self.repositorioEgreso.findById(id))
        categoriaActual = Categoria(self.repositorioCategoria.findById(id_categoria))
        egresoActual.categoria = categoriaActual
        return self.repositorioEgreso.save(egresoActual)