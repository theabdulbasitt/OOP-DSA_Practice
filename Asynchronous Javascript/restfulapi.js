const express = require('express');
const app = express();
const PORT = 8080;

app.use(express.json());


app.get('/tshirts', (req, res) =>{
    
    res.status(200).send({
        tshirt:'red',
        size:'large'
    })
});


app.post('/tshirts/:id', (req, res) => {

    const { id } = req.params;
    const {logo} = req.body;

    if (!logo) {
        res.status(408).send( {message:'We need a logo'})
    }

    res.send({
        tshirt:`myshirt with ${logo} and ID of ${id}`,
    })

});

app.listen(
    PORT,
    () => console.log(`live on http://localhost:${PORT}`)
)

