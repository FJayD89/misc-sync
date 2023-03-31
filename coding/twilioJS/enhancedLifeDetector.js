treeArg = process.argv[2];

if (treeArg == 0){
	console.log('alive');
} else if (treeArg == 1){
	console.log('flowering');
}else if (treeArg == 2){
	console.log('shedding');
} else {
	console.log('other');
}