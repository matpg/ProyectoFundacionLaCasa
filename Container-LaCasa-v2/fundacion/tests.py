from django.test import TestCase
from fundacion.models import Voluntario, Proyecto, Usuario

class ProyectoTestCase(TestCase):
	def setUp(self):
		Proyecto.proyectos.create(id_proyecto=1000,
								nombre="proyecto de testeo",
								descripcion="asdasd",
								jefe="chelo",
								fecha_inicio="01/01/19",
								fecha_termino="01/11/19",
								cantidad_voluntarios=3,
								presupuesto="2000000"
		)

	def test_proyectos_creados(self):
		proyecto_prueba = Proyecto.proyectos.get(nombre="proyecto de testeo")
        self.assertEqual(proyecto_prueba.nombre, "Proyecto creado:" + proyecto_prueba.nombre)


class VoluntarioTestCase(TestCase):
	def setUp(self):
		Voluntario.voluntarios.create(nombre="carlos",
								rut="pérez",
								fecha="02/01/19",
								edad="1",
								proyecto_actividad="proyecto 1",
								celular="91923912",
								comuna="Puente Alto",
								email="carlos.perez@gmail.com",
								fecha_incripcion="01/01/19"

		)

	def test_voluntarios_creados(self):
		voluntario_prueba = Voluntario.voluntarios.get(nombre="carlos")
        self.assertEqual(voluntario_prueba.nombre, "Voluntario creado:" + voluntario_prueba.nombre)


class UsuarioTestCase(TestCase):
	def setUp(self):
		Usuario.usuarios.create(nombre="felipe",
								apellidos="poblete",
								email="felipe.poblete@gmail.com",
								id_proyecto="2"
		)
	def test_usuario_creados(self):
		usuario_prueba = Usuario.usuarios.get(nombre="felipe")
        self.assertEqual(usuario_prueba.nombre, "Usuario creado:" + usuario_prueba.nombre)
        