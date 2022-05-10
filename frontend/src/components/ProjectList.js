const ProjectItem = ({ project }) => {
    return (
        <tr>
            <td>{project.project_name}</td>
            <td>{project.repo}</td>
            <td>{project.users}</td>
        </tr>
    )
}

const ProjectList = ({ projects }) => {
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
            {projects.map((project) => <ProjectItem project={project} />)}
        </table>
    )
}

export default ProjectList