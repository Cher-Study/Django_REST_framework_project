import React from 'react'
import axios from 'axios'
import UserList from './components/UserList.js'

class App extends React.Component {
  constructor(props) {
    super(props)
    this.state = {
      'users': []
    }
  }

  componentDidMount() {
    axios
      .get('http://127.0.0.1:8000/api/users/')
      .then(response => {
        let users = response.data.results
        this.setState({
          'users': users
        })
      })
      .catch(error => console.log(error))
  }

  render() {
    return (
      <div>
        <div class='menu'></div>

        <div> <UserList users={this.state.users} /> </div>

        <div class='footer'></div>
      </div>
    )
  }
}

export default App;
