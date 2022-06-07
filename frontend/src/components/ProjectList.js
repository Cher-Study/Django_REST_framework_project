const ProjectItem = ({ project, deleteProject }) => {
    return (
        <tr>
            <td>{project.project_name}</td>
            <td>{project.repo}</td>
            <td>{project.users}</td>
            <td><button onClick={() => deleteProject(project.id)}>Delete</button></td>
        </tr>
    )
}

const ProjectList = ({ projects, deleteProject }) => {
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
            {projects.map((project) => <ProjectItem project={project} deleteProject={deleteProject} />)}
        </table>
    )
}

export default ProjectList