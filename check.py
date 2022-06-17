# -*- coding: utf-8 -*-
"""
Created on Sun May 29 22:11:39 2022

@author: Abhra
"""
import streamlit as st
import time

with st.spinner('Wait for it...'):
    time.sleep(5)
st.success('Done!')
