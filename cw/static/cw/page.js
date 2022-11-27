// Створення POST запиту для зміни категорії нинішньої сторінки
const allLgi = Array.from(document.getElementsByClassName("list-group-item"))
const statusIds = {
    "none": "none",
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

var pickReady = true    // Індикатор кулдауну
function pick(item) {
    if (pickReady && !item.classList.contains("active")) {
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
            },
            success: () => {
                pickReady = false
                // Функціонал появи повідомлення про зміну папки
                var snack = document.getElementById("snackbar")
                snack.classList.add("show")
                setTimeout(() => {
                    snack.classList.remove("show")
                    pickReady = true
                }, 1300)
            }
        })
    }
}