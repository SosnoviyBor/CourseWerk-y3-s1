// Додаємо гіперсилку до кожної сторінки
const cards = Array.from(document.getElementsByClassName("card"))
cards.forEach(card => {
    card.addEventListener("click", () => {
        console.log("aaa")
        window.location = `/page/${card.id}`
    })
})