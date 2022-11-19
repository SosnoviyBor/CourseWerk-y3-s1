// Збереження кнопок для переходу між папками на майбутнє
const allLgi = Array.from(document.getElementsByClassName("list-group-item"))
// Збереження списків для переключення між ними
const allCardLists = document.getElementsByClassName("card-list")
var cardLists = {
    "active": allCardLists[0],
    "planned": allCardLists[1],
    "done": allCardLists[2],
}

// Вирахування кількості тем у кожній папці
Array.from(allLgi).forEach((lgi) => {
    const type = lgi.id
    const amount = cardLists[type].getElementsByClassName("card").length
    lgi.getElementsByClassName("badge")[0].innerHTML = amount
})

Array.from(allCardLists).forEach((cl) => {
    // Додаємо гіперсилку до кожної сторінки
    Array.from(cl.getElementsByClassName("card")).forEach((card) => {
        console.log(card)
        card.addEventListener("click", () => {
            window.location = `/page/${card.id}`
        })
    })

    // Видалення усіх списків окрім "активних", бо вони є дефолтним станом сторінки
    if (cl.id !== "active"){
        cl.remove()
    }
})

// Функція для переключення між папками
function pick(item) {
    // Якщо ми клацнули на вже активну кнопку
    if (item.classList.contains("active")) { return }

    // Заміна card-list
    const cardList = document.getElementsByClassName("card-list")[0]
    cardList.remove()
    document.getElementById("wrapper").appendChild(cardLists[item.id])

    // Оновлення зовнішнього виду кнопок
    allLgi.forEach((lgi) => {
        const badge = lgi.getElementsByClassName("badge")[0]
        if (lgi === item) {
            lgi.classList.add("active")
            badge.classList.replace("badge-primary", "badge-light")
        } else {
            lgi.classList.remove("active")
            badge.classList.replace("badge-light", "badge-primary")
        }
    })
}