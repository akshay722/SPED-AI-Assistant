import React from "react";
import "../App.css";

const Header = ({ onLogout }) => {
  return (
    <header>
      <h1>AI Agent for Sped Services</h1>
      <button onClick={onLogout}>Logout</button>
    </header>
  );
};

export default Header;
