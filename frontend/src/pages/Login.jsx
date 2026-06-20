import { useState } from 'react'
import { Link } from 'react-router-dom'
import './Login.css'

function validateForm(email, password) {
  const errors = {}

  if (!email.trim()) {
    errors.email = 'Email is required'
  } else if (!/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email.trim())) {
    errors.email = 'Enter a valid email address'
  }

  if (!password) {
    errors.password = 'Password is required'
  } else if (password.length < 6) {
    errors.password = 'Password must be at least 6 characters'
  }

  return errors
}

function Login() {
  const [email, setEmail] = useState('')
  const [password, setPassword] = useState('')
  const [errors, setErrors] = useState({})
  const [touched, setTouched] = useState({})
  const [isSubmitting, setIsSubmitting] = useState(false)

  const handleBlur = (field) => {
    setTouched((prev) => ({ ...prev, [field]: true }))
    setErrors(validateForm(email, password))
  }

  const handleSubmit = async (event) => {
    event.preventDefault()

    const validationErrors = validateForm(email, password)
    setErrors(validationErrors)
    setTouched({ email: true, password: true })

    if (Object.keys(validationErrors).length > 0) {
      return
    }

    setIsSubmitting(true)

    try {
      // Ready for backend integration: POST /auth/login
      await new Promise((resolve) => setTimeout(resolve, 600))
    } finally {
      setIsSubmitting(false)
    }
  }

  const showError = (field) => touched[field] && errors[field]

  return (
    <div className="auth-page">
      <div className="auth-brand">
        <div className="auth-brand-content">
          <span className="auth-logo">✈</span>
          <h1>Wanderlust</h1>
          <p>Discover destinations, book packages, and start your next adventure.</p>
        </div>
      </div>

      <div className="auth-form-panel">
        <div className="auth-card">
          <div className="auth-card-header">
            <h2>Welcome back</h2>
            <p>Sign in to manage your bookings and explore new trips.</p>
          </div>

          <form className="auth-form" onSubmit={handleSubmit} noValidate>
            <div className={`form-group ${showError('email') ? 'has-error' : ''}`}>
              <label htmlFor="email">Email</label>
              <input
                id="email"
                type="email"
                name="email"
                autoComplete="email"
                placeholder="you@example.com"
                value={email}
                onChange={(event) => setEmail(event.target.value)}
                onBlur={() => handleBlur('email')}
                aria-invalid={Boolean(showError('email'))}
                aria-describedby={showError('email') ? 'email-error' : undefined}
              />
              {showError('email') && (
                <span id="email-error" className="field-error" role="alert">
                  {errors.email}
                </span>
              )}
            </div>

            <div className={`form-group ${showError('password') ? 'has-error' : ''}`}>
              <label htmlFor="password">Password</label>
              <input
                id="password"
                type="password"
                name="password"
                autoComplete="current-password"
                placeholder="Enter your password"
                value={password}
                onChange={(event) => setPassword(event.target.value)}
                onBlur={() => handleBlur('password')}
                aria-invalid={Boolean(showError('password'))}
                aria-describedby={showError('password') ? 'password-error' : undefined}
              />
              {showError('password') && (
                <span id="password-error" className="field-error" role="alert">
                  {errors.password}
                </span>
              )}
            </div>

            <button type="submit" className="auth-submit" disabled={isSubmitting}>
              {isSubmitting ? 'Signing in…' : 'Login'}
            </button>
          </form>

          <p className="auth-footer">
            Don&apos;t have an account?{' '}
            <Link to="/register" className="auth-link">
              Register
            </Link>
          </p>
        </div>
      </div>
    </div>
  )
}

export default Login
