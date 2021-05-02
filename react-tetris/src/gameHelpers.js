export const STAGE_WIDTH = 12;
export const STAGE_HEIGHT = 20;

// export a function that create the stage: 
// stage = A nested array (height * width * 2)
// Array.from(arrayLike, mapFn)

export const createStage = () => 
	Array.from(
		Array(STAGE_HEIGHT), () => (
			Array(STAGE_WIDTH).fill([0, 'clear'])
			)
		)