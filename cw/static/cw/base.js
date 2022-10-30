var search = document.getElementById("search")
search.addEventListener("keypress", function(event) {
    if (event.key === "Enter") {
        event.preventDefault()
        // сюда прикрутить поиск нада буит
        alert(search.value)
    }
})