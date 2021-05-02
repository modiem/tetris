import { useState, useEffect } from 'react';
import { createStage } from '../gameHelpers';

export const useStage = (player, resetPlayer) => {
	const [Stage, setStage] = useState(createStage());

	useEffect(() => {
		const updateStage = prevStage => {

			// first flush the stage
			const newStage = prevStage.map(row => 
				row.map(cell => (cell[1] === 'clear' ? [0, 'clear'] : cell))
				);

			//Then draw the tetrominos
			player.tetrominos.forEach((row, y) => {
				row.forEach((value, x) => {
					if (value !== 0) {
						newStage[player.pos.y + y][player.pos.x + x] = [
							value,
							(player.collided ? 'merged' : 'clear'),
						];
					};		
				});
			});
			
			return newStage;
		};

		setStage(prev => updateStage(prev));
	}, [player]);

	return [Stage, setStage]
}