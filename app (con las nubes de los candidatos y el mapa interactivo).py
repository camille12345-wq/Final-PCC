import streamlit as st
import pandas as pd
import plotly.express as px

# Generamos 5 páginas en la aplicación web de Streamlit.
# Generamos una página principal

# Creamos la lista de páginas
paginas = ['Inicio', 'Denuncias', 'Nubes de palabra', 'Gráficos interactivos', 'Mapa interactivo']

# Creamos botones de navegación tomando la lista de páginas
pagina_seleccionada = st.sidebar.selectbox('Selecciona una página', paginas)

# Generamos condicionales para mostrar el contenido de cada página
if pagina_seleccionada == "Inicio":
    # Fondo superior
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("https://radiouno.pe/wp-content/uploads/2024/06/standard_standard_FACHADA_DEL_MINISTERIO__2__2_.jpg");
            background-size: cover;
            background-repeat: no-repeat;
            background-attachment: fixed;
            background-position: center;
        }}
        .titulo {{
            background-color: rgba(255, 255, 255, 0.85);
            padding: 2rem;
            border-radius: 15px;
            margin-top: 3rem;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )
    #Título personalizado
    st.markdown(
    "<h1 style='padding: 15px; border-radius: 10px; text-align: center;'>"
    "<span style='color: #660000;'>Portal</span> "
    "<span style='color: black;'>de</span> "
    "<span style='color: #660000;'>Transparencia</span> "
    "<span style='color: black;'>Electoral</span> "
    "<span style='color: #660000;'>2026</span>"
    "</h1>",
    unsafe_allow_html=True
)
     # Estructura en columnas para centrar el contenido
    col1, col2, col3 = st.columns([1, 2, 1])

    with col2:
        # Texto de bienvenida centrado
        st.markdown("""
        <div style='background-color: white; padding: 20px; border-radius: 10px; color: black; text-align: center;'>
            <p style='font-size: 18px;'>
                Bienvenido al <strong>Portal de Transparencia</strong>, una herramienta ciudadana para conocer la trayectoria de los candidatos presidenciales del 2026 en Perú.<br><br>
                Podrás revisar denuncias, ocupación, ingresos, experiencia política y más.
            </p>
        </div>
        """, unsafe_allow_html=True)

        # Botón centrado dentro de la columna
        st.write('---')
        st.markdown("<div style='text-align: center;'>", unsafe_allow_html=True)
    if st.button("🔍 Ver candidatos"):
        st.markdown("<p style='background-color: white; text-align: center; color: black;'>Haz clic en 'Denuncias' en el menú lateral izquierdo para ver la información de los candidatos.</p>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)
#Apartado de denuncias
elif pagina_seleccionada == 'Denuncias':

    # Cargar el archivo Excel
    df = pd.read_excel('excel_base_de_datos.xlsx')

    # Menú desplegable con los nombres
    politico = st.selectbox('Selecciona una figura política', df['Nombre'].unique())

    # Filtrar datos del político seleccionado
    datos = df[df['Nombre'] == politico].iloc[0]

    # Dividir en dos columnas: foto a la izquierda, datos a la derecha
    col1, col2 = st.columns([1, 2])

    with col1:
        st.image(datos['url_foto'], width=200)

    with col2:
        st.write(f"## {datos['Nombre']}")
        st.write(f"**DNI:** {datos['DNI']}")
        st.write(f"**Partido:** {datos['Partido']}")
        st.write(f"**Lugar de nacimiento:** {datos['Lugar de nacimiento']}")

    # Crear un DataFrame con los datos de denuncias
    denuncias_data = pd.DataFrame({
        'Código': [datos['Código']],
        'Nombre': [datos['Nombre']],
        'Número de denuncias': [datos['# de denuncias encontrado']],
        'Tipo de denuncia más frecuente': [datos['Tipo de denuncia más frecuente ']],
        'URL de la denuncia': [datos['URL tipo noticia más frecuente']]
    })

    # Mostrar la tabla
    st.write('---')
    st.write("### Información sobre denuncias")
    st.dataframe(denuncias_data)

    # Nota aclaratoria
    st.write("*Para ver la denuncia, copie y pegue el enlace en su navegador.*")
    
elif  pagina_seleccionada == 'Gráficos interactivos':

    # Agregamos un título
    st.markdown("<h1 style='text-align: center;'>Gráficos interactivos y comparación de variables en figuras políticas</h1>", unsafe_allow_html=True)
    
    # Creamos una lista de gráficos
    graficos = ['Nube de palabras Ocupaciones Laborales','Nube de palabras Cargos públicos anteriores', 'Gráfico de pastel de Nivel de estudios', 'Gráfico de pastel de Conocimiento de Lenguas originarias', 'Gráfico de dispersión de Ingresos anuales y Nivel de estudios', 'Gráfico de barras de Cargos públicos previos', 'Gráfico de barras de Inmuebles y Muebles', 'Treemap comparativo Ocupación e Ingresos']

    # Creamos un cuadro de selección en la página de gráficos
    grafico_seleccionado = st.selectbox('Selecciona un gráfico', graficos)

    st.write('---')
    
    # Mostramos el gráfico seleccionado
    if grafico_seleccionado == 'Nube de palabras Ocupaciones Laborales':
        st.markdown("<div style='text-align: justify; font-size: 20px;'>El gráfico muestra una nube de palabras que presenta la recopilación de frecuencias recolectadas sobre la base de datos textual a partir de la variable Ocupación laboral.</div>", unsafe_allow_html=True)
        st.image("nube_ocupaciones.png", caption='Nube de palabras Ocupaciones Laborales', width=600)
        pass
    elif grafico_seleccionado == 'Nube de palabras Cargos públicos anteriores':
        st.markdown("<div style='text-align: justify; font-size: 20px;'>El gráfico muestra una nube de palabras que presenta la recopilación de frecuencias recolectadas sobre la base de datos textual a partir de la variable Cargo Público previo.</div>", unsafe_allow_html=True)
        st.image("nube_cargos_anteriores.png", caption='Nube de palabras Cargos públicos anteriores', width=600)
        pass
    elif grafico_seleccionado == 'Gráfico de pastel de Nivel de estudios':
        st.markdown("<div style='text-align: justify; font-size: 20px;'>El gráfico de torta interactivo presenta las proporciones de Nivel de estudio alcanzado por cada político.</div>", unsafe_allow_html=True)
        import streamlit.components.v1 as components
        with open("nivel_estudios_torta.html", "r", encoding="utf-8") as f:
            html_content = f.read()
        components.html(html_content, height=500)
        pass
    elif grafico_seleccionado == 'Gráfico de pastel de Conocimiento de Lenguas originarias':
        st.markdown("<div style='text-align: justify; font-size: 20px;'>El gráfico de torta interactivo presenta las proporciones en Conocimientos de Lenguas originarias por cada político.</div>", unsafe_allow_html=True)
        import streamlit.components.v1 as components
        with open("lenguas_originarias_torta.html", "r", encoding="utf-8") as f:
            html_content = f.read()
        components.html(html_content, height=500)
        pass
    elif grafico_seleccionado == 'Gráfico de dispersión de Ingresos anuales y Nivel de estudios':
        st.markdown("<div style='text-align: justify; font-size: 20px;'>El gráfico de dispersión interactivo presenta una comparativa entre las variables de Ingresos anuales y Nivel de estudios alcanzado por cada político.</div>", unsafe_allow_html=True)
        import streamlit.components.v1 as components
        with open("dispersión_ingresos.html", "r", encoding="utf-8") as f:
            html_content = f.read()
        components.html(html_content, height=500)
        pass
    elif grafico_seleccionado == 'Gráfico de barras de Inmuebles y Muebles':
        st.markdown("<div style='text-align: justify; font-size: 20px;'>El gráfico de barras interactivo presenta una comparativa entre la cantidad de Inmuebles y muebles declarados por cada político.</div>", unsafe_allow_html=True)
        import streamlit.components.v1 as components
        with open("barras_inmuebles.html", "r", encoding="utf-8") as f:
            html_content = f.read()
        components.html(html_content, height=500)
        pass
    elif grafico_seleccionado == 'Treemap comparativo Ocupación e Ingresos':
        st.markdown("<div style='text-align: justify; font-size: 20px;'>El gráfico Treemap interactivo presenta una comparativa entre la Ocupación laboral y el Ingreso anual por cada político.</div>", unsafe_allow_html=True)
        import streamlit.components.v1 as components
        with open("ocupacion_ingresos_treemap2.html", "r", encoding="utf-8") as f:
            html_content = f.read()
        components.html(html_content, height=500)
        pass

elif  pagina_seleccionada == 'Nubes de palabra':

    # Agregamos un título
    st.markdown("<h1 style='text-align: center;'>Nubes de palabras: Recopilación de palabras más asociadas a las figuras políticas</h1>", unsafe_allow_html=True)
    
    # Creamos una lista de gráficos
    graficos_nube = ['Nube de palabras César Acuña Peralta','Nube de palabras Rafael López Aliaga', 'Nube de palabras Keiko Fujimori', 'Nube de palabras Alfonso López-Chau', 'Nube de palabras Fernando Olivera', 'Nube de palabras Veronika Mendoza', 'Nube de palabras Martín Vizcarra', 'Nube de palabras Vladimir Cerrón', 'Nube de palabras George Forsyth', 'Nube de palabras Dina Boluarte', 'Nube de palabras Adriana Tudela', 'Nube de palabras Guido Bellido', 'Nube de palabras Julio Guzmán', 'Nube de palabras Modesto Montoya', 'Nube de palabras Jorge Pérez', 'Nube de palabras Yohny Lescano']

    # Creamos un cuadro de selección en la página de gráficos
    grafico_seleccionado_nube = st.selectbox('Selecciona un gráfico', graficos_nube)
    
    st.write('---')
    
    # Mostramos el gráfico seleccionado
    if grafico_seleccionado_nube == 'Nube de palabras César Acuña Peralta':
        st.markdown("<div style='text-align: justify; font-size: 20px;'>El gráfico muestra una nube de palabras que presenta la recopilación de frecuencias recolectadas sobre la base de noticias relacionadas con las palabras clave con mayor asociación al político.</div>", unsafe_allow_html=True)
        st.image("nube_palabras_acuña.png", caption='Nube de palabras César Acuña Peralta', width=600)
        pass
    elif grafico_seleccionado_nube == 'Nube de palabras Rafael López Aliaga':
        st.markdown("<div style='text-align: justify; font-size: 20px;'>El gráfico muestra una nube de palabras que presenta la recopilación de frecuencias recolectadas sobre la base de noticias relacionadas con las palabras clave con mayor asociación al político.</div>", unsafe_allow_html=True)
        st.image("nube_palabras_aliaga.png", caption='Nube de palabras Rafael López Aliaga', width=600)
        pass
    elif grafico_seleccionado_nube == 'Nube de palabras Rafael Keiko Fujimori':
        st.markdown("<div style='text-align: justify; font-size: 20px;'>El gráfico muestra una nube de palabras que presenta la recopilación de frecuencias recolectadas sobre la base de noticias relacionadas con las palabras clave con mayor asociación al político.</div>", unsafe_allow_html=True)
        st.image("nube_palabras_keiko.png", caption='Nube de palabras Keiko Fujimori', width=600)
        pass
    elif grafico_seleccionado_nube == 'Nube de palabras Alfonso López-Chau':
        st.markdown("<div style='text-align: justify; font-size: 20px;'>El gráfico muestra una nube de palabras que presenta la recopilación de frecuencias recolectadas sobre la base de noticias relacionadas con las palabras clave con mayor asociación al político.</div>", unsafe_allow_html=True)
        st.image("nube_palabras_lopezchau.png", caption='Nube de palabras Alfonso López-Chau', width=600)
        pass
    elif grafico_seleccionado_nube == 'Nube de palabras Fernando Olivera':
        st.markdown("<div style='text-align: justify; font-size: 20px;'>El gráfico muestra una nube de palabras que presenta la recopilación de frecuencias recolectadas sobre la base de noticias relacionadas con las palabras clave con mayor asociación al político.</div>", unsafe_allow_html=True)
        st.image("nube_palabras_olivera.png", caption='Nube de palabras Fernando Olivera', width=600)
        pass
    elif grafico_seleccionado_nube == 'Nube de palabras Veronika Mendoza':
        st.markdown("<div style='text-align: justify; font-size: 20px;'>El gráfico muestra una nube de palabras que presenta la recopilación de frecuencias recolectadas sobre la base de noticias relacionadas con las palabras clave con mayor asociación al político.</div>", unsafe_allow_html=True)
        st.image("nube_palabras_veronika.png", caption='Nube de palabras Veronika Mendoza', width=600)
        pass
    elif grafico_seleccionado_nube == 'Nube de palabras Martín Vizcarra':
        st.markdown("<div style='text-align: justify; font-size: 20px;'>El gráfico muestra una nube de palabras que presenta la recopilación de frecuencias recolectadas sobre la base de noticias relacionadas con las palabras clave con mayor asociación al político.</div>", unsafe_allow_html=True)
        st.image("nube_palabras_vizcarra.png", caption='Nube de palabras Martín Vizcarra', width=600)
        pass
    elif grafico_seleccionado_nube == 'Nube de palabras Vladimir Cerrón':
        st.markdown("<div style='text-align: justify; font-size: 20px;'>El gráfico muestra una nube de palabras que presenta la recopilación de frecuencias recolectadas sobre la base de noticias relacionadas con las palabras clave con mayor asociación al político.</div>", unsafe_allow_html=True)
        st.image("nube_palabras_vladimircerron.png", caption='Nube de palabras Vladimir Cerrón', width=600)
        pass
    elif grafico_seleccionado_nube == 'Nube de palabras George Forsyth':
        st.markdown("<div style='text-align: justify; font-size: 20px;'>El gráfico muestra una nube de palabras que presenta la recopilación de frecuencias recolectadas sobre la base de noticias relacionadas con las palabras clave con mayor asociación al político.</div>", unsafe_allow_html=True)
        st.image("nube_george_forsyth.png", caption='Nube de palabras George Forsyth', width=600)
        pass
    elif grafico_seleccionado_nube == 'Nube de palabras Dina Boluarte':
        st.markdown("<div style='text-align: justify; font-size: 20px;'>El gráfico muestra una nube de palabras que presenta la recopilación de frecuencias recolectadas sobre la base de noticias relacionadas con las palabras clave con mayor asociación a la política.</div>", unsafe_allow_html=True)
        st.image("nube_palabras_dina.png", caption='Nube de palabras Dina Boluarte', width=600)
        pass
    elif grafico_seleccionado_nube == 'Nube de palabras Adriana Tudela':
        st.markdown("<div style='text-align: justify; font-size: 20px;'>El gráfico muestra una nube de palabras que presenta la recopilación de frecuencias recolectadas sobre la base de noticias relacionadas con las palabras clave con mayor asociación a la política.</div>", unsafe_allow_html=True)
        st.image("nube_adriana_tudela.png", caption='Nube de palabras Adriana Tudela', width=600)
        pass
    elif grafico_seleccionado_nube == 'Nube de palabras Guido Bellido':
        st.markdown("<div style='text-align: justify; font-size: 20px;'>El gráfico muestra una nube de palabras que presenta la recopilación de frecuencias recolectadas sobre la base de noticias relacionadas con las palabras clave con mayor asociación al político.</div>", unsafe_allow_html=True)
        st.image("nube_guido_bellido.png", caption='Nube de palabras Guido Bellido', width=600)
        pass
    elif grafico_seleccionado_nube == 'Nube de palabras Julio Guzmán':
        st.markdown("<div style='text-align: justify; font-size: 20px;'>El gráfico muestra una nube de palabras que presenta la recopilación de frecuencias recolectadas sobre la base de noticias relacionadas con las palabras clave con mayor asociación al político.</div>", unsafe_allow_html=True)
        st.image("nube_julio_guzman.png", caption='Nube de palabras Julio Guzmán', width=600)
        pass
    elif grafico_seleccionado_nube == 'Nube de palabras Modesto Montoya':
        st.markdown("<div style='text-align: justify; font-size: 20px;'>El gráfico muestra una nube de palabras que presenta la recopilación de frecuencias recolectadas sobre la base de noticias relacionadas con las palabras clave con mayor asociación al político.</div>", unsafe_allow_html=True)
        st.image("nube_modesto_montoya.png", caption='Nube de palabras Modesto Montoya', width=600)
        pass
    elif grafico_seleccionado_nube == 'Nube de palabras Jorge Pérez':
        st.markdown("<div style='text-align: justify; font-size: 20px;'>El gráfico muestra una nube de palabras que presenta la recopilación de frecuencias recolectadas sobre la base de noticias relacionadas con las palabras clave con mayor asociación al político.</div>", unsafe_allow_html=True)
        st.image("nube_de_palabras_jorge.png", caption='Nube de palabras Jorge Pérez', width=600)
        pass
    elif grafico_seleccionado_nube == 'Nube de palabras Yohny Lescano':
        st.markdown("<div style='text-align: justify; font-size: 20px;'>El gráfico muestra una nube de palabras que presenta la recopilación de frecuencias recolectadas sobre la base de noticias relacionadas con las palabras clave con mayor asociación al político.</div>", unsafe_allow_html=True)
        st.image("nube_lescano.png", caption='Nube de palabras Yohny Lescano', width=600)
        pass

elif pagina_seleccionada == 'Mapa interactivo':
    st.markdown("<h1 style='text-align: center;'>Mapa interactivo por lugar de nacimiento</h1>", unsafe_allow_html=True)
    st.markdown("<div style='text-align: justify; font-size: 20px;'>Explora en este mapa interactivo los lugares de nacimiento de los candidatos presidenciales del 2026.</div>", unsafe_allow_html=True)
    import streamlit.components.v1 as components
    try:
        with open("mapa_politicos.html", "r", encoding="utf-8") as f:
            html_content = f.read()
        components.html(html_content, height=700)
    except FileNotFoundError:
        st.error("No se encontró el archivo 'mapa_politicos.html'. Asegúrate de haberlo subido correctamente al repositorio.")
     # La función components.html toma como primer argumento el contenido HTML que se desea mostrar.
    # En este caso, el contenido HTML se lee desde el archivo "mapa_politicos.html".
    # El argumento height se utiliza para especificar la altura del contenido HTML, en este caso 700 píxeles.
