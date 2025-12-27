# Auth API

## POST /login

Parameters:
- email: string
- otp: string
- device_id: string

Description:
Authenticates a user using email, password, and OTP with enhanced security.
Example:
POST /login
{
  "email": "priya12@gmail.com",
  "password": "secret",
  "otp": "123456"
}
