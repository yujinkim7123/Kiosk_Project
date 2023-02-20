const express = require("express");
const router = express.Router();

router.get("/", (req, res) => {
    res.send({response : " i am slive"}).status(200);
}) 


module.exports = router