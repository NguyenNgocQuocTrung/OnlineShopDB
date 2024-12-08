import React from "react";
import "@testing-library/jest-dom";
import Login from "./LoginForm"; 
import { useUser } from "../../utils/hooks/useUser";
import { render, screen, fireEvent, waitFor } from "@testing-library/react";
import { useNavigate } from "react-router-dom";

jest.mock("react-router-dom", () => ({
  useNavigate: jest.fn(),
  useLocation: jest.fn(),
}));

jest.mock("../../utils/hooks/useUser", () => ({
  useUser: jest.fn(),
}));

describe("Login Component", () => {
  let mockLogin, mockNavigate;

  beforeEach(() => {
    mockNavigate = jest.fn();
    mockLogin = jest.fn();
    global.alert = jest.fn();
    useUser.mockReturnValue({ login: mockLogin });
    useNavigate.mockReturnValue(mockNavigate);
  });
  //Test 1: Kiểm tra form render đúng
  it("Render LoginForm successfully", () => {
    render(<Login />);
    expect(screen.getByLabelText(/Email/i)).toBeInTheDocument();
    expect(screen.getByLabelText(/Password/i)).toBeInTheDocument();
    expect(screen.getByRole("button", { name: /Login/i })).toBeInTheDocument();
  });
  //Test 2: Kiểm tra thông báo lỗi khi không điền dữ liệu vào các trường bắt buộc
  it("Login with null input -> shows required inputs on null inputs", async () => {
    render(<Login />);

    fireEvent.click(screen.getByRole("button", { name: /Login/i }));

    await waitFor(() => {
      expect(screen.getByText(/Email is required/i)).toBeInTheDocument();
    });

    await waitFor(() => {
      expect(screen.getByText(/Password is required/i)).toBeInTheDocument();
    });
  });

  it("Login successfully", async () => {
    render(<Login />);

    const loginData = {
      email: "elroydevops@gmail.com",
      password: "0900000009",
    };
    mockLogin.mockResolvedValue(true); 
    fireEvent.change(screen.getByLabelText(/Email/i), {
      target: { value: loginData.email },
    });
    fireEvent.change(screen.getByLabelText(/Password/i), {
      target: { value: loginData.password },
    });
    fireEvent.click(screen.getByRole("button", { name: /Login/i }));
    await waitFor(() => {
      expect(mockNavigate).toHaveBeenCalledWith("/account");
    });
  });

  //Test 3: Kiểm tra thông báo lỗi khi đăng nhập với email hoặc mật khẩu không đúng
  it("Login with wrong email or password", async () => {
    render(<Login />);

    const loginData = {
      email: "abcshdsa@gmadls.com",
      password: "992832198sdas",
    };

    mockLogin.mockResolvedValue(true);
    fireEvent.change(screen.getByLabelText(/Email/i), {
      target: { value: loginData.email },
    });
    fireEvent.change(screen.getByLabelText(/Password/i), {
      target: { value: loginData.password },
    });
    fireEvent.click(screen.getByRole("button", { name: /Login/i }));

    await waitFor(() => {
      expect(global.alert).toHaveBeenCalledWith("Invalid email or password.");
    });
  });

  //Test 4: Kiểm tra thông báo lỗi khi đăng nhập với email không hợp lệ hoặc mật khẩu không đủ độ dài
  it("Login with invalid email or not enought length password", async () => {
    render(<Login />);

    const loginData = {
      email: "test",
      password: "123",
    };
    mockLogin.mockResolvedValue(true); 
    fireEvent.change(screen.getByLabelText(/Email/i), {
      target: { value: loginData.email },
    });
    fireEvent.change(screen.getByLabelText(/Password/i), {
      target: { value: loginData.password },
    });
    fireEvent.click(screen.getByRole("button", { name: /Login/i }));

    await waitFor(() => {
      expect(screen.getByText(/Invalid email address/i)).toBeInTheDocument();
    });
    await waitFor(() => {
      expect(
        screen.getByText(/Password must be at least 8 characters long/i)
      ).toBeInTheDocument();
    });
  });
});
