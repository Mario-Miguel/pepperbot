import React from "react";
import history from "../history";
import { connect } from "react-redux";
import { deviceReady } from "../actions";

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
        <button
          className={`ui button ${this.props.ready ? "negative" : "primary"}`}
          onClick={() => this.props.deviceReady(id)}
        >
          Ready to use!
        </button>
      </div>
    );
  }
}

const mapStateToProps = (state) => {
  console.log(state);
  return {};
};

export default connect(mapStateToProps, { deviceReady })(Device);
