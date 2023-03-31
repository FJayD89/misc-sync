class Ducktypium{
	constructor(color){
		this.color = color;
		checkColor(color);
		this.calibrationSequence = [];
	}
	
	refract(color){
		checkColor(color);
		if (color == this.color){
			return color
		}
		
		let colList = [color, this.color];
		
		if (colList.includes('red')){
			if (colList.includes('blue')){
				return 'purple';
			}
			
			if (colList.includes('yellow')){
				return 'orange';
			}
		}
		
		//only remaining option
		return 'green';
	}
	
	calibrate(numList){
		numList.sort()
		numList.forEach(num => this.calibrationSequence.push(num*3));
	}
}

function checkColor(color){
	if (color != 'red' && color != 'blue' && color != 'yellow'){
		throw new Error('Invalid color!');
	}
}

