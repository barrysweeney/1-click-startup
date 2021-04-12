import logo from './logo.svg';
import Container from 'react-bootstrap/Container'
import './App.css';
import React, { Component } from "react"

class App extends Component {
    constructor(props) {
        super(props);
        this.state = {
            results: [],
        };
    }

    async submitHandler(e) {
        e.preventDefault()
        const day = e.target.day.value
        const month = e.target.month.value
        const year = e.target.year.value

        const body = {}
        body.day = day
        body.month = month
        body.year = year

        const response = await fetch(`http://localhost:5000/`, {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(body)
        })
        if (response.status === 200) {
            const data = await response.json();
            this.setState({
                results: data.results,
            })
        }
    }

    render(){
        return (
            <Container>
                <h1>Customer Order</h1>
                <form onSubmit={this.submitHandler.bind(this)} action="#" style={{display: `grid`, gap: `10px`}}>
                    <label style={{ display: `grid`, gap: `10px` }}>
                        Day
                        <input type="range" min="1" max="31" value="1" className="slider" id="day"/>
                    </label>
                    <label style={{ display: `grid`, gap: `10px` }}>
                        Month
                            <select>
                                <option value="employee">January</option>
                                <option value="employee">February</option>
                                <option value="employee">March</option>
                                <option value="employee">April</option>
                                <option value="employee">May</option>
                                <option value="employee">June</option>
                                <option value="employee">July</option>
                                <option value="employee">August</option>
                                <option value="employee">September</option>
                                <option value="employee">October</option>
                                <option value="employee">November</option>
                                <option value="employee">December</option>
                            </select>
                    </label>
                    <label style={{ display: `grid`, gap: `10px` }}>
                        Day
                        <input type="range" min="1950" max="2021" value="2000" className="slider" id="year"/>
                    </label>
                    <button type="submit" id="submit-date">Search</button>
                </form>
                <div>
                    {this.state.results.length !==0 ? (
                        <ul>{
                            this.state.results.map(result =>
                                <li>{result}</li>
                            )
                        }</ul>
                    ): null}
                </div>
            </Container>
        )
    }
}

export default App;
