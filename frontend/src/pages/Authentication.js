import React, { useState } from 'react';
import Register from "../components/auth/RegisterForm";
import Login from "../components/auth/LoginForm";
import "../styles/auth.css";
function Authentication() {
  const [activeTab, setActiveTab] = useState("login");

  return (
    <div className="auth container">
      <div className="auth-container">
        {activeTab === "login" && <Login />}
        {activeTab === "signup" && <Register />}
      </div>

      {/* Tab Navigation */}
      <div className="tab-navigation">
        <a
          href="#"
          role="button"
          className={`tab ${activeTab === "login" ? "active" : ""}`}
          onClick={(e) => {
            e.preventDefault();
            setActiveTab("login");
          }}
        >
          Already a member?
        </a>
        <a
          href="#"
          role="button"
          className={`tab ${activeTab === "signup" ? "active" : ""}`}
          onClick={(e) => {
            e.preventDefault();
            setActiveTab("signup");
          }}
        >
          Not a member yet?
        </a>
      </div>
    </div>
  );
}

export default Authentication;
