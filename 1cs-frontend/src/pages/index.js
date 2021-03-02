import React from "react"

import Layout from "../components/layout"
import SEO from "../components/seo"

// TODO: populate by a GET request to $BACKEND_URI$/checklist
const tasks = [
  "Turn on equipment",
  "Turn on customer order app",
  "Record Temperatures",
  "Defrost dough",
  "Defrost meat",
  "Dishes",
  "Empty bins",
  "Turn off customer order app",
  "Turn off equipment",
  "Ensure fridges and freezers are closed",
  "Lock freezer",
  "Lock back door",
  "Clean floor",
  "Record sales",
  "Lock front door"
]

const IndexPage = () => {
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
                <label style={{ padding: `10px` }}>{task}</label>
              </li>
            )
          }
        </ul>

      </div>
    </Layout>
  )
}

export default IndexPage
