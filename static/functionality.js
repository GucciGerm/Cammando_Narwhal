let article = document.getElementById("interface");
let aside = document.getElementById("repo")
let mode = "repos"
let repos = document.getElementsByClassName("repo");
let repoCount = 0;
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
	repo.setAttribute('id', repoCount);
	repoCount++;

	repo.addEventListener("click", toggle)
}


function toggle() {
	if (mode === "repos")
		mode = "repo"
	else
		mode = "repos"

	article.className = mode;
	aside.className = mode;

	let name = this.getAttribute("data-name");
	let desc = this.getAttribute("data-desc");
	let collabs = this.getAttribute("data-contributors");
	let createdAt = this.getAttribute("data-createdAt");
	let updatedAt = this.getAttribute("data-updatedAt");
	let size = this.getAttribute("data-size");

	// "<div class='caption'></div> <div class='asideText'>"++"</div>"
	document.getElementById("asideName").innerHTML = "<div class='caption'>Name: </div> <div class='asideText'>"+name+"</div>";
	document.getElementById("asideDesc").innerHTML = "<div class='caption'>Desc: </div> <div class='asideText'>"+desc+"</div>";
	document.getElementById("asideCreatedAt").innerHTML = "<div class='caption'>Created At: </div> <div class='asideText'>"+createdAt+"</div>";
	document.getElementById("asideUpdatedAt").innerHTML = "<div class='caption'>Updated At: </div> <div class='asideText'>"+updatedAt+"</div>";
	document.getElementById("asideSize").innerHTML = "<div class='caption'>Commits: </div> <div class='asideText'>"+size+"</div>";
	// document.getElementById("asideContributors").innerHTML = "<div class='caption'>Contributors: </div> <div class='asideText'>"+collabs+"</div>";



}


