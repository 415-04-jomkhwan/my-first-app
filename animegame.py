import time
import streamlit as st

st.title("⏱️ เกมเติมศัพท์จับเวลา — ของใช้ในบ้าน")

TIME_LIMIT = 60 # วินาที 


QUESTIONS = [
{"key": "ans1", "hint": "O_ep_ece", "emoji": "🗄️", "answer": "Onepiece"},
{"key": "ans2", "hint": "N_r_t_", "emoji": "🪑", "answer": "Naruto"},
{"key": "ans3", "hint": "D_m_n Sl_yer", "emoji": "🛏️", "answer": "Demon Slayer"},
{"key": "ans4", "hint": "_tt_ck On Ti_an", "emoji": "🛋️", "answer": "Attack On Titan"},
{"key": "ans5", "hint": "H_ik_uu", "emoji": "🧊", "answer": "Haikyuu"},
]

for q in QUESTIONS:
    val_key = f"{q['key']}_val"
if val_key not in st.session_state:
    st.session_state[val_key] = ""


def reset_game():
    for q in QUESTIONS:
        st.session_state[f"{q['key']}_val"] = "" # เคลียร์ค่าทุกช่อง
        st.session_state.start = time.time() # เริ่มเวลาใหม่
        st.session_state.is_ended = False # ปิด Dialog



@st.dialog("📊 สรุปผลการเล่นเกม")
def show_result_dialog(answers):
    st.balloons()
    score = 0

    for i, q in enumerate(QUESTIONS, start=1):
        u_ans = answers[q["key"]].strip().lower()
if u_ans == q["answer"]:
    st.success(f"✅ ข้อ {i} ({q['emoji']}): ถูกต้อง — {q['answer']}")
    score += 1
else:
    st.error(f"❌ ข้อ {i} ({q['emoji']}): ยังไม่ถูกต้อง (คุณตอบ '{u_ans}' / เฉลย '{q['answer']}')")

    st.info(f"🏆 ได้คะแนนรวม: {score} จาก {len(QUESTIONS)} คะแนน")

if score == len(QUESTIONS):
    st.success("🎉 You win! เต็มทุกข้อ!")
elif score >= len(QUESTIONS) * 0.6:
    st.success("👍 เก่งมาก!")
else:
    st.error("💀 You lose! ลองใหม่อีกครั้งนะ")



st.button("🎮 เริ่มเล่นเกม", on_click=reset_game)


if "start" in st.session_state and not st.session_state.get("is_ended", False):
    time_left = int(TIME_LIMIT - (time.time() - st.session_state.start))

if time_left > 0:
    st.error(f"⏳ เหลือเวลา: {time_left} วินาที")
else:
    st.session_state.is_ended = True
    st.rerun()

    st.divider()


current_answers = {}
for i, q in enumerate(QUESTIONS, start=1):
    val_key = f"{q['key']}_val"
    ans = st.text_input(
f"ข้อ {i}: `{q['hint']}` {q['emoji']}",
value=st.session_state[val_key],
key=f"input_{q['key']}",
)
st.session_state[val_key] = ans
current_answers[q["key"]] = ans


if "start" in st.session_state and not st.session_state.get("is_ended", False):
if st.button("📥 ส่งคำตอบ"):
st.session_state.is_ended = True
st.rerun()

time.sleep(1)
st.rerun()


if st.session_state.get("is_ended", False):
show_result_dialog(current_answers)

st.divider()
