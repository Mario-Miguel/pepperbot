import "../styles/App.css";
import React from "react";
import HomePage from "./HomePage";
import Device from "./Device";
import { Router, Route, Switch } from "react-router-dom";
import history from "../history";

function App() {
  return (
    <div className="ui container">
      <Router history={history}>
        <div>
          <Switch>
            <Route path="/" exact component={HomePage} />
            <Route path="/device/:id" component={Device} />
          </Switch>
        </div>
      </Router>
    </div>
  );
}

export default App;
