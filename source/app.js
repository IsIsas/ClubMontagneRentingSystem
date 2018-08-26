
var React = require('react');
var ReactDOM = require('react-dom');
var createReactClass = require('create-react-class');
var Hello = createReactClass({
 render: function () {
 return <div>Hello {this.props.name}</div>;
 }
});
ReactDOM.render(
 <Hello name="World" />,
 document.getElementById('react-container')
);