import streamlit as st

st.set_page_config(page_title="İlişki Ölçeği", layout="wide")

# Custom CSS for better styling
st.markdown("""
    <style>
    .category-box {
        border: 3px solid;
        border-radius: 10px;
        padding: 20px;
        margin: 15px 0;
        background-color: rgba(255,255,255,0.8);
    }
    
    .fiziksel { border-color: #e9dfbd; background: linear-gradient(135deg, #e9dfbd 0%, rgba(233,223,189,0.1) 100%); }
    .karakter { border-color: #f3d35f; background: linear-gradient(135deg, #f3d35f 0%, rgba(243,211,95,0.1) 100%); }
    .sosyal { border-color: #e9c09f; background: linear-gradient(135deg, #e9c09f 0%, rgba(233,192,159,0.1) 100%); }
    .statu { border-color: #d39ad5; background: linear-gradient(135deg, #d39ad5 0%, rgba(211,154,213,0.1) 100%); }
    .degerler { border-color: #bfc8d8; background: linear-gradient(135deg, #bfc8d8 0%, rgba(191,200,216,0.1) 100%); }
    .kimya { border-color: #c6c6c8; background: linear-gradient(135deg, #c6c6c8 0%, rgba(198,198,200,0.1) 100%); }
    .yasam { border-color: #a5c98d; background: linear-gradient(135deg, #a5c98d 0%, rgba(165,201,141,0.1) 100%); }
    
    .category-title {
        font-size: 24px;
        font-weight: bold;
        margin-bottom: 15px;
        padding-bottom: 10px;
        border-bottom: 2px solid;
    }
    
    .fiziksel .category-title { color: #8B7355; border-color: #e9dfbd; }
    .karakter .category-title { color: #D4A017; border-color: #f3d35f; }
    .sosyal .category-title { color: #CD7F32; border-color: #e9c09f; }
    .statu .category-title { color: #9B59B6; border-color: #d39ad5; }
    .degerler .category-title { color: #5B7C99; border-color: #bfc8d8; }
    .kimya .category-title { color: #666666; border-color: #c6c6c8; }
    .yasam .category-title { color: #7CB342; border-color: #a5c98d; }
    
    .main-title {
        text-align: center;
        font-size: 64px;
        font-weight: bold;
        color: #FF1744;
        margin-bottom: 30px;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.1);
    }
    
    .total-container {
        background: linear-gradient(135deg, #f0c3cb 0%, rgba(240,195,203,0.1) 100%);
        border: 3px solid #f0c3cb;
        border-radius: 10px;
        padding: 25px;
        margin: 30px 0;
        text-align: center;
    }
    
    .score-item {
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding: 8px 0;
        font-size: 16px;
    }
    
    .input-fiziksel input { background-color: rgba(233, 223, 189, 0.3) !important; border-color: #e9dfbd !important; }
    .input-karakter input { background-color: rgba(243, 211, 95, 0.3) !important; border-color: #f3d35f !important; }
    .input-sosyal input { background-color: rgba(233, 192, 159, 0.3) !important; border-color: #e9c09f !important; }
    .input-statu input { background-color: rgba(211, 154, 213, 0.3) !important; border-color: #d39ad5 !important; }
    .input-degerler input { background-color: rgba(191, 200, 216, 0.3) !important; border-color: #bfc8d8 !important; }
    .input-kimya input { background-color: rgba(198, 198, 200, 0.3) !important; border-color: #c6c6c8 !important; }
    .input-yasam input { background-color: rgba(165, 201, 141, 0.3) !important; border-color: #a5c98d !important; }
    
    .input-item-label {
        font-size: 12px;
        font-weight: 600;
        margin-bottom: 5px;
    }
    </style>
""", unsafe_allow_html=True)

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
        ("Tutku", 30), ("Tensel Uyum", 80),
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

CATEGORY_CLASS = {
    "FİZİKSEL": "fiziksel",
    "KARAKTER": "karakter",
    "SOSYAL": "sosyal",
    "STATÜ": "statu",
    "DEĞERLER": "degerler",
    "KİMYA": "kimya",
    "YAŞAM TARZI": "yasam",
}

st.markdown("<div class='main-title'>💕 İlişki Ölçeği 💕</div>", unsafe_allow_html=True)

# Initialize session state for scores
if "scores" not in st.session_state:
    st.session_state.scores = {category: {} for category in CATEGORY_DATA}

# Create columns for categories
columns = st.columns(7, gap="small")

def render_category(category, col):
    """Render a category with styling"""
    class_name = CATEGORY_CLASS.get(category, "")
    with col:
        st.markdown(f"""
            <div class='category-box {class_name}'>
                <div class='category-title'>{category}</div>
            </div>
        """, unsafe_allow_html=True)
        
        for item, max_score in CATEGORY_DATA[category]:
            score = st.number_input(
                f"{item} (Max: {max_score})",
                min_value=0,
                max_value=max_score,
                key=f"{category}_{item}",
                label_visibility="visible"
            )
            st.session_state.scores[category][item] = score

# Render each category in its own column
all_categories = list(CATEGORY_DATA.keys())
for idx, category in enumerate(all_categories):
    render_category(category, columns[idx])

# Calculate totals
st.markdown("---")

total_score = 0
total_max = 0
category_results = []

# Calculate all categories
for category in all_categories:
    items = CATEGORY_DATA[category]
    cat_score = sum(st.session_state.scores[category].get(item, 0) for item, _ in items)
    cat_max = sum(max_score for _, max_score in items)
    total_score += cat_score
    total_max += cat_max
    category_results.append((category, cat_score, cat_max))

# Display category scores
cols = st.columns(7, gap="small")
for idx, (category, cat_score, cat_max) in enumerate(category_results):
    color = CATEGORY_COLORS[category]
    with cols[idx]:
        st.markdown(f"""
            <div style='background-color: {color}; padding: 10px; border-radius: 5px; text-align: center;'>
                <strong style='font-size: 12px;'>{category}</strong><br>
                <span style='font-size: 16px; font-weight: bold;'>{cat_score}/{cat_max}</span>
            </div>
        """, unsafe_allow_html=True)

# Total score with special styling
st.markdown(f"""
    <div class='total-container'>
        <h2 style='color: #FF1744; margin: 0;'>🏆 TOPLAM PUAN 🏆</h2>
        <h1 style='color: #FF1744; margin: 10px 0; font-size: 48px;'>{total_score}/{total_max}</h1>
        <p style='color: #666; margin: 0;'>Uyum Yüzdesi: <strong style='color: #FF1744; font-size: 24px;'>{round((total_score/total_max*100) if total_max > 0 else 0, 1)}%</strong></p>
    </div>
""", unsafe_allow_html=True)

# Reset button at the bottom
st.markdown("---")
if st.button("🔄 Formu Sıfırla", type="secondary", use_container_width=True):
    for category, items in CATEGORY_DATA.items():
        st.session_state.scores[category] = {}
        for item, _ in items:
            st.session_state[f"{category}_{item}"] = 0
    st.rerun()
