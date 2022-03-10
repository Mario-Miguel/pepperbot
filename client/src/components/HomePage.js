import React from "react";
import { Link } from "react-router-dom";

class HomePage extends React.Component {
  render() {
    return (
      <div>
        <h1>Select a device</h1>
        <div>
          <Link to="/device/1" className="ui button">
            Device 1
          </Link>
          <Link to="/device/2" className="ui button">
            Device 2
          </Link>
          <Link to="/device/3" className="ui button">
            Device 3
          </Link>
        </div>
      </div>
    );
  }
}

export default HomePage;
