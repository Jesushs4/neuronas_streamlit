import streamlit as st

st.image("img/neurona.jpg")
st.title("¡Hola neurona!")

tab1, tab2, tab3 = st.tabs(["Una entrada", "Dos entradas", "Tres entradas y sesgo"])

with tab1:
    
    st.subheader("Una neurona con una entrada y un peso")

    w0 = st.slider("Peso", min_value=0.0, max_value=5.0, value=0.0, key="tab1_slider")
    x0 = st.number_input("Introduzca el valor de la entrada", key="tab1_input")

    if st.button("Calcular salida", key="tab1_button"):
        st.write("La salida de la neurona es:", w0 * x0)

with tab2:
    col1, col2 = st.columns(2)
    
    with col1:

        w0 = st.slider("Peso w$_0$", min_value=0.0, max_value=5.0, value=0.0, key="tab2_slider1")
        x0 = st.number_input("Entrada x$_0$", value=0.0, key="tab2_input1")
    
    with col2:
        w1 = st.slider("Peso w$_1$", min_value=0.0, max_value=5.0, value=0.0, key="tab2_slider2")
        x1 = st.number_input("Entrada x$_1$", value=0.0, key="tab2_input2")
    if st.button("Calcular salida", key="tab2_button"):
        st.write("La salida de la neurona es:", w0 * x0 + w1 * x1)

with tab3:
    col1, col2, col3 = st.columns(3)

    with col1:
        w0 = st.slider("Peso w$_0$", min_value=0.0, max_value=5.0, value=0.0, key="tab3_slider1")
        x0 = st.number_input("Entrada x$_0$", value=0.0, key="tab3_input1")

    with col2:
        w1 = st.slider("Peso w$_1$", min_value=0.0, max_value=5.0, value=0.0, key="tab3_slider2")
        x1 = st.number_input("Entrada x$_1$", value=0.0, key="tab3_input2")

    with col3:
        w2 = st.slider("Peso w$_2$", min_value=0.0, max_value=5.0, value=0.0, key="tab3_slider3")
        x2 = st.number_input("Entrada x$_2$", value=0.0, key="tab3_input3")
    b = st.number_input("Introduzca el valor del sesgo", value=0.0, key="bias")

    if st.button("Calcular salida", key="tab3_button"):
        st.write("La salida de la neurona es:", w0 * x0 + w1 * x1 + w2 * x2 + b)