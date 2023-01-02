function getFirstAmountSorted(arrayArg, num){
	let sorted = arrayArg.sort();
	let retList = sorted.slice(0,num);
	return retList;
}