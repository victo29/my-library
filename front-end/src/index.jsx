import { StrictMode } from 'react';
import { createRoot } from 'react-dom/client';
import {Routes, Route, HashRouter } from 'react-router-dom';
import './App.css';

import Login from './pages/Login'
import PrivateRouteHome from './pages/PrivateRouteHome'
import Home from './pages/Home';

createRoot(document.getElementById('root')).render(
  <StrictMode>
    <HashRouter>
      <Routes>
        <Route path="/" element={<Login />} />
        <Route path='/Home' element={<PrivateRouteHome> <Home/> </PrivateRouteHome>}/>
        
      </Routes>
    </HashRouter>
  </StrictMode>,
);

