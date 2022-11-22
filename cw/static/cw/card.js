// Додаємо гіперсилку до кожної сторінки
const cards = Array.from(document.getElementsByClassName("card"))
cards.forEach(card => {
    card.addEventListener("click", () => {
        window.location = `/page/${card.id}`
    })
})