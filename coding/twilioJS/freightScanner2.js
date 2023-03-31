let contraband = 'contraband';

function scan(someStrs){
	let length = someStrs.length;
	let indexArray = [];
	for (index = 0; index < length; index ++){
		if (someStrs[index] == contraband){
			indexArray.push(index);
		}
	}
	return indexArray;
}