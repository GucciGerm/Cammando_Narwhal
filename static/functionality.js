let article = document.getElementById("interface");
let aside = document.getElementById("repo")
let mode = "repos"
let repos = document.getElementsByClassName("repo");
for (let repo of repos) {
	let name = document.createElement("div")
	name.setAttribute("class", "repoName")
	name.innerHTML = repo.getAttribute("data-name")
	let desc = document.createElement("div")
	desc.setAttribute("class", "description")
	let descText = repo.getAttribute("data-desc")
	if (descText === "None")
		desc.innerHTML = ""
	else desc.innerHTML = descText
	repo.append(name)
	repo.append(desc)

	repo.addEventListener("click", toggle)
}


function toggle() {
	if (mode === "repos")
		mode = "repo"
	else
		mode = "repos"

	article.className = mode;
	aside.className = mode;
}


