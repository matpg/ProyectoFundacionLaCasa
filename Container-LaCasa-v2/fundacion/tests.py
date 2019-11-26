from django.test import TestCase
from fundacion.models import Voluntario, Proyecto, Usuario


class VoluntarioTestCase(TestCase):
	def setUp(self):
		Proyecto.proyectos.create(name="carlos")
        Proyecto.proyectos.create(name="americo")

	def test_voluntarios_creados(self):
		vol_1 = Proyecto.proyectos.get(name="carlos")
        vol_2 = Proyecto.proyectos.get(name="americo")
        self.assertEqual(vol_1.nombre, 'The lion says "roar" and carlos')
        self.assertEqual(vol_2.nombre, 'The cat says "meow" and americo')
