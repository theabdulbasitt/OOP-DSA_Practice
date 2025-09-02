console.log("Hi");

setTimeout(
    callback => console.log("Async function"),
    5000
);

console.log("Sync function");