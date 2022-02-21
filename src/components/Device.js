import React from "react";
import history from "../history";

class Device extends React.Component {
  isValidId(deviceId) {
    return parseInt(deviceId) > 0 && parseInt(deviceId) < 4;
  }
  componentDidMount() {
    const id = this.props.match.params.id;
    console.log();
    if (!this.isValidId(id)) {
      history.push("/");
    }
  }

  render() {
    const id = this.props.match.params.id;
    return (
      <div>
        <h1>Device {id}</h1>
      </div>
    );
  }
}

export default Device;
