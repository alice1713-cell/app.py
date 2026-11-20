# app.py
import random import streamlit as st st.title("🍱 오늘의 점심 메뉴 추천기") menus = [     "김치찌개", "된장찌개", "제육볶음", "비빔밥", "국밥",     "짜장면", "짬뽕", "마라탕", "초밥", "돈까스",     "라멘", "파스타", "피자", "햄버거", "떡볶이"]  if st.button("🎲 오늘의 점심 메뉴 뽑기!", type="primary", use_container_width=True):     st.balloons()     st.success(f"🎉 오늘의 추천 메뉴: **{random.choice(menus)}**")
