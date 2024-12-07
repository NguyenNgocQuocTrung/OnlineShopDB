import { render, screen, fireEvent, waitFor } from "@testing-library/react";
import Register from "./RegisterForm";
import axios from "axios";
import { BrowserRouter as Router } from "react-router-dom";
import { useNavigate } from "react-router-dom";

import "@testing-library/jest-dom";
// Mock axios module và useNavigate
jest.mock("axios");
jest.mock("react-router-dom", () => ({
  useNavigate: jest.fn(),
  useLocation: jest.fn(),
}));

describe("Register Component", () => {
  let mockNavigate;

  beforeEach(() => {
    mockNavigate = jest.fn();
    global.alert = jest.fn(); 
    useNavigate.mockReturnValue(mockNavigate); 
  });
  afterEach(() => {
    jest.clearAllMocks();
  });
  // Test 1: Kiểm tra form render đúng
  it("Render RegisterForm successfully", () => {
    render(<Register />);
    expect(screen.getByLabelText(/First Name/i)).toBeInTheDocument();
    expect(screen.getByLabelText(/Last Name/i)).toBeInTheDocument();
    expect(screen.getByLabelText(/Email/i)).toBeInTheDocument();
    expect(screen.getByLabelText(/Phone/i)).toBeInTheDocument();
    expect(screen.getByLabelText(/Password/i)).toBeInTheDocument();
    expect(screen.getByLabelText(/Address/i)).toBeInTheDocument();
    expect(screen.getByLabelText(/City/i)).toBeInTheDocument();
    expect(screen.getByLabelText(/Postal Code/i)).toBeInTheDocument();

    expect(
      screen.getByRole("button", { name: /REGISTER/i })
    ).toBeInTheDocument();
  });

  // Test 2: Kiểm tra thông báo lỗi khi không điền dữ liệu vào các trường bắt buộc
  it("should show error message if required fields are empty", async () => {
    render(<Register />);

    fireEvent.click(screen.getByRole("button", { name: /REGISTER/i }));

    expect(
      await screen.findByText(/First name is required/i)
    ).toBeInTheDocument();
    expect(
      await screen.findByText(/Last name is required/i)
    ).toBeInTheDocument();
    expect(await screen.findByText(/Email is required/i)).toBeInTheDocument();
    expect(
      await screen.findByText(/Phone number is required/i)
    ).toBeInTheDocument();
    expect(
      await screen.findByText(/Password is required/i)
    ).toBeInTheDocument();
  });
  it("should show errors for all invalid inputs", async () => {
    render(<Register />);

    fireEvent.input(screen.getByLabelText(/First Name/i), {
      target: { value: "123" },
    });
    fireEvent.input(screen.getByLabelText(/Last Name/i), {
      target: { value: "123" },
    });
    fireEvent.input(screen.getByLabelText(/Email/i), {
      target: { value: "invalid-email" },
    });
    fireEvent.input(screen.getByLabelText(/Phone/i), {
      target: { value: "12345" },
    });
    fireEvent.input(screen.getByLabelText(/Password/i), {
      target: { value: "short" },
    });
    fireEvent.input(screen.getByLabelText(/Address/i), {
      target: { value: "valid address" },
    });
    fireEvent.input(screen.getByLabelText(/City/i), {
      target: {
        value: "Valid City",
      },
    });
    fireEvent.input(screen.getByLabelText(/Postal Code/i), {
      target: { value: "12" },
    });

    fireEvent.click(screen.getByRole("button", { name: /REGISTER/i }));

    await waitFor(() => {
      const firstlastName = screen.queryAllByText(
        /Only characters and spaces are allowed/i
      );
      expect(firstlastName.length).toBeGreaterThan(1);
    });

    expect(
      await screen.findByText(/Invalid email address/i)
    ).toBeInTheDocument(); 
    expect(
      await screen.findByText(
        /Phone number must start with 0 and contain 10-11 digits/i
      )
    ).toBeInTheDocument();
    expect(
      await screen.findByText(/Must be at least 8 characters/i)
    ).toBeInTheDocument(); 
    expect(
      await screen.findByText(/Must be at least 3 characters/i)
    ).toBeInTheDocument();
  });
  // Test 3: Kiểm tra điều hướng sau khi đăng ký thành công
  it("should navigate to /account after successful registration", async () => {
    render(<Register />);
    axios.post.mockResolvedValueOnce(true);
    fireEvent.change(screen.getByLabelText(/First Name/i), {
      target: { value: "John" },
    });
    fireEvent.change(screen.getByLabelText(/Last Name/i), {
      target: { value: "Doe" },
    });
    fireEvent.change(screen.getByLabelText(/Email/i), {
      target: { value: "john.doe@example.com" },
    });
    fireEvent.change(screen.getByLabelText(/Phone/i), {
      target: { value: "0123456789" },
    });
    fireEvent.change(screen.getByLabelText(/Password/i), {
      target: { value: "Password1!" },
    });

    fireEvent.click(screen.getByRole("button", { name: /REGISTER/i }));
    await waitFor(() => expect(mockNavigate).toHaveBeenCalledWith("/account"));
  });
});
