const readline = require('readline');

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout,
});

function ask(question) {
    return new Promise((resolve) => rl.question(question, resolve));
}

async function main() {
    const choice = await ask("Welcome to Area Calculator. \n Please Enter your Choice. \n1.Area of Rectangle. \n2.Area of Triangle. \n");

    if (choice == '1') {
        const l = await ask('Enter the Length: ');
        const b = await ask('Enter the breadth: ');
        const result = Number(l) * Number(b);
        console.log('The Area is ' + result);
    }

    if (choice == '2') {
        const h = await ask('Enter the height: ');
        const b = await ask('Enter the base: ');
        const result = Number(h) * Number(b) / 2;
        console.log('The Area is ' + result);
    }


    rl.close();
}

main();


