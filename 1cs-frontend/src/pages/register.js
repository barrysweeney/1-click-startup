import React from "react"
import { Link } from "gatsby"

import Layout from "../components/layout"
import SEO from "../components/seo"

const Register = () => (
  <Layout>
    <SEO title="Register" />
    <h1>Register</h1>
    <form method="post" action="http://172.17.0.1:5000/register" style={{display: `grid`, gap: `10px`}}>
      <label style={{display: `grid`, gap: `10px`}}>
        Name
        <input type="text" name="name" id="user-name" />
      </label>
      <label style={{display: `grid`, gap: `10px`}}>
        Email
        <input type="text" name="number" id="customer-contact-number" />
      </label>
      <label style={{display: `grid`, gap: `10px`}}>
        Password
        <input type="password" name="password" id="password" />
      </label>
      <label style={{display: `grid`, gap: `10px`}}>
        Role
        <select>
          <option>Employee</option>
          <option>Manager</option>
        </select>
      </label>
      <button type="submit" id="submit-register">Register</button>
    </form>
    <Link to="/">Go back to the homepage</Link>
  </Layout>
)

export default Register
