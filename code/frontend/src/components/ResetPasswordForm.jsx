import React, { useState } from "react";

export default function ResetPasswordForm() {
  const [password, setPassword] = useState("");
  const [submitted, setSubmitted] = useState(false);

const handleSubmit = (e) => {
  e.preventDefault();
   setSubmitted(true);
};

  return (
    <form onSubmit={handleSubmit}>
      <label htmlFor="password">New Password:</label>
      <input
        id="password"
        type="password"
        value={password}
        onChange={(e) => setPassword(e.target.value)}
      />
      <button type="submit">Submit</button>
      {submitted && <p>Password submitted!</p>}
    </form>
  );
}
