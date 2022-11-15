// const host = "http://127.0.0.1:8000/"

const search = document.getElementById("search")
const allItems = Array.from(document.getElementsByClassName("item"))
// Функціонал пошуку
search.addEventListener("keypress", function(event) {
    if (event.key === "Enter") {
        // Блокуємо звичайну поведінку натиснутої клавіші
        event.preventDefault()

        const inp = search.value.toLowerCase()
        const result = []
        search.value = ""

        // Якщо результат відсутній, нічого не робимо
        if (inp === "") { return }

        // Видалення усіх сторінок, що були присутні
        try {
            // Та повідомлення, якщо воно існувало
            document.getElementById("not-found").remove()
        } catch {
            Array.from(document.getElementsByClassName("item"))
                .forEach(book => {book.remove()})
        }

        // Фільтрування збережених у пам'ять сторінок
        for (let i = 0; i < allItems.length; i++){
            const name = allItems[i].getElementsByClassName("item-name")[0].innerHTML
            const desc = allItems[i].getElementsByClassName("item-desc")[0].innerHTML
            if (name.toLowerCase().includes(inp) ||
                desc.toLowerCase().includes(inp)) {
                    result.push(allItems[i])
            }
        }

        // Відображення результату пошуку
        if (result.length === 0) {
            // Нічого не було знайдено
            const content = document.getElementById("item-list")
            const p = document.createElement("p")
            p.id = "not-found"
            p.innerHTML = "Нажаль, нічого не було знайдено за вашим запитом"
            content.appendChild(p)
        } else {
            // Щось було знайдено
            for (let i = 0; i < result.length; i++){
                document.getElementById("item-list").appendChild(result[i])
            }
        }
    }
})