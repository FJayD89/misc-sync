function calculateMass(someStrs) {
	totalLen = 0;
	someStrs.forEach(element => totalLen += element.length);
	return totalLen;
}