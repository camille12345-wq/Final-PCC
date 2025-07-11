import streamlit as st
import pandas as pd

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
