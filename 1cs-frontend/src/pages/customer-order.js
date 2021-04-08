import React, { Component } from "react"
import { Link } from "gatsby"

import Layout from "../components/layout"
import SEO from "../components/seo"
import { navigate } from "gatsby"

class CustomerOrder extends Component {

    async submitHandler(e) {
        e.preventDefault()
        const name = e.target.name.value
        const number = e.target.number.value
        const order = e.target.order.value

        const body = {}
        body.name = name
        body.number = number
        body.order = order

        const response = await fetch(`http://172.17.0.1:5000/customer/order/new`, {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(body)
        })
        if (response.status === 200) {
            navigate("/customer-order")
        }
    }

    render(){
        return (
            <Layout>
                <SEO title="Customer Order" />
                <h1>Customer Order</h1>
                <form onSubmit={this.submitHandler.bind(this)} action="#" style={{display: `grid`, gap: `10px`}}>
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
                        <textarea name="order" id="customer-order"/>
                    </label>
                    <button type="submit" id="submit-customer-order">Send</button>
                </form>
                <Link to="/">Go back to the homepage</Link>
            </Layout>
        )
    }
}

export default CustomerOrder
