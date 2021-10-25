const express = require("express");
const fs = require("fs");

const app = express();

app.use(express.json());

app.post('/graphql', (req, res) => {
	res.header('Content-Type', 'application/json');
	return res.end(getResponse(req.get("X_NOVI_GRAPHQL_CLIENT_DOCUMENT_NAME")));
});

function getResponse(docName) {
	return fs.readFileSync("./" + docName + ".json");
}

app.listen(8080);
