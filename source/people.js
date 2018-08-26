import React, { Component } from 'react';
import get_list_people from ./server/people


var data = get_list_people()

class App extends Component {
  render() {
    return (
      <div className="App">
        <p className="Table-header">Basic Table</p>
        <Table1 data={data}/>
      </div>
    );
  }
}

