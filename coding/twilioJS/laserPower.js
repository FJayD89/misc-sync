function calculatePower(numList){
	let total = 0;
	numList.forEach(num => total += num);
	total *= 2;
	return total;
}