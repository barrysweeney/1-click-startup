import React from "react"
import { Link } from "gatsby"

import Layout from "../components/layout"
import SEO from "../components/seo"

const IndexPage = () => {
  const tasks = ["Empty bins", "Defrost meat", "Defrost dough", "Record sales", "Record Temperatures", "Turn on equipment", "Turn off equipment", "Turn on customer order app", "Turn off customer order app", "Dishes", "Clean floor", "Lock freezer", "Lock back door", "Lock front door", "Ensure fridges and freezers are closed"]
  return (
    <Layout>
      <SEO title="Home" />
      <h1>Daily Checklist</h1>
      <div style={{ maxWidth: `300px`, marginBottom: `1.45rem` }}>
        <ul style={{ listStyle: `none` }}>
          {
            tasks.map(task =>
              <li>
                <input type="checkbox" />
                <label>{task}</label>
              </li>
            )
          }
        </ul>

      </div>
    </Layout>
  )
}

export default IndexPage
