import streamlit as st

# Título de la pestaña
st.set_page_config(page_title="El Origen de los Juegos", page_icon="🎮")

# Encabezado principal
st.title("🕹️ El Origen de los Juegos")
st.subheader("Un viaje en el tiempo a través del entretenimiento")

st.write("Explora los tableros y pantallas que lo iniciaron todo sin instalar nada.")
st.divider()

# --- SECCIÓN 1: EGIPTO ---
st.header("🏛️ 1. El Senet (Egipto, 3100 a.C.)")
col1, col2 = st.columns(2)

with col1:
    st.write(
        "Es uno de los juegos de mesa más antiguos del mundo. Jugado por faraones, "
        "consistía en un tablero de 30 casillas. Tenía un profundo significado religioso, "
        "ya que se creía que ganar ayudaba al alma en su viaje al más allá."
    )
with col2:
    st.image(
        "https://wikimedia.org", 
        caption="Tablero egipcio de Senet conservado en un museo.",
        use_container_width=True
    )

st.divider()

# --- SECCIÓN 2: VIDEOJUEGOS ---
st.header("📺 2. El Éxito de Atari Pong (1972)")
col3, col4 = st.columns(2)

with col3:
    st.write(
        "Desarrollado por Allan Alcorn para la compañía Atari, Pong se convirtió en el "
        "primer videojuego de éxito comercial masivo de la historia, popularizando las "
        "míticas máquinas de arcade que funcionaban con monedas."
    )
with col4:
    st.image(
        "https://wikimedia.org",
        caption="La legendaria máquina recreativa de Pong.",
        use_container_width=True
    )

st.divider()
st.caption("Página web creada 100% en la nube con Python 🚀")
