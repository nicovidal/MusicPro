from django.shortcuts import render, redirect
import requests
from requests.exceptions import JSONDecodeError

def obtener_guitarras(request):
    api_url = 'http://127.0.0.1:8000/api/productos/'
    response = requests.get(api_url)

    try:
        data = response.json()
        productos = data.get('productos', [])
    
    except JSONDecodeError:
        productos = []
    
    return render(request, 'productos/instrumentosDeCuerdas/guitarras/guitarras.html', {'productos': productos})

""" !-consumo de api """
#productos

def obtener_productos(request):
    api_url = 'http://127.0.0.1:8000/api/productos/' 
    response = requests.get(api_url) 
    data = response.json()  
    productos = data['productos'] 
    return render(request, 'index.html', {'productos': productos})


def obtener_guitarras_acusticas(request):
    api_url = 'http://127.0.0.1:8000/api/productos/' 
    
    response = requests.get(api_url) 
    data = response.json()  
    productos = data['productos']  
    return render(request, 'productos/instrumentosDeCuerdas/guitarras/guitarrasAcusticas.html', {'productos': productos})

def obtener_guitarras_electricas(request):
    api_url = 'http://127.0.0.1:8000/api/productos/'  
    
    response = requests.get(api_url) 
    data = response.json()  
    productos = data['productos']  
    return render(request, 'productos/instrumentosDeCuerdas/guitarras/guitarrasElectricas.html', {'productos': productos})

def obtener_guitarras_solido(request):
    api_url = 'http://127.0.0.1:8000/api/productos/'  
    response = requests.get(api_url)  
    data = response.json() 
    productos = data['productos']
    return render(request, 'productos/instrumentosDeCuerdas/guitarras/guitarrasCuerpoSolido.html', {'productos': productos})


def obtener_bajos(request):
    api_url = 'http://127.0.0.1:8000/api/productos/'
    response = requests.get(api_url)

    try:
        data = response.json()
        productos = data.get('productos', [])
    
    except JSONDecodeError:
        productos = []
    
    return render(request, 'productos/instrumentosDeCuerdas/bajos/bajos.html', {'productos': productos})
def obtener_bajos_cuatro(request):
    api_url = 'http://127.0.0.1:8000/api/productos/'
    response = requests.get(api_url)

    try:
        data = response.json()
        productos = data.get('productos', [])
    
    except JSONDecodeError:
        productos = []
    
    return render(request, 'productos/instrumentosDeCuerdas/bajos/bajosCuatroCuerdas.html', {'productos': productos})
def obtener_bajos_cinco(request):
    api_url = 'http://127.0.0.1:8000/api/productos/'
    response = requests.get(api_url)

    try:
        data = response.json()
        productos = data.get('productos', [])
    
    except JSONDecodeError:
        productos = []
    
    return render(request, 'productos/instrumentosDeCuerdas/bajos/bajosCincoCuerdas.html', {'productos': productos})

def obtener_bajos_pasivos(request):
    api_url = 'http://127.0.0.1:8000/api/productos/'
    response = requests.get(api_url)

    try:
        data = response.json()
        productos = data.get('productos', [])
    
    except JSONDecodeError:
        productos = []
    
    return render(request, 'productos/instrumentosDeCuerdas/bajos/bajosPasivos.html', {'productos': productos})

def obtener_bajos_activos(request):
    api_url = 'http://127.0.0.1:8000/api/productos/'
    response = requests.get(api_url)

    try:
        data = response.json()
        productos = data.get('productos', [])
    
    except JSONDecodeError:
        productos = []
    
    return render(request, 'productos/instrumentosDeCuerdas/bajos/bajosActivos.html', {'productos': productos})

def obtener_accesorios(request):
    api_url = 'http://127.0.0.1:8000/api/productos/'
    response = requests.get(api_url)

    try:
        data = response.json()
        productos = data.get('productos', [])
    
    except JSONDecodeError:
        productos = []
    
    return render(request, 'productos/accesoriosVarios/accesoriosGeneral.html', {'productos': productos})

def obtener_audifonos(request):
    api_url = 'http://127.0.0.1:8000/api/productos/'
    response = requests.get(api_url)

    try:
        data = response.json()
        productos = data.get('productos', [])
    
    except JSONDecodeError:
        productos = []
    
    return render(request, 'productos/accesoriosVarios/audifonos.html', {'productos': productos})
def obtener_cables(request):
    api_url = 'http://127.0.0.1:8000/api/productos/'
    response = requests.get(api_url)

    try:
        data = response.json()
        productos = data.get('productos', [])
    
    except JSONDecodeError:
        productos = []
    
    return render(request, 'productos/accesoriosVarios/cables.html', {'productos': productos})
