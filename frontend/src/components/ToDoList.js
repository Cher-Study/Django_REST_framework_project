const ToDoItem = ({ todo, users, deleteToDo }) => {
    let authorsFilter = todo.author.map(userId => users.find(u => u.id == userId).user_name)

    return (
        <tr>
            <td>{todo.project}</td>
            <td>{todo.text}</td>
            <td>{todo.created}</td>
            <td>{todo.updated}</td>
            <td>{todo.author.map(userId => users.find(u => u.id == userId).user_name)}</td>
            <td>{todo.is_active}</td>
            <td><button onClick={() => deleteToDo(todo.id)}>Delete</button></td>
        </tr>
    )
}

const ToDoList = ({ todos, author, deleteToDo }) => {
    return (
        <table>
            <th>
                Project
            </th>
            <th>
                Text
            </th>
            <th>
                Created
            </th>
            <th>
                Updated
            </th>
            <th>
                aurhor
            </th>
            <th>
                Is active
            </th>
            {todos.map((todo) => <ToDoItem todo={todo} author={author} deleteToDo={deleteToDo} />)}

        </table>
    )
}

export default ToDoList