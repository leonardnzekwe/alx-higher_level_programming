#!/usr/bin/node

const fs = require('fs').promises;
const process = require('process');
const argv = process.argv;

if (argv.length === 5) {
  const fileA = argv[2];
  const fileB = argv[3];
  const fileC = argv[4];

  concatFiles(fileA, fileB, fileC);

  async function concatFiles (srcA, srcB, dest) {
    try {
      const contentA = await fs.readFile(srcA, 'utf8');
      const contentB = await fs.readFile(srcB, 'utf8');

      const newContent = contentA + contentB;

      await fs.writeFile(dest, newContent);
    } catch (err) {
      console.error(err);
    }
  }
}