def obtener_interfaces(request):
    api_url = 'http://127.0.0.1:8000/api/productos/'
    response = requests.get(api_url)

    try:
        data = response.json()
        productos = data.get('productos', [])
    
    except JSONDecodeError:
        productos = []
    
    return render(request, 'productos/accesoriosVarios/interfaces.html', {'productos': productos})

def obtener_microfonos(request):
    api_url = 'http://127.0.0.1:8000/api/productos/'
    response = requests.get(api_url)

    try:
        data = response.json()
        productos = data.get('productos', [])
    
    except JSONDecodeError:
        productos = []
    
    return render(request, 'productos/accesoriosVarios/microfonos.html', {'productos': productos})

def obtener_mixers(request):
    api_url = 'http://127.0.0.1:8000/api/productos/'
    response = requests.get(api_url)

    try:
        data = response.json()
        productos = data.get('productos', [])
    
    except JSONDecodeError:
        productos = []
    
    return render(request, 'productos/accesoriosVarios/mixers.html', {'productos': productos})

def obtener_monitores(request):
    api_url = 'http://127.0.0.1:8000/api/productos/'
    response = requests.get(api_url)

    try:
        data = response.json()
        productos = data.get('productos', [])
    
    except JSONDecodeError:
        productos = []
    
    return render(request, 'productos/accesoriosVarios/monitores.html', {'productos': productos})

def obtener_parlantes(request):
    api_url = 'http://127.0.0.1:8000/api/productos/'
    response = requests.get(api_url)

    try:
        data = response.json()
        productos = data.get('productos', [])
    
    except JSONDecodeError:
        productos = []
    
    return render(request, 'productos/accesoriosVarios/parlantes.html', {'productos': productos})

def obtener_cabezales(request):
    api_url = 'http://127.0.0.1:8000/api/productos/'
    response = requests.get(api_url)

    try:
        data = response.json()
        productos = data.get('productos', [])
    
    except JSONDecodeError:
        productos = []
    
    return render(request, 'productos/amplificadores/cabezales/cabezales.html', {'productos': productos})

def obtener_cabezales_engl(request):
    api_url = 'http://127.0.0.1:8000/api/productos/'
    response = requests.get(api_url)

    try:
        data = response.json()
        productos = data.get('productos', [])
    
    except JSONDecodeError:
        productos = []
    
    return render(request, 'productos/amplificadores/cabezales/engl.html', {'productos': productos})



def obtener_cabezales_evh(request):
    api_url = 'http://127.0.0.1:8000/api/productos/'
    response = requests.get(api_url)

    try:
        data = response.json()
        productos = data.get('productos', [])
    
    except JSONDecodeError:
        productos = []
    
    return render(request, 'productos/amplificadores/cabezales/evh.html', {'productos': productos})



def obtener_cabezales_marshall(request):
    api_url = 'http://127.0.0.1:8000/api/productos/'
    response = requests.get(api_url)

    try:
        data = response.json()
        productos = data.get('productos', [])
    
    except JSONDecodeError:
        productos = []
    
    return render(request, 'productos/amplificadores/cabezales/marshall.html', {'productos': productos})


def obtener_cabezales_pavey(request):
    api_url = 'http://127.0.0.1:8000/api/productos/'
    response = requests.get(api_url)

    try:
        data = response.json()
        productos = data.get('productos', [])
    
    except JSONDecodeError:
        productos = []
    
    return render(request, 'productos/amplificadores/cabezales/pavey.html', {'productos': productos})

def obtener_cajas(request):
    api_url = 'http://127.0.0.1:8000/api/productos/'
    response = requests.get(api_url)

    try:
        data = response.json()
        productos = data.get('productos', [])
    
    except JSONDecodeError:
        productos = []
    
    return render(request, 'productos/amplificadores/cajas/cajas.html', {'productos': productos})

def obtener_cajas_engl(request):
    api_url = 'http://127.0.0.1:8000/api/productos/'
    response = requests.get(api_url)

    try:
        data = response.json()
        productos = data.get('productos', [])
    
    except JSONDecodeError:
        productos = []
    
    return render(request, 'productos/amplificadores/cajas/engl.html', {'productos': productos})

def obtener_cajas_evh(request):
    api_url = 'http://127.0.0.1:8000/api/productos/'
    response = requests.get(api_url)

    try:
        data = response.json()
        productos = data.get('productos', [])
    
    except JSONDecodeError:
        productos = []
    
    return render(request, 'productos/amplificadores/cajas/evh.html', {'productos': productos})

def obtener_cajas_marshall(request):
    api_url = 'http://127.0.0.1:8000/api/productos/'
    response = requests.get(api_url)

    try:
        data = response.json()
        productos = data.get('productos', [])
    
    except JSONDecodeError:
        productos = []
    
    return render(request, 'productos/amplificadores/cajas/marshall.html', {'productos': productos})

