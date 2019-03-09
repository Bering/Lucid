var ul = document.getElementById("usersList");
for (const [username, user] of Object.entries(users)) {
	var li = document.createElement("li");
	var text = document.createTextNode(username);
	li.appendChild(text);
	ul.appendChild(li);	
}
