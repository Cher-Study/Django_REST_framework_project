import React from 'react'
import axios from 'axios'
import './App.css';
import UserList from './components/UserList.js'
import ToDoList from './components/ToDoList.js'
import ToDoForm from './components/ToDoForm.js'
import ProjectList from './components/ProjectList.js'
import ProjectForm from './components/ProjectForm.js'
import LoginForm from './components/LoginForm.js'
import { HashRouter, BrowserRouter, Route, Routes, Link, Navigate, useLocation } from 'react-router-dom'


const NotFound = () => {
    var location = useLocation()
    return (
        <div>
            Page "{location.pathname}" not found
        </div>
    )
}

class App extends React.Component {
    constructor(props) {
        super(props)
        this.state = {
            'users': [],
            'projects': [],
            'todos': [],
            'token': ''
        }
    }

    obtainAuthToken(login, password) {
        axios
            .post('http://127.0.0.1:8000/api-auth-token/', { 'username': login, 'password': password })
            .then(response => {
                let token = response.data.token
                // console.log(token)
                localStorage.setItem('token', token)
                this.setState({
                    'token': token
                }, this.getData)
            })
            .catch(error => console.log(error))
    }

    isAuth() {
        return !!this.state.token
    }

    getHeaders() {
        if (this.isAuth()) {
            return {
                'Authorization': 'Token' + this.state.token
            }
        }
        return {}
    }

    componentDidMount() {
        let token = localStorage.getItem('token')
        this.setState({
            'token': token
        }, this.getData)
    }

    logOut() {
        localStorage.setItem('token', '')
        this.setState({
            'token': ''
        }, this.getData)
    }


    getData() {
        let headers = this.getHeaders()

        axios
            .get('http://127.0.0.1:8000/api/users/', { headers })
            .then(response => {
                let users = response.data.results
                this.setState({
                    'users': users
                })
            })
            .catch(error => {
                this.setState({
                    'users': [],
                })
                console.log(error)
            })

        axios
            .get('http://127.0.0.1:8000/api/projects/', { headers })
            .then(response => {
                let projects = response.data.results
                this.setState({
                    'projects': projects
                })
            })
            .catch(error => {
                this.setState({
                    'projects': [],
                })
                console.log(error)
            })

        axios
            .get('http://127.0.0.1:8000/api/todos/', { headers })
            .then(response => {
                let todos = response.data.results
                this.setState({
                    'todos': todos
                })
            })
            .catch(error => {
                this.setState({
                    'todos': [],
                })
                console.log(error)
            })
    }

    createProject(project_name, repo, users) {

        let headers = this.getHeaders()

        axios
            .delete('http://127.0.0.1:8000/api/projects/', { 'project_name': project_name, 'repo': repo, 'users': users }, { headers })
            .then(response => {
                this.getData()
            })
            .catch(error => {
                console.log(error)
            })

        console.log(project_name, repo, users)
    }

    deleteProject(id) {
        let headers = this.getHeaders()

        axios
            .delete(`http://127.0.0.1:8000/api/projects/${id}`, { headers })
            .then(response => {
                let projects = response.data.results
                this.setState({
                    'projects': this.state.projects.filter((project) => project.id !== id)
                })
            })
            .catch(error => {
                console.log(error)
            })

        console.log(id)
    }

    createToDo(project, text, author) {

        let headers = this.getHeaders()

        axios
            .delete('http://127.0.0.1:8000/api/todos/', { 'project': project, 'text': text, 'author': author }, { headers })
            .then(response => {
                this.getData()
            })
            .catch(error => {
                console.log(error)
            })

        console.log(project, text, author)
    }

    deleteToDo(id) {
        let headers = this.getHeaders()

        axios
            .delete(`http://127.0.0.1:8000/api/todos/${id}`, { headers })
            .then(response => {
                let todos = response.data.results
                this.setState({
                    'todos': this.state.todos.filter((todo) => todo.id !== id)
                })
            })
            .catch(error => {
                console.log(error)
            })

        console.log(id)
    }

    render() {
        return (
            <div>
                <BrowserRouter>
                    <nav>
                        <li><Link to='/'>Users</Link></li>
                        <li><Link to='/projects'>Projects</Link></li>
                        <li><Link to='/projects/create'>New project</Link></li>
                        <li><Link to='/todo'>ToDo</Link></li>
                        <li><Link to='/todo/create'>New ToDo</Link></li>
                        <li>
                            {this.isAuth() ? <button onClick={() => this.logOut()}>Logout</button> : <Link to='/login'>login</Link>}

                        </li>
                    </nav>

                    <Routes>
                        <Route exact path='/' element={<UserList users={this.state.users} />} />
                        <Route exact path='/users' element={<Navigate to='/' />} />
                        <Route exact path='/projects' element={<ProjectList projects={this.state.projects} users={this.state.users} deleteProject={(id) => this.deleteProject(id)} />} />
                        <Route exact path='/projects/create' element={<ProjectForm projects={this.state.users} createProject={(project_name, repo, users) => this.createProject(project_name, repo, users)} />} />
                        <Route exact path='/todo' element={<ToDoList todos={this.state.todos} />} />
                        <Route exact path='/todo/create' element={<ToDoForm todos={this.state.projects} createToDo={(project, text, author) => this.createToDo(project, text, author)} />} />
                        <Route exact path='/login' element={<LoginForm obtainAuthToken={(login, password) => this.obtainAuthToken(login, password)} />} />
                        <Route path='*' element={<NotFound />} />
                    </Routes>
                </BrowserRouter>
            </div>
        )
    }
}

export default App;