import logo from './logo.svg';
import Container from 'react-bootstrap/Container'
import './App.css';
import React, {Component} from "react"

class App extends Component {
    constructor(props) {
        super(props);
        this.state = {
            results: [],
            year: 2000,
            day: 1,
            searching: false,
        };
    }

    async yearHandler(e) {
        this.setState({
            year: e.target.value
        })
    }

    async dayHandler(e) {
        this.setState({
            day: e.target.value
        })
    }

    async submitHandler(e) {
        e.preventDefault()
        const date = e.target.date.value.split("-")
        const year = date[0]
        const monthCode = date[1]
        const day = parseInt(date[2], 10)

        const body = {}
        body.day = day
        body.month_code = monthCode
        body.year = year

        this.setState({
            searching: true,
        })

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
