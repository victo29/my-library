import { useState } from "react";
import Swal from "sweetalert2";
import { useNavigate } from 'react-router-dom';
import { registerUser, loginUser } from "../services/authService";
import styles from "../modules/Login.module.css"


export default function Login(){

    const navigate = useNavigate();

    const [loginShowInputs, setLoginShowInputs] = useState(true);
    function ShowInputsRegister() {
    setLoginShowInputs(false);
    }
    function ShowInputsLogin() {
    setLoginShowInputs(true);
    }  


    const [nameForRegister, setNameForRegister] = useState("");
    const [passwordForRegister, setPasswordForRegister] = useState("");
    const [emailForRegister, setEmailForRegister] = useState("");

    // Responsável por pegar os dados dos inputs, chamar a função para cadastro e exibir resposta
    async function handleRegisterUser(event){
        event.preventDefault();

        if(nameForRegister !== "" && passwordForRegister !== "" && emailForRegister !== ""){
            const userData = {
                name: nameForRegister,
                email: emailForRegister,
                password: passwordForRegister
            };

            const response = await registerUser(userData);

            if(response.error){
                Swal.fire({
                    icon: "error",
                    title: "Error",
                    text: response.error
                  });
            }else{
                Swal.fire({
                    icon: "success",
                    title: "Sucesso!",
                    text: response.message
                  });
            }
        }else{
            Swal.fire({
                icon: "error",
                title: "Error",
                text: "Todos os campos são obrigatórios"
              });
        }
            
    }


    const [passwordForLogin, setPasswordForLogin] = useState("");
    const [emailForLogin, setEmailForLogin] = useState("");

    // Responsável por pegar os dados dos inputs, chamar a função para login e exibir resposta
    async function handleLoginUser(event){
        event.preventDefault()


        if (passwordForLogin !== "" && emailForLogin !== ""){
            
            const userData = {
                email: emailForLogin,
                password: passwordForLogin
            }

            const response = await loginUser(userData)
            
            if(response.error){
                Swal.fire({
                    icon: "error",
                    title: "Error",
                    text: response.error
                  });
            }else{
                localStorage.setItem("nameUser", response.userData);
                navigate("/Home");
            }
        }
        else{
            Swal.fire({
                icon: "error",
                title: "Error",
                text: "Todos os campos são obrigatórios"
              });
        }
    }


    return(
        <main className={styles.main}>

            <section className={styles.leftSection}>
                <div className={styles.header}>
                    <div className={styles.boxImage}>
                        <img src="logo.svg" alt=""/>
                    </div>
                </div>
                {loginShowInputs ? (
                    <div className={styles.content}>
                        <h1>Bem-vindo de volta</h1>
                        <div className={styles.divForm}>
                            <form className={styles.formLoginRegister} method="POST">
                                <div>
                                    <label>Email</label><br/>
                                    <input  value={emailForLogin} onChange={(e)=>setEmailForLogin(e.target.value)} type="email" name="email" id="InputEmail" aria-describedby="emailHelp" />
                                    <div className={styles.formText}>Nunca compartilharemos seu e-mail com mais ninguém.</div>
                                </div>

                                <div className={styles.boxInput}>
                                    <label>Senha</label><br/>
                                    <input value={passwordForLogin} onChange={(e)=>setPasswordForLogin(e.target.value)} type="password" name="password" id="InputPassword" />
                                </div>

                                <p className={styles.redirect} onClick={ShowInputsRegister} >Não está cadastrado? Cadastre-se agora!</p><br/>
                                
                                <button className={styles.btn} onClick={handleLoginUser}>ENTRAR</button>
                                
                            </form>
                        </div>
                    </div>
                ) : (
                    <div className={styles.content}>
                        <h1>Cadastre-se</h1>
                        <div  className={styles.divForm}>
                            <form className={styles.formLoginRegister} method="POST">
                                <div>
                                    <label>Email</label><br/>
                                    <input value={emailForRegister} onChange={(e)=>setEmailForRegister(e.target.value)} type="email" name="email" id="InputEmail" aria-describedby="emailHelp" />
                                    <div className={styles.formText}>Nunca compartilharemos seu e-mail com mais ninguém.</div>
                                </div>

                                <div className={styles.boxInput}>
                                    <label>Nome</label><br/>
                                    <input value={nameForRegister} onChange={(e)=>setNameForRegister(e.target.value)} type="text" name="name" id="InputName"/>
                                </div>

                                <div className={styles.boxInput}>
                                    <label>Senha</label><br/>
                                    <input value={passwordForRegister} onChange={(e)=>setPasswordForRegister(e.target.value)} type="password" name="password" id="InputPassword"/>
                                </div>

                                <p className={styles.redirect} onClick={ShowInputsLogin}>Já é cadastrado?</p><br/>
                                
                                <button className={styles.btn} onClick={handleRegisterUser}>CADASTRAR</button>
                                
                                
                            </form>
                        </div>
                    </div>
                )}

            </section>


            <section className={styles.rightSection}>
                
                <div>
                    <img src="bookLogo.svg" alt=""/>
                </div>

            </section>
        </main>
    )
}

