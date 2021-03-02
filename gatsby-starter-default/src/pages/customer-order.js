import React from "react"
import { Link } from "gatsby"

import Layout from "../components/layout"
import SEO from "../components/seo"

const CustomerOrder = () => (
  <Layout>
    <SEO title="Customer Order" />
    <h1>Customer Order</h1>
    <form method="post" action="$backend-uri$/customer-order" style={{display: `grid`, gap: `10px`}}>
      <label style={{display: `grid`, gap: `10px`}}>
        Name
        <input type="text" name="name" id="name" />
      </label>
      <label style={{display: `grid`, gap: `10px`}}>
        Contact Number
        <input type="text" name="number" id="number" />
      </label>
      <label style={{display: `grid`, gap: `10px`}}>
        Order
        <textarea name="order" id="order"/>
      </label>
      <button type="submit">Send</button>
    </form>
    <Link to="/">Go back to the homepage</Link>
  </Layout>
)

export default CustomerOrder
