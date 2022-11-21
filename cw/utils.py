from .models import *

# Для отримання назв статусів тем для користувача
STATUS_TEXT = {
    None: None,
    0: "Активна",
    1: "Запланована",
    2: "Пройдена"
}

def cards_ctx(req, pages):
    """Функція для генерації контексту, що використовується в card_template.html

    Args:
        req : запит до сервера
        pages : результат "Page.objects.all()". Набір об'єктів можна фільтрувати

    Returns:
        Масив, що треба передавати до контексту сторінки під назвою "cards"
    """
    ctx = []
    folders = Folder.objects

    for page in pages:
        try:    # Папка має статус у цього користувача
            status_id = folders.filter(user=req.user).get(page=page).status
        except: # Або ні
            status_id = None
        ctx.append((page, status_id, STATUS_TEXT[status_id]))
    return ctx