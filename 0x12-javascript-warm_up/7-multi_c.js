#!/usr/bin/node
if (isNaN(parseInt(process.argv[2]))) {
  console.log('Missing number of occurrences');
} else {
  const total = parseInt(process.argv[2]);
  for (let i = 0; i < total; i++) {
    console.log('C is fun');
  }
}
