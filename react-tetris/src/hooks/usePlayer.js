import { useState, useCallback } from 'react';
import { TETROMINOS, randomTetriminos } from '../tetrominos'
import { STAGE_WIDTH } from '../gameHelpers';


export const usePlayer = () => {
	const [Player, setPlayer] = useState({
		pos: {x:0, y:0},
		tetrominos: TETROMINOS[0].shape,
		collided: false,
	});

	const updatePlayerPos = ({ x, y, collided }) => {
		setPlayer(prev => ({
			...prev,
			pos: {x: (prev.pos.x += x), y: (prev.pos.y += y)},
			collided,
		}))
	};

	const resetPlayer = useCallback(() => {
		setPlayer({
			pos: {x: STAGE_WIDTH/2 - 2, y:0},
			tetrominos: randomTetriminos().shape,
			collided:false,
		})
	}, []);

	return [Player, updatePlayerPos, resetPlayer];
}