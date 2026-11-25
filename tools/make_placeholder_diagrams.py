"""Генерация шаблонных PNG-заглушек для диаграмм проекта.

Каждый файл — аккуратная заглушка с названием диаграммы, идентификатором
артефакта и источником. Заглушку нужно заменить реальной диаграммой,
созданной в инструменте моделирования.
"""
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

W, H = 1600, 1000
WHITE = (255, 255, 255)
INK = (40, 48, 64)
MUTED = (130, 138, 152)
BORDER = (28, 48, 82)
FRAME = (208, 216, 228)
ACCENT_BG = (240, 244, 250)

FONT_DIR = "/usr/share/fonts/truetype/dejavu"
f_title = ImageFont.truetype(f"{FONT_DIR}/DejaVuSans-Bold.ttf", 64)
f_sub = ImageFont.truetype(f"{FONT_DIR}/DejaVuSans.ttf", 40)
f_small = ImageFont.truetype(f"{FONT_DIR}/DejaVuSans.ttf", 30)

PROJECT = "Проект: Автомат печати фото из ВКонтакте"

SPECS = [
    ("diagrams/process/process-model.png",
     "Модель бизнес-процесса", "ART-003", "ЛР №2"),
    ("diagrams/functional/as-is.png",
     "Функциональная модель AS-IS", "ART-004", "ЛР №3"),
    ("diagrams/functional/to-be.png",
     "Функциональная модель TO-BE", "ART-005", "ЛР №3"),
    ("diagrams/data/data-flow.png",
     "Модель потоков данных", "ART-006", "ЛР №4"),
    ("diagrams/data/erd.png",
     "Модель данных (ER-диаграмма)", "ART-007", "ЛР №4"),
    ("diagrams/architecture/c4-context.png",
     "Архитектурная модель (C4, контекст)", "ART-008", "ЛР №6"),
    ("diagrams/api/api-diagram.png",
     "Схема API", "ART-009", "ЛР №8"),
]


def centered(draw, y, text, font, fill):
    w = draw.textlength(text, font=font)
    draw.text(((W - w) / 2, y), text, font=font, fill=fill)


for rel, title, art, source in SPECS:
    img = Image.new("RGB", (W, H), WHITE)
    d = ImageDraw.Draw(img)

    d.rectangle([8, 8, W - 8, H - 8], outline=BORDER, width=6)
    d.rectangle([40, 40, W - 40, H - 40], outline=FRAME, width=3)
    d.rectangle([40, 40, W - 40, 330], fill=ACCENT_BG)

    centered(d, 120, title, f_title, INK)
    centered(d, 220, "Шаблон-заглушка диаграммы", f_sub, MUTED)

    centered(d, 470, "Замените этот файл диаграммой, созданной", f_sub, MUTED)
    centered(d, 530, "в инструменте моделирования", f_sub, MUTED)

    footer = f"{PROJECT}  ·  Артефакт: {art}  ·  Источник: {source}"
    centered(d, 850, footer, f_small, MUTED)

    out = Path(rel)
    out.parent.mkdir(parents=True, exist_ok=True)
    img.save(out, "PNG")
    print("OK", rel)
