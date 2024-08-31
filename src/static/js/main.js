fetch("http://127.0.0.1:5000/get-dados-usuario", {
    method: 'GET',
})
.then(response => response.json()) 
.then(resposta =>{
    console.log(resposta)
})
