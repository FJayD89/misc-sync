class TargetingSolution{
	constructor(position){
		this.x = position.x
		this.y = position.y
		this.z = position.z
	}
	
	target(){
		let retString = '(' + this.x.toString();
		retString += ', ' + this.y.toString();
		retString += ', ' + this.z.toString() + ')';
		return retString	
	}
}

const sln = new TargetingSolution({
  x: 45,
  y: 12,
  z: -1,
});

console.log(sln.target());