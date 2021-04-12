import React, { Component } from "react"
import { Link } from "gatsby"

import Layout from "../components/layout"
import SEO from "../components/seo"
import { navigate } from "gatsby"

class Register extends Component {

  async registerHandler(e) {
    e.preventDefault()
    const name = e.target.name.value
    const email = e.target.email.value
    const password = e.target.password.value
    const role = e.target.role.value
    const business = e.target.business.value
    const body = {}
    body.name = name
    body.email = email
    body.password = password
    body.role = role
    body.business = business

    const response = await fetch(`http://172.17.0.1:5000/register`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify(body)
    })
    if (response.status === 200) {
      navigate("/login")
    }
  }

  render() {
    return (
      <Layout>
        <SEO title="Register" />
        <h1>Register</h1>
        <form onSubmit={this.registerHandler.bind(this)} action="#" style={{ display: `grid`, gap: `10px` }}>
          <label style={{ display: `grid`, gap: `10px` }}>
            Name
            <input type="text" name="name" id="user-name" />
          </label>
          <label style={{ display: `grid`, gap: `10px` }}>
            Email
            <input type="text" name="email" id="user-email" />
          </label>
          <label style={{ display: `grid`, gap: `10px` }}>
            Password
            <input type="password" name="password" id="user-password" />
          </label>
          <label style={{ display: `grid`, gap: `10px` }}>
            Business
            <input type="text" name="business" id="user-business" />
          </label>
          <label style={{ display: `grid`, gap: `10px` }}>
            Role
            <select id="user-role" name="role">
              <option value="employee">Employee</option>
              <option value="manager">Manager</option>
            </select>
          </label>
          <button type="submit" id="submit-register">Register</button>
        </form>
        <Link to="/">Go back to the homepage</Link>
      </Layout>
    )
  }
}

export default Register
