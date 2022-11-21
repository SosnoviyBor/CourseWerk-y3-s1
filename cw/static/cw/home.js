// Створення повідомлення, якщо нічого не було знайдено
if (document.getElementsByClassName("card").length === 0) {
    const content = document.getElementsByClassName("card-list")[0]
    const p = document.createElement("p")
    p.id = "not-found"
    p.innerHTML = "Нажаль, нічого не було знайдено за вашим запитом"
    content.appendChild(p)
}