function addFirstToLast(arrayArg){
	let length = arrayArg.length
	if (length == 0){
		return '';
	}
	let concatenated = arrayArg[0];
	concatenated = concatenated + arrayArg[arrayArg.length-1]
	return concatenated
}