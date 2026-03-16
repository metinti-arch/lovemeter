import streamlit as st

st.set_page_config(page_title="İlişki Ölçeği", layout="wide")

# Your categories data
CATEGORY_DATA = {
    "FİZİKSEL": [
        ("Saç", 10), ("Gözler", 10), ("Burun", 10), ("Dişler", 10), ("Boy", 15),
        ("Fitness", 30), ("Vücut Şekli", 20), ("Koku", 30), ("Ten", 20),
    ],
    "KARAKTER": [
        ("Mizah Yeteneği", 40), ("Karakter", 30), ("Mantık", 15), ("Romantik", 10),
        ("Açık Fikirlilik", 20), ("Motivasyon", 20), ("Duygu Kontrolü", 20), ("Empati", 20),
        ("Özgüven", 15), ("Sabır", 10), ("Kıskançlık", 10), ("Güvenilirlik", 25),
    ],
    "SOSYAL": [
        ("Karizma", 20), ("Yetenek", 40), ("Zeka", 30), ("Kitap Okuma", 20),
        ("Film İzleme", 10), ("Müzik Dinleme", 20), ("Genel Kültür", 30), ("Konuşma", 10),
        ("Dinleme", 10), ("Sohbet Becerisi", 30), ("Hobiler", 10),
    ],
    "STATÜ": [
        ("Eğitim", 15), ("Yabancı Dil", 15), ("Meslek", 20), ("Gelir", 10),
    ],
    "DEĞERLER": [
        ("Aile", 10), ("Arkadaşlar", 10), ("Din", 30), ("Politika", 20),
    ],
    "KİMYA": [
        ("Ortak İlgi Alanları", 20), ("Beceri", 30), ("Arzu", 20),
        ("Tutku", 30), ("Cinsel Uyum", 80),
    ],
    "YAŞAM TARZI": [
        ("Hayvanseverlik", 20), ("Disiplin", 20), ("Düzen", 15), ("Temizlik", 15),
    ],
}

CATEGORY_COLORS = {
    "FİZİKSEL": "#e9dfbd",
    "KARAKTER": "#f3d35f",
    "SOSYAL": "#e9c09f",
    "STATÜ": "#d39ad5",
    "DEĞERLER": "#bfc8d8",
    "KİMYA": "#c6c6c8",
    "YAŞAM TARZI": "#a5c98d",
    "TOPLAM": "#f0c3cb",
}

st.title("İlişki Ölçeği")

# Initialize session state for scores
if "scores" not in st.session_state:
    st.session_state.scores = {category: {} for category in CATEGORY_DATA}

# Create columns for layout
col1, col2 = st.columns(2)

with col1:
    categories_left = ["FİZİKSEL", "DEĞERLER", "STATÜ", "YAŞAM TARZI"]
    for category in categories_left:
        st.markdown(f"### {category}")
        for item, max_score in CATEGORY_DATA[category]:
            score = st.number_input(
                f"{item} (Max: {max_score})",
                min_value=0,
                max_value=max_score,  # Bu satır önemli!
                key=f"{category}_{item}",
                label_visibility="visible"
            )
            st.session_state.scores[category][item] = score

with col2:
    categories_right = ["KARAKTER", "SOSYAL", "KİMYA"]
    for category in categories_right:
        st.markdown(f"### {category}")
        for item, max_score in CATEGORY_DATA[category]:
            score = st.number_input(
                f"{item} (Max: {max_score})",
                min_value=0,
                max_value=max_score,  # Bu satır önemli!
                key=f"{category}_{item}",
                label_visibility="visible"
            )
            st.session_state.scores[category][item] = score

# Calculate totals
st.markdown("---")
st.markdown("## Toplam Puanlar")

total_score = 0
total_max = 0

for category, items in CATEGORY_DATA.items():
    cat_score = sum(st.session_state.scores[category].get(item, 0) for item, _ in items)
    cat_max = sum(max_score for _, max_score in items)
    total_score += cat_score
    total_max += cat_max
    
    st.metric(category, f"{cat_score}/{cat_max}")

st.markdown("---")
st.metric("TOPLAM", f"{total_score}/{total_max}", delta=None)
