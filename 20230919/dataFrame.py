import pandas as pd
import streamlit as st

df = pd.DataFrame(
    [
        {"command": "st.selectbox", "rating": 4, "is_widget": True},
        {"command": "st.balloons", "rating": 5, "is_widget": False},
        {"command": "st.time_input", "rating": 3, "is_widget": True},
        {"command": "st.slider", "rating": 2, "is_widget": True,"avator":"http://192.168.31.92/E:/Streamlit框架/20230919/imgs/1.jpg"}
    ]
)

# st.dataframe(df, use_container_width=True)

edited_df = st.data_editor(df,
                           num_rows="dynamic",
                           column_config={
                               "avator": st.column_config.ImageColumn(
                                   "Preview Image",help="This is a preview image"
                               )
                           }) # 👈 An editable dataframe

favorite_command = edited_df.loc[edited_df["rating"].idxmax()]["command"]
st.markdown(f"Your favorite command is **{favorite_command}** 🎈")
