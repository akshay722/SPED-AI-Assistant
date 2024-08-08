import React, { useState } from "react";
import Login from "./components/Login";
import Header from "./components/Header";
import AddDataForm from "./components/AddDataForm";
import DataTable from "./components/DataTable";
import axios from "axios";
import "./App.css";

function App() {
  const [isAuthenticated, setIsAuthenticated] = useState(false);
  const [data, setData] = useState([]);

  const handleLogin = async (email, password) => {
    try {
      const response = await axios.post("http://localhost:8000/login", {
        email,
        password,
      });
      console.log(response);
      if (response.status === 200) {
        setIsAuthenticated(true);
      }
    } catch (error) {
      console.error("Login failed", error);
    }
  };

  const handleLogout = () => {
    setIsAuthenticated(false);
  };

  const handleAddData = async () => {};

  if (!isAuthenticated) {
    return <Login onLogin={handleLogin} />;
  }

  return (
    <div className="App">
      <Header onLogout={handleLogout} />
      <AddDataForm onAddData={handleAddData} />
      <DataTable data={data} />
    </div>
  );
}

export default App;
