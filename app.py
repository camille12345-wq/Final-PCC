import streamlit as st
import pandas as pd
import plotly.express as px

# Generamos 5 páginas en la aplicación web de Streamlit.
# Generamos una página principal, otra donde contaran su experiencia aprendiendo a programar y una tercera donde presentarán sus gráficos.

# Creamos la lista de páginas
paginas = ['Inicio', 'Denuncias', 'Nubes de palabra', 'Gráficos interactivos', 'Mapa interactivo']

# Creamos botones de navegación tomando la lista de páginas
pagina_seleccionada = st.sidebar.selectbox('Selecciona una página', paginas)

# Generamos condicionales para mostrar el contenido de cada página
if pagina_seleccionada == 'Denuncias':

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
    
    # Mostramos el gráfico seleccionado
    if grafico_seleccionado == 'Nube de palabras Ocupaciones Laborales':
        st.markdown("<div style='text-align: justify; font-size: 20px;'>El gráfico muestra la nube de palabras presenta la recopilación de frecuencias recolectadas sobre la base de datos textual a partir de la variable Ocupación laboral.</div>", unsafe_allow_html=True)
        st.image("nube_ocupaciones.png", caption='Nube de palabras Ocupaciones Laborales', width=500)
        pass
    elif grafico_seleccionado == 'Nube de palabras Cargos públicos anteriores':
        st.markdown("<div style='text-align: justify; font-size: 20px;'>El gráfico muestra la nube de palabras presenta la recopilación de frecuencias recolectadas sobre la base de datos textual a partir de la variable Cargo Público previo.</div>", unsafe_allow_html=True)
        st.image("nube_cargos_anteriores.png", caption='Nube de palabras Cargos públicos anteriores', width=500)
        pass
    elif grafico_seleccionado == 'Gráfico de pastel de Nivel de estudios':
        st.markdown("<div style='text-align: justify; font-size: 20px;'>El gráfico de torta interactivo presenta las proporciones de Nivel de estudio alcanzado por cada político.</div>", unsafe_allow_html=True)
        import streamlit.components.v1 as components
        with open("nivel_estudios_torta.html", "r", encoding="utf-8") as f:
            html_content = f.read()
        components.html(html_content, height=500)
        pass
    elif grafico_seleccionado == 'Gráfico de pastel de Netflix':
        st.markdown("<div style='text-align: justify; font-size: 20px;'>El gráfico de pastel muestra los tipos de contenidos audiovisuales en la plataforma Netflix, donde un sector representa el 30.4 porciento de los tipos de contenido pertenecen a TV show, mientras que el otro sector representa que el 69.6 porciento del tipo de contenidos pertenece a las series</div>", unsafe_allow_html=True)
        st.image("pastel_netflix.png", caption='Gráfico de pastel de Netflix', width=500)
        pass
    elif grafico_seleccionado == 'Gráfico de pastel de Netflix':
        st.markdown("<div style='text-align: justify; font-size: 20px;'>El gráfico de pastel muestra los tipos de contenidos audiovisuales en la plataforma Netflix, donde un sector representa el 30.4 porciento de los tipos de contenido pertenecen a TV show, mientras que el otro sector representa que el 69.6 porciento del tipo de contenidos pertenece a las series</div>", unsafe_allow_html=True)
        st.image("pastel_netflix.png", caption='Gráfico de pastel de Netflix', width=500)
        pass
    elif grafico_seleccionado == 'Gráfico de pastel de Netflix':
        st.markdown("<div style='text-align: justify; font-size: 20px;'>El gráfico de pastel muestra los tipos de contenidos audiovisuales en la plataforma Netflix, donde un sector representa el 30.4 porciento de los tipos de contenido pertenecen a TV show, mientras que el otro sector representa que el 69.6 porciento del tipo de contenidos pertenece a las series</div>", unsafe_allow_html=True)
        st.image("pastel_netflix.png", caption='Gráfico de pastel de Netflix', width=500)
        pass
    elif grafico_seleccionado == 'Gráfico de pastel de Netflix':
        st.markdown("<div style='text-align: justify; font-size: 20px;'>El gráfico de pastel muestra los tipos de contenidos audiovisuales en la plataforma Netflix, donde un sector representa el 30.4 porciento de los tipos de contenido pertenecen a TV show, mientras que el otro sector representa que el 69.6 porciento del tipo de contenidos pertenece a las series</div>", unsafe_allow_html=True)
        st.image("pastel_netflix.png", caption='Gráfico de pastel de Netflix', width=500)
        pass
    elif grafico_seleccionado == 'Gráfico de pastel de Netflix':
        st.markdown("<div style='text-align: justify; font-size: 20px;'>El gráfico de pastel muestra los tipos de contenidos audiovisuales en la plataforma Netflix, donde un sector representa el 30.4 porciento de los tipos de contenido pertenecen a TV show, mientras que el otro sector representa que el 69.6 porciento del tipo de contenidos pertenece a las series</div>", unsafe_allow_html=True)
        st.image("pastel_netflix.png", caption='Gráfico de pastel de Netflix', width=500)
        pass
   
