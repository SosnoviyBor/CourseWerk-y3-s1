// Створення POST запиту для зміни категорії нинішньої сторінки
const pickFolder = document.getElementById("pick-folder")
pickFolder.addEventListener("change", (event)=>{
    $.ajax({
        url: window.location.href,
        type: "POST",
        data: {
            "action": "setfolder",
            "value": event.target.value,
        }
    })
})

// Виставлення активної категорії
for (var i = 0; i < pickFolder.children.length; i++) {
    if (pickFolder.children[i].value === s) {
        pickFolder.children[i].selected = true
        break
    }
}