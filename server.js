var express = require("express");

var app = express();

// Configuration
app.use("/static", express.static(__dirname + "/static"));

app.engine("ejs", require("ejs").renderFile);
app.set("view engine", "ejs");

app.get("/", function (req, res) {
  res.render("index");
});

var server = app.listen(3000, function () {
  console.log("Listening on port %d", server.address().port);
});
