import streamlit as sk
sk.title("🛒 แอปพลิเคชั่นคำนวณราคาสินค้ารวม VAT 7% 💫 ")
price = sk.number_input("กรอกราคาสินค้า (บาท):", value=0.0)
vat = price * 0.07
net_price = price - vat
sk.header(f"• ภาษีมูลค่าเพิ่ม (VAT 7%): **{vat:.2f}** บาท")
sk.header(f"• ราคาสุทธิ: {net_price:.2f} บาท")
sk.divider()
st.write("นางสาวจอมขวัญ อาภัย เลขที่ 4  ม.4/15")
