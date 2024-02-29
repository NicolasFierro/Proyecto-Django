from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
layout = """
        <h1>Sitio Web con Django | Nicolas Fierro</h1>
        </hr>
        <ul>
            <li>
                <a href="/holaMundo">Hola Mundo</a>
            </li>

            <li>
                <a href="/saludo">Saludo</a>
            </li>

            <li>
                <a href="/Inicio">Inicio</a>
            </li>

            <li>
                <a href="/presentacion">Presentacion</a>
            </li>

            <li>
                <a href="/contacto">Contacto</a>
            </li>

        </ul>
        """


def holaMundo(request):
    return render(request, 'holaMundo.html')


def saludo(request, redirigir=0):
    if redirigir == 1:
        return redirect('Contacto', nombre="Nicolas")
    return render(request, 'contacto.html')


def index(request):
    añosPares = []
    añosViciesto = []
    year = 2024
    while year <= 2050:
        if year % 2 == 0:
            añosPares.append(year)
        if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
            añosViciesto.append(year)
        year += 1

    even_years_html = "<h2>AÑOS PARES:</h2><ul>"
    for year in añosPares:
        even_years_html += f"<li>{year}</li>"
    even_years_html += "</ul>"

    leap_years_html = "<h2>AÑOS VICIESTOS:</h2><ul>"
    for year in añosViciesto:
        leap_years_html += f"<li>{year}</li>"
    leap_years_html += "</ul>"
    Nombre = 'Nicolas Fierro'

    # Ejemplo de ciclo for para generar una lista de marcas de vehiculos
    marcas = ["Land Rover", "Porsche", "Tesla", "Mazda", "Hyundai", "Audi", "Kia"]

    # Ejemplo de ciclo while para generar los numeros pares
    pares = []
    num = 0
    while num <= 10:
        pares.append(num)
        num += 2

    nombres = ['Alice', 'Bob', 'Charlie', 'David', 'Eve']
    i = 0
    nombres_while = []
    while i < len(nombres):
        nombres_while.append(nombres[i])
        i += 1

    year=2024
    hasta= range(year,2050)

    lenguajes=['JavaScript', 'Python', 'PHP', 'C']
    lenguajes=['PHP']
    

    template = f"""
                    <h1>Inicio</h1>
                    <p>Años pares y años bisiestos desde 2024 hasta 2050:</p>
                    {even_years_html}
                    {leap_years_html}
                """

    return render(request, 'index.html', {
        'mi_variable': 'Soy un dato que esta en la vista',
        'title': 'Inicio del sitio',
        'titulo': 'Pagina Inicio SENA',
        'name': Nombre,
        'marcas': marcas,
        'pares': pares,
        'nombres_while': nombres_while,
        'lenguajes': lenguajes,
        'añosPares': añosPares,
        'years': hasta,
    })


def presentacion(request):
    return render(request, 'presentacion.html')


def contacto(request, nombre="", apellido=""):
    aprendiz = ""
    if nombre and apellido:
        aprendiz = "<h2> Nombre completo: </h2>"
        aprendiz += f"<h3> {nombre} {apellido} </h3>"
    elif nombre:
        aprendiz = "<h2>Nombre sin apellido</h2>"
        aprendiz += f"<h2> Bienvenido {nombre}</h2>"
    elif apellido:
        aprendiz = "<h2>Apellido sin nombre</h2>"
        aprendiz += f"<h2> Bienvenido {apellido}</h2>"
    else:
        aprendiz = "<h2> Sin nombre y apellidos definidos</h2>"

    return render(request, 'contacto.html', {'aprendiz': aprendiz})


def quienesSomos(request):
    return render(request, 'quienesSomos.html')


def productAndServices(request):
    return render(request, 'productAndServices.html')

def pagina(request, redirigir = 0):
    if redirigir == 1:
        return redirect('contacto', nombre= "Ana", apellidos="Perez")
    return render(request, 'pagina.html',{'texto': 'Este es mi texto',  'lista': ['uno','dos','tres'],})
