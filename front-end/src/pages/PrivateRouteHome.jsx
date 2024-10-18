import { Navigate } from "react-router-dom";

export default function PrivateRouteHome({children}){
    const name = localStorage.getItem("nameUser")

    return name ? children : <Navigate to='/login'/>
}