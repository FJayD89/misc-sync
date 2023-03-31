function scanAndFilter(someStrs, filterStr){
	let filtered = someStrs.filter(str => str != filterStr);
	return filtered;
}