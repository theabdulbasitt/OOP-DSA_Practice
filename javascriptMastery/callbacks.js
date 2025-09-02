

hello(goodbye);

function hello (goodbye) {
    setTimeout ( function () {
        console.log('Hello');
        goodbye();
    }, 3000);
    
};

function goodbye () {
    console.log("Bye");
};