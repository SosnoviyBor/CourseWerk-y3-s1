// Збереження списків для переключення між ними
const itemLists = document.getElementsByClassName("item-list")
var items = {
    "active": itemLists[0],
    "planned": itemLists[1],
    "done": itemLists[2],
}
// Видалення усіх списків окрім "активних", бо вони є дефолтним станом сторінки
for (var i = 0; i < itemLists.length; i++){
    if (itemLists[i].id !== "active"){
        itemLists[i].remove()
        i--
    }
}

// Переключення між списками
const display = document.getElementById("display-items")
display.addEventListener("change", (event)=>{
    const itemList = document.getElementsByClassName("item-list")[0]
    itemList.remove()
    document.getElementById("item-lists").appendChild(items[event.target.value])
})