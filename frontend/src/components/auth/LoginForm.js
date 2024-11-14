import React, { useState } from "react";
import { useForm } from "react-hook-form";
import { useNavigate, useLocation } from "react-router-dom";
import { icons } from "../../assets/icons/icons";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import { useUser } from "../../utils/hooks/useUser";

function Login() {
  const navigate = useNavigate();
  const location = useLocation();
  const { login } = useUser();

  const {
    register,
    handleSubmit,
    formState: { errors },
    setError,
  } = useForm();
  const [loading, setLoading] = useState(false); // Loading state
  const [loginError, setLoginError] = useState(""); // General login error message

  const onSubmit = async (loginData) => {
    setLoading(true); // Set loading state
    setLoginError(""); // Clear any previous error message

    try {
      const user = await login(loginData);

      if (user) {
        // Redirect to the "account" page if login is successful
        navigate("/account");
      } else {
        // Set a general login error message if login fails
        setLoginError("Invalid email or password.");
      }
    } catch (error) {
      // Handle error (e.g., network error)
      setLoginError(error.message || "Failed to login. Please try again.");
    } finally {
      setLoading(false); // Reset loading state
    }
  };

  return (
    <div className="login">
      <h1>Login</h1>
      <form onSubmit={handleSubmit(onSubmit)}>
        {/* Display login error */}
        {loginError && <div className="error-message">{loginError}</div>}

        {/* Email Field */}
        <label className="input-label">
          Email
          <div className="input-wrapper">
            <FontAwesomeIcon icon={icons.email} />
            <input
              className="input-field"
              type="email"
              {...register("email", {
                required: "Email is required",
                pattern: {
                  value: /^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}$/,
                  message: "Invalid email address",
                },
              })}
            />
          </div>
        </label>
        {errors.email && (
          <span className="error-text">{errors.email.message}</span>
        )}

        {/* Password Field */}
        <label className="input-label">
          Password
          <div className="input-wrapper">
            <FontAwesomeIcon icon={icons.lock} />
            <input
              className="input-field"
              type="password"
              {...register("password", {
                required: "Password is required",
                minLength: {
                  value: 8,
                  message: "Password must be at least 8 characters long",
                },
              })}
            />
          </div>
        </label>
        {errors.password && (
          <span className="error-text">{errors.password.message}</span>
        )}

        {/* Submit Button with Loading State */}
        <button type="submit" disabled={loading}>
          {loading ? "Logging in..." : "LOGIN"}
        </button>
      </form>
    </div>
  );
}

export default Login;
