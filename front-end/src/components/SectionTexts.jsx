
import styles from "../modules/SectionTexts.module.css"

export default function SectionTexts(){
    const nameUser = localStorage.getItem("nameUser")

    return(
        <section className={styles.fistSection}>
            <div className={styles.boxText}>
                <h1>Descubra um novo capítulo na sua vida!</h1>
                <h2>Cada livro é uma porta para um mundo de possibilidades; abra uma e deixe a sua imaginação voar!</h2>
            </div>
            <div className={styles.boxUser}>
                <h1>Seja bem vindo {nameUser} </h1>
                <button>Logout</button>
            </div>
        </section>
    )
}