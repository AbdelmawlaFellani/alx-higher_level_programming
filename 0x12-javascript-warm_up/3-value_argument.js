#!/usr/bin/node
const args = process.argv;
let i = 2;
if (args[2] !== undefined) {
  console.log(args[i]);
} else {
  console.log('No argument');
}
