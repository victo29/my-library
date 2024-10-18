import { useState } from "react";
import styles from "../modules/NavBar.module.css";

export default function NavBar() {
    
    const [isToggled, setIsToggled] = useState(null);

    // Muda valor da variável isToggled que será utilizada para controlar o menu recursivo
    const handleToggleClick = () => {
        if (isToggled === null || isToggled === false) {
            setIsToggled(true);  // Toggle ativado
        } else if (isToggled === true) {
            setIsToggled(false); // Toggle desativado
        }
    };

    return(
        <nav  className={`${styles.navBar} ${isToggled === null ? "" : isToggled ? styles.activeToggle : styles.desactiveToggle}`}>
            <div className={styles.topNavBar }>
                <div className={styles.boxImage}><img src="logoPng.svg" alt=""/></div> 
                <div className={styles.buttonToggle}>
                    <button onClick={handleToggleClick}> <img src="menu.svg" alt=""/> </button>
                </div>
            </div>
            
            <div className={styles.boxForm}>
                <form action="" className={styles.form}>
                    <input type="text" placeholder="Digite o que você quer pesquisar"/>
                </form>
            </div>
            <div className={styles.boxAnchor}>
                <a href="">Inserir</a>
            </div>
        </nav>
    )

}