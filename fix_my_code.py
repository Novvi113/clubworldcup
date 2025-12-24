import re

# Настройки: что и на что менять
replacements = [
    # 1. Ребрендинг
    ("WT Analysis", "Novvi113 Scout"),
    ("WTAnalysis", "Novvi113"),
    
    # 2. Исправление путей к Excel файлам (убираем C:/Users/...)
    # Мы ищем любой мусор перед именем файла и удаляем его
    (r'pd\.read_excel\(.*[\/\\]league_dict\.xlsx[\'"]\)', 'pd.read_excel("league_dict.xlsx")'),
    (r'pd\.read_excel\(.*[\/\\]formation_dict\.xlsx[\'"]\)', 'pd.read_excel("formation_dict.xlsx")'),
    (r'pd\.read_excel\(.*[\/\\]Opta Events\.xlsx[\'"]\)', 'pd.read_excel("Opta Events.xlsx")'),
    (r'pd\.read_excel\(.*[\/\\]Opta Qualifiers\.xlsx[\'"]\)', 'pd.read_excel("Opta Qualifiers.xlsx")'),
    
    # 3. Исправление картинок
    (r'Image\.open\(.*[\/\\]wtatransnew\.png[\'"]\)', 'Image.open("wtatransnew.png")'),
    (r'Image\.open\(.*[\/\\]football\.png[\'"]\)', 'Image.open("football.png")'),
]

# Имя твоего файла
filename = "streamlitcwc.py"

print(f"🔧 Начинаю ремонт файла {filename}...")

# Читаем файл
with open(filename, "r", encoding="utf-8") as f:
    content = f.read()

# Применяем замены
for old, new in replacements:
    # Если это регулярное выражение (начинается с r'...')
    if old.startswith('pd.') or old.startswith('Image.'):
        content = re.sub(old, new, content)
    else:
        # Обычная замена текста
        content = content.replace(old, new)

# Сохраняем обратно
with open(filename, "w", encoding="utf-8") as f:
    f.write(content)

print("✅ Готово! Файл отредактирован. Можно запускать.")