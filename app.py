import streamlit as st
from functions import cb_find, save_file
import pandas as pd
import numpy as np

st.set_page_config(layout='wide')


title_1, title_2, title_3 = st.columns([1,1,1])
with title_2:
    st.title("Diyainfotech QC")

st.text('')


uploaded_csv = None
uploaded_csv = st.file_uploader("Upload CSV here: ", 
                                accept_multiple_files = False, 
                                type = ['csv'] )

#upload file
file_path = "Inputs/data.csv"
if uploaded_csv is not None:
    with open(file_path, "wb") as f:
        f.write(uploaded_csv.getbuffer())


if uploaded_csv:
    # uploaded_csv = pd.DataFrame(uploaded_csv, index=None)
    file_path = "Inputs/data.csv"
    if uploaded_csv is not None:
        df = pd.read_csv('Inputs/data.csv', index_col = False)
        if df is not None:
            df_columns = list(df.columns)
            dic = dict()
            for col in df_columns:
                df[col] = df[col].astype('str')
                options = list(df[col].unique())
                options.append("None")
                dic[col] = st.multiselect(label=col,options=options)
            # st.write(dic)
            # filter = st.button("Filter")
            # if filter:
            new_df = df.copy()
            for i,j in zip(dic.keys(),dic.values()):
                # st.write(i)
                # st.write(j)
                if len(j) != 0:
                    new_df = new_df[new_df[i].isin(j)]
            # st.write(new_df)
            new_df['compare_url'] = new_df['CB_URL'].str.replace("/organization/", "/compare/organization/")
            # st.write(new_df['compare_url'])
            st.write(new_df)

            exist_statuses = ['Updated (Tier 0)',
                                'Updated (Tier 1)',
                                'Updated (Tier 2)',
                                'Correct data point exists']
            not_exist_statuses = ['No data found']

            
            data_cols = new_df.columns
            mistakes = pd.DataFrame(columns=data_cols)
            placeholder = st.empty()
            for i in range(0,new_df.shape[0]):
                compare_url = new_df['compare_url'].iloc[i]
                status = new_df['Status'].iloc[i]
                placeholder.write(f"scanning row: {i}/{new_df.shape[0]}")
                if status in exist_statuses:
                    res = cb_find(compare_url, 'Emp Range Freshness Q1 2025 - verified')
                elif status in not_exist_statuses:                    
                    res = cb_find(compare_url, 'Emp Range Freshness Q1 2025 - Not Found')
                else:
                    res = None
                
                if res == False:
                    mistakes.loc[mistakes.shape[0]] = new_df.iloc[i]
            if mistakes is not None:
                st.write(mistakes)
    try:

        pass
    except Exception as e:
        st.text(f"Error: {str(e)}")

    pass



