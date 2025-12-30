import streamlit as st
from PIL import Image
import matplotlib.pyplot as plt

st.title('タイトル')
st.caption('内容')

col1, col2 = st.columns(2)

with col1:
    st.subheader('自己紹介')
    st.text('ゆるくゲーム制作をしているまままと申します')

    code = '''
    import stream as st

    st.title('タイトル')
    '''
    st.code(code, language='python')

    image = Image.open('./data/miku.png')
    st.image(image, width=400)

with col2:
    with st.form(key='profile_form'):
        name = st.text_input('名前')
        address = st.text_input('住所')

        age_category = st.radio(
            '年齢層',
            ('子供（18歳未満）', '大人（18歳以上）'))
        hobby = st.multiselect('趣味',('スポーツ','学問','芸術','会話'))
        
        submit_btn = st.form_submit_button('送信')
        cancel_btn = st.form_submit_button('キャンセル')
        if submit_btn and name != '' and address != '':
            st.text(f'ようこそ！{name}さん！書籍を{address}へ送りました')
            st.text(f'年齢層:{age_category}')
            st.text(f'{"と".join(hobby)}が好きなんですね')
        elif cancel_btn:
            pass
        else:
            st.text('フォームを入力してください')
#streamlit run streamlit.py