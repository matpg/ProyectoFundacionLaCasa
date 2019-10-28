from django.shortcuts import render, redirect
from .models import Voluntario
from .forms import VoluntarioForm
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import authenticate, login
import re 
from .funciones import CalcularEdadVoluntario
from datetime import datetime
from django.shortcuts import get_list_or_404

# Create your views here.

class HomePageView(TemplateView):
    def get(self, request, **kwards):
        return render (request, 'fundacion/index.html', context=None)

class Exito_vista(TemplateView):
    def get(self, request, **kwards):
        return render (request, 'fundacion/crea_exito.html', context=None)


def GestionarVoluntarios(request):
    voluntarios = get_list_or_404(Voluntario)
    print(voluntarios)
    return render(request, 'fundacion/gestion_voluntario.html', {'voluntarios': voluntarios})



def CrearVoluntarioView(request):
    if request.method == 'POST':
        form = VoluntarioForm(request.POST or None)
        if form.is_valid():
            form_data = form.cleaned_data
            nom = form_data.get("nombre")
            em = form_data.get("email")
            rut = form_data.get("rut")
            fecha = form_data.get("fecha")
            celu = form_data.get("celular")
            comuna = form_data.get("comuna")
            obj = Voluntario()
            obj.nombre = nom
            obj.email = em
            obj.rut = rut
            obj.fecha = fecha
            obj.edad = CalcularEdadVoluntario(fecha)
            obj.fecha_incripcion = datetime.now().date()
            if re.match('\d',obj.celular):
                return render(request,'fundacion/crea_error.html', context=None)
            obj.celular = celu
            obj.comuna = comuna
            obj.save()
            return render(request,'fundacion/crea_exito.html', context=None)
        else:
            return render(request,'fundacion/crea_error.html', context=None)
    return render(request, 'fundacion/crear.html', context=None)



###############################prueba grafico###############################

import plotly.graph_objects as go
import dash_core_components as dcc
import plotly.graph_objs as go

"""def CrearGrafico(request):
   fig = go.Figure()

    fig.add_trace(
        go.Scatter(
            x=[1, 2, 3],
            y=[1, 3, 1]))

    fig.show(config={'displayModeBar': True})"""

#############################################################################

def CrearGrafico():
    dcc.Graph(
        figure=go.Figure(
            data=[
                go.Bar(
                    x=[1995, 1996, 1997, 1998, 1999, 2000, 2001, 2002, 2003,
                    2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012],
                    y=[219, 146, 112, 127, 124, 180, 236, 207, 236, 263,
                    350, 430, 474, 526, 488, 537, 500, 439],
                    name='Rest of world',
                    marker=go.bar.Marker(
                        color='rgb(55, 83, 109)'
                    )
                ),
                go.Bar(
                    x=[1995, 1996, 1997, 1998, 1999, 2000, 2001, 2002, 2003,
                    2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012],
                    y=[16, 13, 10, 11, 28, 37, 43, 55, 56, 88, 105, 156, 270,
                    299, 340, 403, 549, 499],
                    name='China',
                    marker=go.bar.Marker(
                        color='rgb(26, 118, 255)'
                    )
                )
            ],
            layout=go.Layout(
                title='US Export of Plastic Scrap',
                showlegend=True,
                legend=go.layout.Legend(
                    x=0,
                    y=1.0
                ),
                margin=go.layout.Margin(l=40, r=0, t=40, b=30)
            )
        ),
        style={'height': 300},
        id='my-graph'
    )  
    dcc.show()
    return render(request, 'fundacion/Index.html', context=None)

    ###########################################################################

import dash
import dash_html_components as html
import dash_core_components as dcc

def CrearGrafico2():
    external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

    app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
    app.layout = html.Div([
        dcc.Dropdown(
            id='my-dropdown',
            options=[
                {'label': 'New York City', 'value': 'NYC'},
                {'label': 'Montreal', 'value': 'MTL'},
                {'label': 'San Francisco', 'value': 'SF'}
            ],
            value='NYC'
        ),
        dcc.Graph(
            id='graph',
            config={
                'showSendToCloud': True,
                'plotlyServerURL': 'https://plot.ly'
            }
        )
    ])


    @app.callback(
        dash.dependencies.Output('graph', 'figure'),
        [dash.dependencies.Input('my-dropdown', 'value')])
    def update_output(value):
        y_array_dict = {
            'NYC': [4,2,3],
            'MTL': [1, 2, 4],
            'SF': [5, 3, 6]
        }
        return {
            'data': [{
                'type': 'scatter',
                'y': y_array_dict[value]
            }],
            'layout': {
                'title': value
            }
        }


    if __name__ == '__main__':
        app.run_server(debug=True)