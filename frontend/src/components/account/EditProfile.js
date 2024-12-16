import React, { useState } from 'react';
import { useDispatch } from 'react-redux';
import { updateUser } from '../../store/actions/userActions';

function Profile({ currentUser }) {
  const dispatch = useDispatch();
  const [user, setUser] = useState(currentUser);
  const [errors, setErrors] = useState({});

  const handleChange = (e) => {
    const { name, value } = e.target;
    setUser({ ...user, [name]: value });
  };

  const validateField = (name, value) => {
    let error = "";
    if (name === "firstName" || name === "lastName") {
      if (value === null || value === undefined || value === "") {
        if (name === "firstName")
          error = "First name is required";
        else
          error = "Last name is required";
      } else if (!value.match(/^[A-Za-zÀ-ỹ\s]+$/u)) {
        error = "Only characters and spaces are allowed";
      } else if (value.length > 100) {
        error = "Must be at most 100 characters";
      }
    } else if (name === "phone") {
      if (value === null || value === undefined || value === "") {
        error = "Phone number is required";
      } else if (!value.match(/^0[1-9][0-9]{8,9}$/)) {
        error = "Phone number must start with 0 and contain 10-11 digits";
      }
    } else if (name === "postalCode") {
      if (value === null || value === undefined || value === "") {
      } else {
        if (!value.match(/^[A-Za-z0-9 ]{3,10}$/)) {
          error =
            "Invalid postal code. Only letters, numbers, and spaces are allowed. Must be between 3 and 10 characters";
        } 
      }
    } else if (name === "address" && value.length > 255) {
      error = "Must be at most 255 characters";
    } else if (name === "city" && value.length > 100) {
      error = "Must be at most 100 characters";
    }
    return error;
  };

  const validate = () => {
    const newErrors = {};
    Object.keys(user).forEach((key) => {
      const error = validateField(key, user[key]);
      if (error) {
        newErrors[key] = error;
      }
    });
    setErrors(newErrors);
    return Object.keys(newErrors).length === 0;
  };

  const onSave = async () => {
    if (!user.firstName || !user.lastName || !user.phone ) {
      alert('First name, last name, and phone number are required');
      return;
    }
    if (!validate()) {
      return;
    }
    
    try {
      const result = await dispatch(updateUser({ userId: user.UserID, user: { ...user, email: currentUser.email } }));
      if (result.meta.requestStatus === 'fulfilled') {
        alert('Update successful');
        console.log('Update successful');
      } else {
        alert('Update failed');
        console.log('Update failed');
      }
    } catch (error) {
        alert("Update failed");
      console.log('Update failed', error);
    }
  };

  return (
    <>
      <style>
        {`
          .error-text {
            color: red;
          }
        `}
      </style>
      <h1>Edit Profile</h1>
      <div>
        <div className="divider">
          <label>
            First Name
            <input name="firstName" value={user.firstName} onChange={handleChange} />
            {errors.firstName && <span className="error-text">{errors.firstName}</span>}
          </label>
          <label>
            Last Name
            <input name="lastName" value={user.lastName} onChange={handleChange} />
            {errors.lastName && <span className="error-text">{errors.lastName}</span>}
          </label>
        </div>
        <label>
          Email
          <input name="email" value={user.email} disabled />
          {errors.email && <span className="error-text">{errors.email}</span>}
        </label>
        <label>
          Phone Number
          <input name="phone" value={user.phone} onChange={handleChange} />
          {errors.phone && <span className="error-text">{errors.phone}</span>}
        </label>
      </div>
      <h2>Shipping Details</h2>
      <label>
        Address
        <input name="address" value={user.address} onChange={handleChange} />
        {errors.address && <span className="error-text">{errors.address}</span>}
      </label>
      <div className="divider">
        <label>
          Postal Code
          <input name="postalCode" value={user.postalCode} onChange={handleChange} />
          {errors.postalCode && <span className="error-text">{errors.postalCode}</span>}
        </label>
        <label>
          City
          <input name="city" value={user.city} onChange={handleChange} />
          {errors.city && <span className="error-text">{errors.city}</span>}
        </label>
      </div>
      <div className="divider">
        <button className='second-button'>CANCEL</button>
        <button onClick={onSave}>SAVE CHANGES</button>
      </div>
    </>
  );
}

export default Profile;
