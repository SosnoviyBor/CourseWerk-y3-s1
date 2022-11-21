// Створення POST запиту для зміни категорії нинішньої сторінки
const allLgi = Array.from(document.getElementsByClassName("list-group-item"))
const statusIds = {
    "none": "None",
    "active": "0",
    "planned": "1",
    "done": "2"
}

// Вибір активної папки на сторінці
allLgi.forEach((lgi) => {
    const currActive = document.getElementsByClassName("list-group")[0].dataset.active
    if (currActive === statusIds[lgi.id]) {
        lgi.classList.add("active")
        return
    }
})

function pick(item) {
    // Оновлення зовнішнього виду кнопок
    allLgi.forEach((lgi) => {
        if (lgi === item) {
            lgi.classList.add("active")
        } else {
            lgi.classList.remove("active")
        }
    })

    // Створення POST запиту для зміни категорії нинішньої сторінки
    $.ajax({
        url: window.location.href,
        type: "POST",
        data: {
            "action": "setfolder",
            "value": statusIds[item.id],
        }
    })
}