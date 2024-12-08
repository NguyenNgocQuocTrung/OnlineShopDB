import { render, screen, fireEvent, waitFor } from "@testing-library/react";
import ProductCard from "./ProductItem";
import axios from "axios";
import { BrowserRouter as Router } from "react-router-dom";
import { useNavigate } from "react-router-dom";

import "@testing-library/jest-dom"; 