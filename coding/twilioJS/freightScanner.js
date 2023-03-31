let contraband = 'contraband'

function scan(someStrs) {
	let length = someStrs.length;
	let contrabandCount = 0;
	someStrs.forEach(element => contrabandCount += isContra(element));
	return contrabandCount;
}

function isContra(testObj){
	if (testObj == contraband){
		return 1;
	}
	return 0;
}