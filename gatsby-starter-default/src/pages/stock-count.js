import React from "react"
import { Link } from "gatsby"

import Layout from "../components/layout"
import SEO from "../components/seo"

const StockCount = () => (
  <Layout>
    <SEO title="Stock Count" />
    <h1>Stock Count</h1>
    <form method="post" action="backend-uri/stock-count">
      <label>
        Item 1
        <input type="number" name="item1" id="item1" min="0" />
      </label>
      <br />
      <label>
        Item 2
        <input type="number" name="item2" id="item2" min="0" />
      </label>
      <br />
      <button type="submit">Send</button>
    </form>
    <Link to="/">Go back to the homepage</Link>
  </Layout>
)

export default StockCount
