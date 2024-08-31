document.getElementById("formPublicar").addEventListener("submit", (event)=>{
    event.preventDefault();

    const alertBox = document.getElementById("alertBox");
    const form = document.getElementById("formPublicar");
    const formData = new FormData(form);
    
    fetch("http://127.0.0.1:5000/publicar-post", {
        method: 'POST',
        body: formData
    })
    .then(response => response.json())  // Converte a resposta para JSON
    .then(resposta => {
        alertBox.innerHTML = ""
        const alertDiv = document.createElement("div");
        alertDiv.role = "alert";
        if (resposta.error) {
            
            alertDiv.className = "alert alert-danger mt-2 text-center";
            alertDiv.textContent = resposta.error;
        }else{
            alertDiv.className = "alert alert-success mt-2 text-center";
            alertDiv.textContent = resposta.message;
        }

        alertBox.appendChild(alertDiv);
    })
    .catch(error => {
        alertBox.innerHTML = ""
        const alertDiv = document.createElement("div");
        alertDiv.role = "alert";
        alertDiv.className = "alert alert-warning mt-2 text-center";
        alertDiv.textContent = 'Ocorreu um erro ao fazer a publicação'
        alertBox.appendChild(alertDiv);
    });

});
   

   

