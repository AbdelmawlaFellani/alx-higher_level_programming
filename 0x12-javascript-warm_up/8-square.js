#!/usr/bin/node
const size = Math.floor(Number(process.argv[2]));
if (isNaN(size)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < size; i++) {
    let str = '';
    for (let j = 0; j < size; j++) str += 'X';
    console.log(str);
  }
}
