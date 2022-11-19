// Константи із елементами
const allCards = Array.from(document.getElementsByClassName("card"))
const search = document.getElementById("search")

// Додаємо гіперсилку до кожної сторінки
allCards.forEach((card) => {
    card.addEventListener("click", () => {
        window.location = `/page/${card.id}`
    })
})

// Створення повідомлення, якщо нічого не було знайдено
if (document.getElementsByClassName("card").length === 0) {
    const content = document.getElementById("card-list")
    const p = document.createElement("p")
    p.id = "not-found"
    p.innerHTML = "Нажаль, нічого не було знайдено за вашим запитом"
    content.appendChild(p)
}