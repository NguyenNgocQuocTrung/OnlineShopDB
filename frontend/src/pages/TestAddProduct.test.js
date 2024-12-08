import { render, screen, fireEvent, waitFor } from "@testing-library/react";
import ProductDetail from "./ProductDetail";
import axios from "axios";
import { BrowserRouter as Router } from "react-router-dom";
import { useNavigate } from "react-router-dom";

import "@testing-library/jest-dom"; 
import { useProduct } from "../utils/hooks/useProduct";

jest.mock("react-router-dom", () => ({
    useNavigate: jest.fn(),
    useLocation: jest.fn(),
}));

jest.mock("../../utils/hooks/userCart", () => ({
    userCart: jest.fn(),
}));
jest.mock("../../utils/hooks/useProduct", () => ({
    useProduct: jest.fn(),
}));
jest.mock("../../utils/hooks/useUtil", () => ({
    useUtil: jest.fn(),
}));

describe("Product component", () => {
    let mockProduct;
    beforeEach(() => {
        mockProduct = jest.fn();
        useProduct.mock
    })
})