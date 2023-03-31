let out = '';

num = process.argv[2];

if (num % 3 == 0){
	out += 'Java';
}

if (num % 5 == 0){
	out += 'Script';
}

if (out.length == 0){
	console.log(num)
} else {
	console.log(out)
}