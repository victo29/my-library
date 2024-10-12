document.getElementById("form").addEventListener("submit", (event)=>{
    event.preventDefault();

    const alertBox = document.getElementById("alertBox");
    const form = document.getElementById("form");
    const formData = new FormData(form);
    const inputEmail = document.getElementById("InputEmail")
    const InputPassword = document.getElementById("InputPassword")

    fetch("http://127.0.0.1:5000/logar", {
        method: 'POST',
        body: formData
    })
    .then(response => response.json())  
    .then(resposta => {
        alertBox.innerHTML = ""
        const alertDiv = document.createElement("div");
        alertDiv.role = "alert";
        if (resposta.error) {
            
            alertDiv.className = "error";
            alertDiv.textContent = resposta.error;
        }else{
            window.location.replace(resposta.redirect);
        }

        alertBox.appendChild(alertDiv);
    })
    .catch(error => {
        alertBox.innerHTML = ""
        const alertDiv = document.createElement("div");
        alertDiv.role = "alert";
        alertDiv.className = "warning";
        alertDiv.textContent = 'Ocorreu um erro ao tentar logar o usuário.'
        alertBox.appendChild(alertDiv);
    });

});
   

   

