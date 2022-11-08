HOST = "http://127.0.0.1:8000/"

var search = document.getElementById("search")
search.addEventListener("keypress", function(event) {
    if (event.key === "Enter") {
        event.preventDefault()  // Блокуємо звичайну поведінку натиснутої клавіші
        // Формуємо GET запит та відправляємо на вьюху, що прив'язана до "HOST/" сторінки
        $.ajax({
            url: HOST,
            type: "GET",
            data: {
                "action": "search",
                "value": search.value
            },
            success: (data)=>{
                window.location.href = HOST
                document.write(data)
            }
        })
    }
})