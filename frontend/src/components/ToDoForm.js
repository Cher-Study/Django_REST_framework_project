import React from 'react'


class ToDoForm extends React.Component {
    constructor(props) {
        super(props)
        this.state = {
            'project': '',
            'text': '',
            'author': []
        }
    }

    handleChange(event) {
        this.setState(
            {
                [event.target.name]: event.target.value
            }
        );
    }

    handleUserChange(event) {
        if (!event.target.selectedOptios) {
            return
        }

        let users = []

        for (let i = 0; i < event.target.selectedOptios.length; i++) {
            users.push(parseInt(event.target.selectedOptios.item(i).value))
        }

        this.setState({
            'users': users
        })
    }

    handleSubmit(event) {
        this.props.createProject(this.state.project_name, this.state.repo, this.state.users)
        event.preventDefault()
    }

    render() {
        return (
            <form onSubmit={(event) => this.handleSubmit(event)}>
                <input type="text" name="project" placeholder="project"
                    value={this.state.project} onChange={(event) => this.handleChange(event)} />
                <input type="text" name="text" placeholder="text"
                    value={this.state.text} onChange={(event) => this.handleChange(event)} />
                <select onChange={(event) => this.handleUserChange(event)}>
                    {this.props.author.map((user) => <option value={user.id}>{user.user_name} {user.first_name} {user.last_name}</option>)}
                </select>

                <input type="submit" value="Create" />
            </form>
        )
    }
}
export default ToDoForm
