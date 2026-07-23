import React, { Component } from 'react'

export default class UserGreetingClass extends Component {
  render() {
    return (
      <div>Hello {this.props.user}!</div>
    )
  }
}

