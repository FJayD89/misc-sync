let str1 = process.argv[2].toUpperCase();
let str2 = process.argv[3].toUpperCase();

let strList = [str1, str2];
let sortList = [str1, str2];
sortList.sort();

if (str1 == str2) {
	console.log(0)
} else if (strList[0] == sortList[0]){
	console.log(-1)
} else {
	console.log(1)
}
// console.log(strList, sortList)