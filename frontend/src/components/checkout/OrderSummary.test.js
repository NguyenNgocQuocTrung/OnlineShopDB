import React from 'react';
import { render, screen, fireEvent, waitFor } from '@testing-library/react';
import { PayPalScriptProvider, PayPalButtons } from '@paypal/react-paypal-js';
import OrderSummary from './OrderSummary'; // Đảm bảo đúng đường dẫn
import { useCart } from '../../utils/hooks/useCart';

// Mock PayPal và useCart
jest.mock('@paypal/react-paypal-js', () => ({
  PayPalScriptProvider: ({ children }) => <div>{children}</div>, // Mock PayPalScriptProvider
  PayPalButtons: ({ createOrder, onApprove, style }) => (
    <button onClick={() => onApprove({}, { order: { capture: jest.fn().mockResolvedValue({ payer: { email_address: 'test@paypal.com' }, purchase_units: [{ payments: { captures: [{ id: '1234' }] } }] }) } })}>
      Pay with PayPal
    </button>
  ), // Mock PayPalButtons
}));

jest.mock('../../utils/hooks/useCart', () => ({
  useCart: jest.fn(),
}));

describe('OrderSummary', () => {
  const mockOnPaymentComplete = jest.fn();
  const mockClearCart = jest.fn();

  const mockCartData = {
    subtotal: 100,
    delivery: 20,
    discount: 10,
    defaultTotal: 110,
    clearCart: mockClearCart,
  };

  beforeEach(() => {
    // Mock hook `useCart` trả về dữ liệu giỏ hàng giả
    useCart.mockReturnValue(mockCartData);

    // Mock global alert
    jest.spyOn(global, 'alert').mockImplementation(() => {});
  });

  afterEach(() => {
    jest.clearAllMocks(); // Dọn dẹp mocks sau mỗi test
  });

  test('renders order summary correctly', () => {
    render(<OrderSummary onPaymentComplete={mockOnPaymentComplete} />);

    // Kiểm tra các giá trị hiển thị
    expect(screen.getByText('Subtotal')).toBeInTheDocument();
    expect(screen.getByText('100')).toBeInTheDocument();

    expect(screen.getByText('Discount')).toBeInTheDocument();
    expect(screen.getByText('-10%')).toBeInTheDocument();

    expect(screen.getByText('Delivery')).toBeInTheDocument();
    expect(screen.getByText('20')).toBeInTheDocument();

    expect(screen.getByText('Total')).toBeInTheDocument();
    expect(screen.getByText('110')).toBeInTheDocument();
  });

  test('calls onApprove and clears the cart after PayPal payment', async () => {
    render(<OrderSummary onPaymentComplete={mockOnPaymentComplete} />);

    // Tìm và click vào nút thanh toán PayPal
    const payButton = screen.getByText('Pay with PayPal');
    fireEvent.click(payButton);

    // Kiểm tra xem các hành động đã được gọi đúng
    await waitFor(() => {
      expect(mockClearCart).toHaveBeenCalled();
      expect(mockOnPaymentComplete).toHaveBeenCalled();
    });

    // Kiểm tra xem alert có được gọi với đúng thông tin không
    expect(global.alert).toHaveBeenCalledWith(
      'An order confirmation will be sent to email: test@paypal.com. Transaction ID: 1234.'
    );
  });
});