def obtener_cajas_pavey(request):
    api_url = 'http://127.0.0.1:8000/api/productos/'
    response = requests.get(api_url)

    try:
        data = response.json()
        productos = data.get('productos', [])
    
    except JSONDecodeError:
        productos = []
    
    return render(request, 'productos/amplificadores/cajas/pavey.html', {'productos': productos})


def obtener_pianos(request):
    api_url = 'http://127.0.0.1:8000/api/productos/'
    response = requests.get(api_url)

    try:
        data = response.json()
        productos = data.get('productos', [])
    
    except JSONDecodeError:
        productos = []
    
    return render(request, 'productos/instrumentosDeCuerdas/pianos/pianos.html', {'productos': productos})


def obtener_pianolas(request):
    api_url = 'http://127.0.0.1:8000/api/productos/'
    response = requests.get(api_url)

    try:
        data = response.json()
        productos = data.get('productos', [])
    
    except JSONDecodeError:
        productos = []
    
    return render(request, 'productos/instrumentosDeCuerdas/pianos/pianolas.html', {'productos': productos})


def obtener_pianos_entera(request):
    api_url = 'http://127.0.0.1:8000/api/productos/'
    response = requests.get(api_url)

    try:
        data = response.json()
        productos = data.get('productos', [])
    
    except JSONDecodeError:
        productos = []
    
    return render(request, 'productos/pianos/instrumentosDeCuerdas/pianoDeColaEntera.html', {'productos': productos})


def obtener_pianos_media(request):
    api_url = 'http://127.0.0.1:8000/api/productos/'
    response = requests.get(api_url)

    try:
        data = response.json()
        productos = data.get('productos', [])
    
    except JSONDecodeError:
        productos = []
    
    return render(request, 'productos/pianos/instrumentosDeCuerdas/pianoDeMediaCuerda.html', {'productos': productos})

def obtener_baterias_acusticas(request):
    api_url = 'http://127.0.0.1:8000/api/productos/'
    response = requests.get(api_url)

    try:
        data = response.json()
        productos = data.get('productos', [])
    
    except JSONDecodeError:
        productos = []
    
    return render(request, 'productos/percusion/bateriasAcusticas/bateriaAcustica.html', {'productos': productos})

def obtener_baterias_acusticas_mapex(request):
    api_url = 'http://127.0.0.1:8000/api/productos/'
    response = requests.get(api_url)

    try:
        data = response.json()
        productos = data.get('productos', [])
    
    except JSONDecodeError:
        productos = []
    
    return render(request, 'productos/percusion/bateriasAcusticas/mapex.html', {'productos': productos})

def obtener_baterias_acusticas_pearl(request):
    api_url = 'http://127.0.0.1:8000/api/productos/'
    response = requests.get(api_url)

    try:
        data = response.json()
        productos = data.get('productos', [])
    
    except JSONDecodeError:
        productos = []
    
    return render(request, 'productos/percusion/bateriasAcusticas/pearl.html', {'productos': productos})

def obtener_baterias_acusticas_sonor(request):
    api_url = 'http://127.0.0.1:8000/api/productos/'
    response = requests.get(api_url)

    try:
        data = response.json()
        productos = data.get('productos', [])
    
    except JSONDecodeError:
        productos = []
    
    return render(request, 'productos/percusion/bateriasAcusticas/sonor.html', {'productos': productos})

def obtener_baterias_acusticas_tama(request):
    api_url = 'http://127.0.0.1:8000/api/productos/'
    response = requests.get(api_url)

    try:
        data = response.json()
        productos = data.get('productos', [])
    
    except JSONDecodeError:
        productos = []
    
    return render(request, 'productos/percusion/bateriasAcusticas/tama.html', {'productos': productos})

def obtener_baterias_electricas(request):
    api_url = 'http://127.0.0.1:8000/api/productos/'
    response = requests.get(api_url)

    try:
        data = response.json()
        productos = data.get('productos', [])
    
    except JSONDecodeError:
        productos = []
    
    return render(request, 'productos/percusion/bateriasElectricas/bateriasElectrica.html', {'productos': productos})

def obtener_baterias_electrica_alesis(request):
    api_url = 'http://127.0.0.1:8000/api/productos/'
    response = requests.get(api_url)

    try:
        data = response.json()
        productos = data.get('productos', [])
    
    except JSONDecodeError:
        productos = []
    
    return render(request, 'productos/percusion/bateriasElectricas/alesis.html', {'productos': productos})

def obtener_baterias_electrica_roland(request):
    api_url = 'http://127.0.0.1:8000/api/productos/'
    response = requests.get(api_url)

    try:
        data = response.json()
        productos = data.get('productos', [])
    
    except JSONDecodeError:
        productos = []
    
    return render(request, 'productos/percusion/bateriasElectricas/roland.html', {'productos': productos})






