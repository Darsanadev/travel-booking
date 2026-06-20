import { Link } from 'react-router-dom'
import './Login.css'

function Register() {
  return (
    <div className="auth-page">
      <div className="auth-brand">
        <div className="auth-brand-content">
          <span className="auth-logo">✈</span>
          <h1>Join Wanderlust</h1>
          <p>Create an account to book trips and track your adventures.</p>
        </div>
      </div>
          
      <div className="auth-form-panel">
        <div className="auth-card">
          <div className="auth-card-header">
            <h2>Register</h2>
            <p>Registration page coming soon.</p>
          </div>

          <p className="auth-footer">
            Already have an account?{' '}
            <Link to="/login" className="auth-link">
              Login
            </Link>
          </p>
        </div>
      </div>
    </div>
  )
}

export default Register
