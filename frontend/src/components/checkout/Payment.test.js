import React from 'react';
import { render, screen } from '@testing-library/react';
import Payment from './Payment';

describe('Payment Component', () => {
  test('renders title "PAYMENT OPTIONS"', () => {
    render(<Payment />);
    expect(screen.getByText('PAYMENT OPTIONS')).toBeInTheDocument();
  });

  test('renders a line divider', () => {
    render(<Payment />);
    const lineDivider = screen.getByRole('separator', { hidden: true });
    expect(lineDivider).toBeInTheDocument();
  });

  test('renders a payment option for Credit Card', () => {
    render(<Payment />);
    const creditCardOption = screen.getByLabelText(/Credit Card/i);
    expect(creditCardOption).toBeInTheDocument();
    expect(creditCardOption).toBeChecked(); // Kiểm tra ô radio có được chọn hay không
  });

  test('renders a message about redirecting to PayPal', () => {
    render(<Payment />);
    expect(screen.getByText('You will be redirected to PayPal to complete your payment.')).toBeInTheDocument();
  });
});
