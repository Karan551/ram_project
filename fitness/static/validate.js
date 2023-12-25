const userPassword = document.querySelector("#user-password")
const checkBox = document.querySelector("#check")
checkBox.addEventListener("click", () => {
    if (checkBox.checked) {
        userPassword.type = "text"
    } else {
        userPassword.type = "password"
    }
})

