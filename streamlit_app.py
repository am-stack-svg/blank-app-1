import streamlit as st
from supabase import create_client

# Supabase接続情報（自分のものに置き換える）
SUPABASE_URL = "https://xxxxx.supabase.co"
SUPABASE_KEY = "public-anon-key"

supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

st.title("🛒 買い物リストアプリ")

# 入力フォーム
item_name = st.text_input("買う物")
category = st.selectbox(
    "カテゴリー",
    ["食料品", "日用品", "文房具", "その他"]
)

if st.button("追加"):
    if item_name == "":
        st.warning("買う物を入力してください")
    else:
        supabase.table("shopping_items").insert({
            "item_name": item_name,
            "category": category
        }).execute()
        st.success("追加しました！")

# --- 表示 ---
st.subheader("📋 買い物リスト")

items = supabase.table("shopping_items").select("*").execute()

for item in items.data:
    st.write(f"【{item['category']}】 {item['item_name']}")
