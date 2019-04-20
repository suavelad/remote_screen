import React from 'react'
import ReactDOM from 'react-dom'
import './index.css'
import {Route,BrowserRouter as Router, Switch} from 'react-router-dom'
import App from './App'
import About from "./Components/About"
import Contact from "./Components/Contact"
import Admin from './Components/Admin'
import Error from "./Components/Error404"
import * as serviceWorker from './serviceWorker'

const routing = (
    <Router>
        <div>
            <Switch>
                <Route exact path="/" component={App} />
                <Route path="/about" component= {About} />
                <Route path= "/contact" component ={Contact} />
                <Route path="/admin" component={Admin} />
                <Route component = {Error} />
            </Switch>
            
        </div>
    </Router>
)

ReactDOM.render(routing, document.getElementById("root"))

// If you want your app to work offline and load faster, you can change
// unregister() to register() below. Note this comes with some pitfalls.
// Learn more about service workers: https://bit.ly/CRA-PWA
serviceWorker.unregister();
