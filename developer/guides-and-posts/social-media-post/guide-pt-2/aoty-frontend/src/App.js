import logo from './logo.svg';
import Container from 'react-bootstrap/Container'
import './App.css';
import React, {Component} from "react"

class App extends Component {
    constructor(props) {
        super(props);
        this.state = {
            results: [],
            searching: false,
        };
    }


    async submitHandler(e) {
        // Prevent browser's default form submission behaviour
        e.preventDefault()
        // Extract date from form and split into array
        const date = e.target.date.value.split("-")
        // Store year, month code, and formatted day from date array
        const year = date[0]
        const monthCode = date[1]
        const day = parseInt(date[2], 10) // 01 becomes 1, etc.

        // Create request body
        const body = {}
        body.day = day
        body.month_code = monthCode
        body.year = year

        // Set searching to true to display loading spinner
        this.setState({
            searching: true,
        })

        // Send POST request to backend and await a response
        const response = await fetch(`http://localhost:5000/`, {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(body)
        })
        // If the response is OK then set state to display albums
        if (response.status === 200) {
            const data = await response.json();
            this.setState({
                results: data.results,
                searching: false,
            })
        }
    }

    render() {
        return (
            <Container>
                <div style={{display: `grid`, gap: `20px`}}>
                    <h1>Album of the Year Searcher</h1>
                    <form onSubmit={this.submitHandler.bind(this)} action="#" style={{display: `grid`, gap: `10px`}}>
                        <label style={{display: `grid`, gap: `10px`}}>
                            Date
                            <input type="date" name="date" id="date" min="1950-01-01"/>
                        </label>
                        <button type="submit" id="submit-date">Search</button>
                    </form>
                    <div>
                        {this.state.searching ? <div className="text-center">
                            <div className="spinner-border" role="status">
                                <span className="sr-only">Loading...</span>
                            </div>
                        </div> : null}
                        {this.state.results.length !== 0 ? (
                            <ul>{
                                this.state.results.map((result, i) =>
                                    <li key={i}>{result}</li>
                                )
                            }</ul>
                        ) : null}
                    </div>
                </div>
            </Container>
        )
    }
}

export default App;
