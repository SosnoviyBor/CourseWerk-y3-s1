HOST = "http://127.0.0.1:8000/"

document.getElementById("logo").href = HOST
document.getElementById("goto-login").href = `${HOST}login`
document.getElementById("goto-reg").href = `${HOST}register`

var search = document.getElementById("search")
search.addEventListener("keypress", function(event) {
    if (event.key === "Enter") {
        event.preventDefault()
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