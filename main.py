import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import time

st.title('Streamlit 超入門')

st.write('プレグレスバーの表示')
'Start!!'

latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f'iteration{i+1}')
    bar.progress(i+1)
    time.sleep(0.1)

left_column,right_column= st.columns(2)
button = left_column.button('右カラムに文字を表示')
if button:
    right_column.write('ここは右カラム')




expander1= st.expander('問い合わせ１')
expander1.write('問い合わせ１の回答')
expander2= st.expander('問い合わせ2')
expander2.write('問い合わせ2の回答')
# if st.checkbox('Show image'):
#     img = Image.open('profil.jpg')
#     st.image(img, caption='Yuta Suzuki',use_column_width=True)

# text = st.text_input('あなたの趣味を教えてください')
# condition = st.slider('あなたの今の調子は？',0,100,50)

# 'あなたの趣味は：',text,'です'
# 'コンディション',condition