filename = "streamlitcwc.py"

print("🚑 Чиним подключение к базе данных...")

try:
    with open(filename, "r", encoding="utf-8") as f:
        content = f.read()

    # Мы ищем сломанную ссылку (она стала пустой: https:///)
    # И меняем её обратно на рабочую (https://www.scoresway.com/)
    
    # Вариант 1 (если остались слеши)
    new_content = content.replace("'Referer': 'https:///'", "'Referer': 'https://www.scoresway.com/'")
    
    # Вариант 2 (если слеши тоже удалились)
    new_content = new_content.replace("'Referer': 'https://'", "'Referer': 'https://www.scoresway.com/'")

    if content != new_content:
        with open(filename, "w", encoding="utf-8") as f:
            f.write(new_content)
        print("✅ Успех! Ссылка восстановлена. Матчи должны появиться.")
    else:
        print("⚠️ Не нашел сломанную ссылку. Возможно, она выглядит иначе.")
        # На всякий случай выведем кусок кода, чтобы проверить
        start = content.find("'Referer':")
        if start != -1:
            print(f"Сейчас в коде написано: {content[start:start+40]}")

except Exception as e:
    print(f"❌ Ошибка: {e}")