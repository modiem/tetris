import styled from 'styled-components';
import bgImage from '../../img/bg.png'

export const StyledTetrisWrapper = styled.div`
	width: 100vw;
	height: 100vh;
	display: flex;
	align-items: center;
	background: url(${ bgImage }) #000;
	background-size: cover;
	overflow: hidden;
`

export const StyledTetris = styled.div`
	width: 100%;
	display: flex;
	align-items: flex-start;
	padding: 40px;
	margin: 0 auto;
	max-width: 900px;

	aside {
		width: 100%;
		padding: 0 2vw;
		display: block;
		max-width: 200px;
	}	
` 