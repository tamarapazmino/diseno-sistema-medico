from django.contrib import admin
from django.urls import path
from appatencion.views import PacienteView, PacienteRegistroView, \
    DoctorView, HistoriaView, CitaView, AgendaView, HorarioView, RecetaView, AntecedentesView, UsuarioView
from django.conf import settings
app_name = "appatencion"
urlpatterns = [
    path('paciente/', PacienteView.as_view(), name='paciente'),
    path('paciente_registro/', PacienteRegistroView.as_view(), name='pac_r'),
    path('doctor/', DoctorView.as_view(), name='doctor'),
    path('historia-clinica/', HistoriaView.as_view(), name='historia'),
    path('nueva-cita/', CitaView.as_view(), name='cita'),
    path('agenda/', AgendaView.as_view(), name='agenda'),
    path('horario-atencion/', HorarioView.as_view(), name='horario'),
    path('receta-paciente/', RecetaView.as_view(), name='receta'),
    path('antecedentes/', AntecedentesView.as_view(), name='antecedentes'),
    path('usuarios/', UsuarioView.as_view(), name='usuario'),
]
