let loginBtn = document.getElementById("login-btn");
let logoutBtn = document.getElementById("logout-btn");

let token = localStorage.getItem("token");

if (token) {
    if (loginBtn) loginBtn.remove();
} else {
    if (logoutBtn) logoutBtn.remove();
}

if (logoutBtn) {
    logoutBtn.addEventListener("click", (e) => {
        e.preventDefault();
        localStorage.removeItem("token");
        window.location.href = "login.html";
    });
}

const projectsUrl = "http://127.0.0.1:8000/api/projects/";

function getProjects() {

    let token = localStorage.getItem("token");

    fetch(projectsUrl, {
        headers: {
            Authorization: `Bearer ${token}`
        }
    })
    .then(response => response.json())
    .then(data => {
        console.log("Projects:", data);
        buildProjects(data);
    })
    .catch(error => {
        console.error("Error loading projects:", error);
    });

}

function buildProjects(projects) {

    let projectsWrapper = document.getElementById("projects--wrapper");
    projectsWrapper.innerHTML = "";

    projects.forEach(project => {

        let image = project.feature_image
            ? `http://127.0.0.1:8000${project.feature_image}`
            : "http://127.0.0.1:8000/images/default.jpg";

        projectsWrapper.innerHTML += `
            <div class="project--card">

                <img src="${image}" alt="${project.title}">

                <div>

                    <div class="card--header">

                        <h3>${project.title}</h3>

                        <button
                            class="vote--option"
                            data-vote="up"
                            data-project="${project.id}">
                            +
                        </button>

                        <button
                            class="vote--option"
                            data-vote="down"
                            data-project="${project.id}">
                            -
                        </button>

                    </div>

                    <i>${project.vote_ratio}% Positive feedback</i>

                    <p>${project.description.substring(0,150)}</p>

                </div>

            </div>
        `;

    });

    addVoteEvents();

}

function addVoteEvents() {

    console.log("Adding Vote Events");

    let voteBtns = document.querySelectorAll(".vote--option");

    console.log(voteBtns);

    voteBtns.forEach(btn => {

        btn.addEventListener("click", function () {

            console.log("Vote button clicked");

            let token = localStorage.getItem("token");

            console.log("Token:", token);

            let vote = this.dataset.vote;
            let project = this.dataset.project;

            console.log(vote, project);

            fetch(`http://127.0.0.1:8000/api/projects/${project}/vote/`, {

                method: "POST",

                headers: {
                    "Content-Type": "application/json",
                    "Authorization": `Bearer ${token}`
                },

                body: JSON.stringify({
                    value: vote
                })

            })
            .then(response => {
                console.log("Status:", response.status);
                return response.json();
            })
            .then(data => {
                console.log("Vote Success:", data);
                getProjects();
            })
            .catch(error => {
                console.error("Vote Error:", error);
            });

        });

    });

}

getProjects();