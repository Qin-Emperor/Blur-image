import streamlit as st
from PIL import Image, ImageFilter
import io

st.header("*:red[Выберите вашу фотографию]*")

data = st.file_uploader(label=' ',type=['jpeg', 'png', 'jpg'])

sw = st.slider(label='Выберите размытие', min_value=1, max_value=20)

if data is not None:
    image = Image.open(data)

    # Применяем размытие
    blurred_image = image.filter(ImageFilter.BoxBlur(sw))

    # Отображение размытого изображения
    st.image(blurred_image)

    # Сохранение размытого изображения в буфер
    buffered = io.BytesIO()
    blurred_image.save(buffered, format="PNG")

    # Предоставление возможности пользователю скачать размытое изображение
    st.download_button(label='Скачайте фотографию', data=buffered.getvalue(), file_name='blurred_image.png')
