import React from "react"
import { Link } from "gatsby"

import Layout from "../components/layout"
import SEO from "../components/seo"

const CustomerOrder = () => (
  <Layout>
    <SEO title="Customer Order" />
    <h1>Customer Order</h1>
    <form method="post" action="http://172.17.0.1:5000/customer-order" style={{display: `grid`, gap: `10px`}}>
      <label style={{display: `grid`, gap: `10px`}}>
        Name
        <input type="text" name="name" id="customer-name" />
      </label>
      <label style={{display: `grid`, gap: `10px`}}>
        Contact Number
        <input type="text" name="number" id="customer-contact-number" />
      </label>
      <label style={{display: `grid`, gap: `10px`}}>
        Order
        <textarea name="customer-order" id="order"/>
      </label>
      <button type="submit" id="submit-customer-order">Send</button>
    </form>
    <Link to="/">Go back to the homepage</Link>
  </Layout>
)

export default CustomerOrder
