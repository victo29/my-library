
// Realiza uma requisição Post para registrar o usuário
export async function registerUser(userData) {
    try{
        const response = await fetch("http://127.0.0.1:5000/cadastrar",{
            method:'POST',
            headers:{
                'Content-Type':'application/json',
            },
            body: JSON.stringify(userData)

        });
        return await response.json();
    } catch(error){
        return { error: "Ocorreu um erro ao tentar cadastrar o usuário." };
    }
    

}

// Realiza uma requisição Post para logar o usuário
export async function loginUser(userData){
    try{

        const response = await fetch("http://127.0.0.1:5000/logar", {
            method:"POST",
            headers:{
                'Content-Type':'application/json',
            },
            body: JSON.stringify(userData)
        })

        return await response.json();
    }catch(error){
        return {error: "Ocorreu um erro ao tentar logar o usuário."}
    }
    
}

export async function authGuard(){
    
}