const ProjectItem = ({ project, users, deleteProject }) => {
    let usersFilter = project.users.map(userId => users.find(u => u.id == userId).user_name)

    return (
        <tr>
            <td>{project.project_name}</td>
            <td>{project.repo}</td>
            <td>{project.users.map(userId => users.find(u => u.id == userId).user_name)}</td>
            <td><button onClick={() => deleteProject(project.id)}>Delete</button></td>
        </tr>
    )
}

const ProjectList = ({ projects, users, deleteProject }) => {
    return (
        <table>
            <th>
                Project name
            </th>
            <th>
                Repository
            </th>
            <th>
                Users
            </th>
            {projects.map((project) => <ProjectItem project={project} users={users} deleteProject={deleteProject} />)}
        </table>
    )
}

export default ProjectList