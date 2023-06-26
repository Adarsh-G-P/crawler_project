
// sets up the React application, renders the main <App> component, 
//and provides a hook for measuring and reporting web vitals. 
//The rendered application will be injected into the specified root element in the HTML document,
// replacing the placeholder <div id="root"></div>.


import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';
import App from './App';
import reportWebVitals from './reportWebVitals';
// Bootstrap CSS
import "bootstrap/dist/css/bootstrap.min.css";
// Bootstrap Bundle JS
import "bootstrap/dist/js/bootstrap.bundle.min";

//Creates a root element for rendering the React application.

const root = ReactDOM.createRoot(document.getElementById('root'));

//Renders the React application inside the root element.
root.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>
);

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals();
