import React from "react"
import { Link } from "gatsby"

import Layout from "../components/layout"
import SEO from "../components/seo"

const CustomerOrder = () => (
  <Layout>
    <SEO title="Customer Order" />
    <h1>Customer Order</h1>
    <form method="post" action="backend-uri/customer-order">
      <label>
        Name
        <input type="text" name="name" id="name" />
      </label>
      <br/>
      <label>
        Contact Number
        <input type="text" name="number" id="number" />
      </label>
      <br/>
      <label>
        Order
        <textarea name="order" id="order"/>
      </label>
      <br/>
      <button type="submit">Send</button>
    </form>
    <Link to="/">Go back to the homepage</Link>
  </Layout>
)

export default CustomerOrder
