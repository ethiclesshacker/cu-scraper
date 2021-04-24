const fs = require('fs');


// for (let i = 0; i < 1000; i++) {
//     let rawdata = fs.readFileSync('data.json');
//     let students = JSON.parse(rawdata);

//     // console.log(students[0]);

//     students.forEach(element => {
//         process.stdout.write(element.Name + "," + Object.keys(element.marks).splice(-1)[0] + "\n");
//     });
// }


for (let i = 0; i < 1000; i++) {
    fs.readFile('data.json', (err, data) => {
        if (err) throw err;
        let students = JSON.parse(data);

        students.forEach(element => {
            process.stdout.write(element.Name + "," + Object.keys(element.marks).splice(-1)[0] + "\n");
        });
    });
}
