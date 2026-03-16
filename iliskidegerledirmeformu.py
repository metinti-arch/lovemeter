import streamlit as st
import pandas as pd

st.set_page_config(page_title="İlişki Ölçeği")
st.title("İlişki Ölçeği")

# Your categories and scoring logic here

COLUMN_ITEM_WIDTH = 350
COLUMN_MAX_WIDTH = 70
COLUMN_SCORE_WIDTH = 96
CARD_MIN_WIDTH = 700

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

APP_STYLE = """
QWidget {
    background-color: #e9e9e9;
    color: #111111;
    font-size: 13px;
    font-family: Arial, Helvetica, sans-serif;
}
QWidget#mainCard {
    background-color: #ffffff;
    border: 1px solid #d6d6d6;
    border-radius: 0px;
}
QWidget#groupCard {
    border: 1px solid #c9c9c9;
    border-radius: 0px;
}
QLabel#headLabel {
    color: #ff0000;
    font-weight: 700;
    font-size: 23px;
}
QLabel#headNum {
    color: #ff0000;
    font-weight: 700;
    font-size: 18px;
}
QLabel#colLabel {
    color: #ff0000;
    font-weight: 700;
    font-size: 20px;
}
QLabel#itemLabel {
    color: #111111;
    font-weight: 500;
    font-size: 19px;
}
QLabel#maxLabel {
    color: #111111;
    font-weight: 700;
    font-size: 19px;
}
QSpinBox {
    border: 1px solid #777777;
    border-radius: 0px;
    padding: 0px 2px;
    min-width: 62px;
    font-size: 19px;
    font-weight: 700;
}
"""


class CategoryCard(QWidget):
    def __init__(self, name, items):
        super().__init__()
        self.name = name
        self.items = items
        self.max_total = sum(max_score for _, max_score in items)
        self.spins = []

        self.setObjectName("groupCard")
        self.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Maximum)
        self.setMinimumWidth(CARD_MIN_WIDTH)
        self.setStyleSheet(f"background-color: {CATEGORY_COLORS[name]};")

        root = QVBoxLayout()
        root.setContentsMargins(6, 5, 6, 5)
        root.setSpacing(3)

        head = QHBoxLayout()
        head.setSpacing(4)

        title_label = QLabel(name)
        title_label.setObjectName("headLabel")

        self.score_label = QLabel(f"({self.max_total})")
        self.score_label.setObjectName("headNum")

        col_max = QLabel("Maks")
        col_max.setObjectName("colLabel")
        col_max.setFixedWidth(COLUMN_MAX_WIDTH)
        col_max.setAlignment(Qt.AlignmentFlag.AlignCenter)

        col_score = QLabel("Skor")
        col_score.setObjectName("colLabel")
        col_score.setFixedWidth(COLUMN_SCORE_WIDTH)
        col_score.setAlignment(Qt.AlignmentFlag.AlignCenter)

        head.addWidget(title_label)
        head.addWidget(self.score_label)
        head.addStretch(1)
        head.addWidget(col_max)
        head.addWidget(col_score)
        root.addLayout(head)

        body = QGridLayout()
        body.setHorizontalSpacing(10)
        body.setVerticalSpacing(4)
        body.setContentsMargins(0, 0, 0, 0)
        body.setColumnMinimumWidth(0, COLUMN_ITEM_WIDTH)
        body.setColumnMinimumWidth(1, COLUMN_MAX_WIDTH)
        body.setColumnMinimumWidth(2, COLUMN_SCORE_WIDTH)
        body.setColumnStretch(0, 1)

        dense_groups = {"KARAKTER", "SOSYAL"}
        row_height = 40 if self.name in dense_groups else 36

        for label_text, max_score in items:
            item_label = QLabel(label_text)
            item_label.setObjectName("itemLabel")
            item_label.setMinimumWidth(COLUMN_ITEM_WIDTH)
            item_label.setMinimumHeight(row_height)
            item_label.setAlignment(Qt.AlignmentFlag.AlignVCenter | Qt.AlignmentFlag.AlignLeft)

            max_label = QLabel("" if max_score == 0 else str(max_score))
            max_label.setObjectName("maxLabel")
            max_label.setFixedWidth(COLUMN_MAX_WIDTH)
            max_label.setMinimumHeight(row_height)
            max_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

            spin = QSpinBox()
            spin.setFixedWidth(COLUMN_SCORE_WIDTH)
            spin.setMinimumHeight(row_height - 6)
            if max_score > 0:
                spin.setRange(0, 9999)
                spin.setValue(0)
                spin.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.NoButtons)
                spin.lineEdit().setAlignment(Qt.AlignmentFlag.AlignCenter)
                spin.setStyleSheet(
                    f"background-color: {CATEGORY_COLORS[name]}; color: #111111; border: 1px solid #555555;"
                )
                spin.valueChanged.connect(self.on_value_changed)
                spin.editingFinished.connect(
                    lambda s=spin, m=max_score, t=label_text: self.validate_spin_input(s, m, t)
                )
            else:
                spin.setRange(0, 0)
                spin.setEnabled(False)
                spin.setStyleSheet("background-color: #e5e7eb; color: #6b7280;")

            row_index = len(self.spins)
            body.setRowMinimumHeight(row_index, row_height)
            body.addWidget(item_label, row_index, 0)
            body.addWidget(max_label, row_index, 1)
            body.addWidget(spin, row_index, 2)
            self.spins.append((spin, max_score, label_text))

        root.addLayout(body)
        self.setLayout(root)

    def current_score(self):
        return sum(min(spin.value(), max_score) for spin, max_score, _ in self.spins if max_score > 0)

    def on_value_changed(self):
        parent = self.parent()
        while parent is not None and not hasattr(parent, "recalculate"):
            parent = parent.parent()
        if parent is not None:
            parent.recalculate()

    def validate_spin_input(self, spin, max_score, label_text):
        if spin.value() > max_score:
            QMessageBox.warning(
                self,
                "Hatalı Puan",
                f"'{label_text}' için en yüksek puan {max_score}.",
            )
            was_blocked = spin.blockSignals(True)
            spin.setValue(max_score)
            spin.blockSignals(was_blocked)
            spin.setFocus()
            spin.selectAll()
            parent = self.parent()
            while parent is not None and not hasattr(parent, "recalculate"):
                parent = parent.parent()
            if parent is not None:
                parent.recalculate()
            return False
        return True


