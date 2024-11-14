import React from "react";
import { useForm } from "react-hook-form";
import { variables } from "../../utils/api/variables.js";
import axios from "axios";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import {
  faUser,
  faEnvelope,
  faLock,
  faPhone,
  faMapMarkerAlt,
  faCity,
  faFileAlt,
} from "@fortawesome/free-solid-svg-icons";

function Register() {
  const {
    register,
    handleSubmit,
    formState: { errors },
    watch,
  } = useForm();
  const password = watch("password");

  const onSubmit = async (registerData) => {
    try {
      const API_URL = variables.USER_API;
      const response = await axios.post(API_URL, registerData);
      alert("Registration successful: " + response.data);
    } catch (error) {
      alert(error.response?.data?.message || error.message);
    }
  };

  return (
    <div className="register">
      <h1>Register</h1>
      <form onSubmit={handleSubmit(onSubmit)}>
        {/* First Name */}
        <label className="input-label">
          First Name <span>*</span>
          <div className="input-wrapper">
            <FontAwesomeIcon icon={faUser} />
            <input
              className="input-field"
              type="text"
              {...register("firstName", {
                required: "First name is required",
                maxLength: {
                  value: 100,
                  message: "Must be at most 100 characters",
                },
                pattern: {
                  value: /^[A-Za-zÀ-ỹ\s]+$/u,
                  message: "Only characters and spaces are allowed",
                },
              })}
            />
          </div>
        </label>
        {errors.firstName && <span>{errors.firstName.message}</span>}

        {/* Last Name */}
        <label className="input-label">
          Last Name <span>*</span>
          <div className="input-wrapper">
            <FontAwesomeIcon icon={faUser} />
            <input
              className="input-field"
              type="text"
              {...register("lastName", {
                required: "Last name is required",
                maxLength: {
                  value: 100,
                  message: "Must be at most 100 characters",
                },
                pattern: {
                  value: /^[A-Za-zÀ-ỹ\s]+$/u,
                  message: "Only characters and spaces are allowed",
                },
              })}
            />
          </div>
        </label>
        {errors.lastName && <span>{errors.lastName.message}</span>}

        {/* Email */}
        <label className="input-label">
          Email <span>*</span>
          <div className="input-wrapper">
            <FontAwesomeIcon icon={faEnvelope} />
            <input
              className="input-field"
              type="email"
              {...register("email", {
                required: "Email is required",
                maxLength: {
                  value: 255,
                  message: "Must be at most 255 characters",
                },
                pattern: {
                  value: /^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}$/,
                  message: "Invalid email address",
                },
              })}
            />
          </div>
        </label>
        {errors.email && <span>{errors.email.message}</span>}

        {/* Phone */}
        <label className="input-label">
          Phone <span>*</span>
          <div className="input-wrapper">
            <FontAwesomeIcon icon={faPhone} />
            <input
              className="input-field"
              type="text"
              {...register("phone", {
                required: "Phone number is required",
                maxLength: {
                  value: 11,
                  message: "Must be at most 11 characters",
                },
                pattern: {
                  value: /^0[1-9][0-9]{8,9}$/,
                  message:
                    "Phone number must start with 0 and contain 10-11 digits",
                },
              })}
            />
          </div>
        </label>
        {errors.phone && <span>{errors.phone.message}</span>}

        {/* Password */}
        <label className="input-label">
          Password <span>*</span>
          <div className="input-wrapper">
            <FontAwesomeIcon icon={faLock} />
            <input
              className="input-field"
              type="password"
              {...register("password", {
                required: "Password is required",
                maxLength: {
                  value: 255,
                  message: "Must be at most 255 characters",
                },
                minLength: {
                  value: 8,
                  message: "Must be at least 8 characters",
                },
                pattern: {
                  value: /^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[!@#$%^&*])/,
                  message:
                    "Must contain uppercase, lowercase, number, and special character",
                },
              })}
            />
          </div>
        </label>
        {errors.password && <span>{errors.password.message}</span>}

        {/* Address (Optional) */}
        <label className="input-label">
          Address
          <div className="input-wrapper">
            <FontAwesomeIcon icon={faMapMarkerAlt} />
            <input
              className="input-field"
              type="text"
              {...register("address", {
                maxLength: {
                  value: 255,
                  message: "Must be at most 255 characters",
                },
              })}
            />
          </div>
        </label>
        {errors.address && <span>{errors.address.message}</span>}

        {/* City (Optional) */}
        <label className="input-label">
          City
          <div className="input-wrapper">
            <FontAwesomeIcon icon={faCity} />
            <input
              className="input-field"
              type="text"
              {...register("city", {
                maxLength: {
                  value: 100,
                  message: "Must be at most 100 characters",
                },
              })}
            />
          </div>
        </label>
        {errors.city && <span>{errors.city.message}</span>}

        {/* Postal Code (Optional) */}
        <label className="input-label">
          Postal Code
          <div className="input-wrapper">
            <FontAwesomeIcon icon={faFileAlt} />
            <input
              className="input-field"
              type="text"
              {...register("postalCode", {
                maxLength: {
                  value: 20,
                  message: "Must be at most 20 characters",
                },
                pattern: {
                  value: /^[A-Za-z0-9 ]{3,10}$/,
                  message: "Invalid postal code",
                },
              })}
            />
          </div>
        </label>
        {errors.postalCode && <span>{errors.postalCode.message}</span>}

        <button type="submit">REGISTER</button>
      </form>
    </div>
  );
}

export default Register;
