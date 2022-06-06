const fs = require("fs/promises");
const path = require("path");

async function main(argv) {
  const directory = path.join(__dirname, "results", argv[2]);
  const files = await fs.readdir(directory);
  files.sort((a, b) => a - b);
  const times = [];

  for (const file of files) {
    const data = await fs.readFile(path.join(directory, `${file}`));
    const lines = data.toString().split('\n');
    const timeLine = lines.find(line => line.indexOf('user') === 0);
    const time = +timeLine.split('m')[1].replace(',', '.').split('s')[0] + +timeLine.split('m')[0].split('\t')[1] * 60;
    console.log(file);
    times.push(time);
  }

  await fs.writeFile(path.join(__dirname, `${argv[2]}.result.json`), JSON.stringify(times));
}

main(process.argv);
