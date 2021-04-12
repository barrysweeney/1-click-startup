import React from "react"
import { Link } from "gatsby"

import Layout from "../components/layout"
import SEO from "../components/seo"

const ContactManager = () => (
  <Layout>
    <SEO title="Contact Manager" />
    <h1>Contact Manager</h1>
    <form method="post" action="backend-uri/contact-manager" style={{display: `grid`, gap: `10px`}}>
      <label style={{display: `grid`, gap: `10px`}}>
        Subject
        <input type="text" name="subject" id="subject" />
      </label>
      <br/>
      <label style={{display: `grid`, gap: `10px`}}>
        Message
        <textarea name="order" id="order"/>
      </label>
      <br/>
      <button type="submit">Send</button>
    </form>
    <Link to="/">Go back to the homepage</Link>
  </Layout>
)

export default ContactManager