class SumCard(QWidget):
    def __init__(self, total_max):
        super().__init__()

        self.setObjectName("groupCard")
        self.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Maximum)
        self.setMinimumWidth(CARD_MIN_WIDTH)
        self.setStyleSheet(f"background-color: {CATEGORY_COLORS['TOPLAM']};")

        root = QVBoxLayout()
        root.setContentsMargins(6, 5, 6, 5)
        root.setSpacing(4)

        row = QHBoxLayout()
        row.setSpacing(6)

        title = QLabel("TOPLAM")
        title.setObjectName("headLabel")

        max_label = QLabel(str(total_max))
        max_label.setObjectName("maxLabel")
        max_label.setFixedWidth(COLUMN_MAX_WIDTH + 26)
        max_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.score_label = QLabel("0")
        self.score_label.setObjectName("maxLabel")
        self.score_label.setFixedWidth(COLUMN_SCORE_WIDTH + 20)
        self.score_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        row.addWidget(title)
        row.addStretch(1)
        row.addWidget(max_label)
        row.addWidget(self.score_label)
        root.addLayout(row)

        self.setLayout(root)

    def set_score(self, score):
        self.score_label.setText(str(score))


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("İlişki Ölçeği")
        self.resize(1380, 920)

        self.cards = {}

        outer = QVBoxLayout()
        outer.setContentsMargins(16, 12, 16, 12)
        outer.setSpacing(10)

        scroll = QScrollArea()
        scroll.setWidgetResizable(True)
        outer.addWidget(scroll)

        wrapper = QWidget()
        wrapper.setObjectName("mainCard")
        wlayout = QVBoxLayout()
        wlayout.setContentsMargins(6, 6, 6, 6)
        wlayout.setSpacing(8)

        columns_row = QHBoxLayout()
        columns_row.setSpacing(12)

        total_max = 0
        for category, items in CATEGORY_DATA.items():
            total_max += sum(max_score for _, max_score in items)

        left_widget = QWidget()
        right_widget = QWidget()
        left_widget.setMinimumWidth(CARD_MIN_WIDTH)
        right_widget.setMinimumWidth(CARD_MIN_WIDTH)

        left_col = QVBoxLayout()
        right_col = QVBoxLayout()
        left_col.setContentsMargins(0, 0, 0, 0)
        right_col.setContentsMargins(0, 0, 0, 0)
        left_col.setSpacing(10)
        right_col.setSpacing(10)

        left_order = ["FİZİKSEL", "DEĞERLER", "STATÜ", "YAŞAM TARZI", "TOPLAM"]
        right_order = ["KARAKTER", "SOSYAL", "KİMYA"]

        def add_card(container_layout, key):
            if key == "TOPLAM":
                self.sum_card = SumCard(total_max)
                container_layout.addWidget(self.sum_card, alignment=Qt.AlignmentFlag.AlignTop)
            else:
                card = CategoryCard(key, CATEGORY_DATA[key])
                self.cards[key] = card
                container_layout.addWidget(card, alignment=Qt.AlignmentFlag.AlignTop)

        for key in left_order:
            if key == "TOPLAM":
                left_col.addSpacing(280)
            add_card(left_col, key)
        left_col.addStretch(1)

        for key in right_order:
            add_card(right_col, key)
        right_col.addStretch(1)

        left_widget.setLayout(left_col)
        right_widget.setLayout(right_col)
        columns_row.addWidget(left_widget, 1)
        columns_row.addWidget(right_widget, 1)

        wlayout.addLayout(columns_row)

        wrapper.setLayout(wlayout)
        scroll.setWidget(wrapper)
        self.setLayout(outer)

    def recalculate(self):
        total = 0
        for card in self.cards.values():
            total += card.current_score()
        self.sum_card.set_score(total)


def main():
    app = QApplication(sys.argv)
    app.setStyleSheet(APP_STYLE)
    window = MainWindow()
    window.showMaximized()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
