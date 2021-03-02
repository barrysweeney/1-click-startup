import React from "react"
import { Link } from "gatsby"

import Layout from "../components/layout"
import SEO from "../components/seo"

const StockCount = () => {
  const stockItems = ["Water Bottles", "Cheese Bags"]

 return (
  <Layout>
    <SEO title="Stock Count" />
    <h1>Stock Count</h1>
    <form method="post" action="backend-uri/stock-count" style={{display: `grid`, gap: `10px`}}>
      <ul style={{ listStyle: `none` }}>
        {
          stockItems.map(item =>
            <li>
              <input type="number" min={"0"} />
              <label style={{ padding: `10px` }}>{item}</label>
            </li>
          )
        }
      </ul>
      <button type="submit">Send</button>
    </form>
    <Link to="/">Go back to the homepage</Link>
  </Layout>
)
}

export default StockCount
