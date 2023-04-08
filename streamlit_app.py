import numpy as np
import altair as alt
import pandas as pd
import streamlit as st


st.title('Kajome Learning Material :flag-rw:')
st.header('st.write')

# Example 1

st.write(':sunglasses: Hello, **World!** :+1:')
st.header('This is a header')
st.header('A header with _italics_ :blue[colors] and emojis :sunglasses:')

# Example 2

st.write(1234)
st.markdown("Streamlit is **_really_ cool**. It's like drinking :coffee:")
st.markdown("This text is :red[colored red], and this is **:blue[colored]** and bold.", help=('This will display information about a certain text or argument in a code'))
st.markdown(":green[$\sqrt{x^2+y^2}=1$] is a Pythagorean identity. :pencil:")

# Example 3

df = pd.DataFrame({
     'first column': [1, 2, 3, 4],
     'second column': [10, 20, 30, 40]
     })
st.write(df)
st.caption('This is a string that explains something above.')
st.caption('A caption with _italics_ :blue[colors] and emojis :sunglasses:')

# Example 4

st.write('Below is a DataFrame:', df, 'Above is a dataframe.')

# Example 5

df2 = pd.DataFrame(
     np.random.randn(200, 3),
     columns=['a', 'b', 'c'])
c = alt.Chart(df2).mark_circle().encode(
     x='a', y='b', size='c', color='c', tooltip=['a', 'b', 'c'])
st.write(c)

# Example 6

code = '''def hello():
    print("Hello, Streamlit!")'''
st.code(code, language='python', line_numbers=True)
