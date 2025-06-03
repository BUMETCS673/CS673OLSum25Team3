import { render, screen, fireEvent } from "@testing-library/react";
import ResetPasswordForm from "./ResetPasswordForm";

test("shows confirmation after submitting password", () => {
  render(<ResetPasswordForm />);
  const input = screen.getByLabelText(/new password/i);
  const button = screen.getByText(/submit/i);

  fireEvent.change(input, { target: { value: "newpass123" } });
  fireEvent.click(button);

  expect(screen.getByText(/Password submitted!/i)).toBeInTheDocument();
});
