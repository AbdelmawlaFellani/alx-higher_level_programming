#!/usr/bin/node
const args = process.argv;
let i = 2;
if (args[2] !== undefined) {
  while (args[i] !== undefined) {
    console.log(args[i]);
    i++;
  }
} else {
  console.log('No argument');
}
