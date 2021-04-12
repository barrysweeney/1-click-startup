import React, { Component } from "react"
import { Link } from "gatsby"

import Layout from "../components/layout"
import SEO from "../components/seo"
import { navigate } from "gatsby"

class Register extends Component {

  async loginHandler(e) {
    e.preventDefault()
    const email = e.target.email.value
    const password = e.target.password.value

    const body = {}
    body.email = email
    body.password = password

    const response = await fetch(`http://172.17.0.1:5000/login`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify(body)
    })
    if (response.status === 200) {
      navigate("/")
    }
  }

  render() {
    return (
      <Layout>
        <SEO title="Login" />
        <h1>Log In</h1>
        <form onSubmit={this.loginHandler.bind(this)} action="#" style={{ display: `grid`, gap: `10px` }}>
          <label style={{ display: `grid`, gap: `10px` }}>
            Email
            <input type="text" name="email" id="user-email" />
          </label>
          <label style={{ display: `grid`, gap: `10px` }}>
            Password
            <input type="password" name="password" id="user-password" />
          </label>
          <button type="submit" id="submit-login">Log In</button>
        </form>
        <Link to="/">Go back to the homepage</Link>
      </Layout>
    )
  }
}

export default Register
